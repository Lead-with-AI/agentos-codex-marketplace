#!/usr/bin/env python3
"""Build a UTC RRULE candidate and verify the next local run time."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo


WEEKDAY_MAP = {
    "monday": "MO",
    "tuesday": "TU",
    "wednesday": "WE",
    "thursday": "TH",
    "friday": "FR",
    "saturday": "SA",
    "sunday": "SU",
}


def parse_time(value: str) -> time:
    for fmt in ("%H:%M", "%H:%M:%S"):
        try:
            return datetime.strptime(value, fmt).time()
        except ValueError:
            pass
    raise argparse.ArgumentTypeError("time must be HH:MM, e.g. 07:00")


def next_local_run(now_utc: datetime, tz: ZoneInfo, local_t: time, frequency: str, weekday: str | None) -> datetime:
    now_local = now_utc.astimezone(tz)
    candidate = datetime.combine(now_local.date(), local_t, tzinfo=tz)

    if frequency == "daily":
        if candidate <= now_local:
            candidate += timedelta(days=1)
        return candidate

    if frequency == "weekday":
        while candidate <= now_local or candidate.weekday() >= 5:
            candidate += timedelta(days=1)
        return candidate

    if frequency == "weekly":
        if not weekday:
            raise ValueError("--weekday is required for weekly frequency")
        target = list(WEEKDAY_MAP).index(weekday.lower())
        days_ahead = (target - candidate.weekday()) % 7
        candidate += timedelta(days=days_ahead)
        if candidate <= now_local:
            candidate += timedelta(days=7)
        return candidate

    raise ValueError("frequency must be daily, weekday, or weekly")


def observes_dst(tz: ZoneInfo, year: int) -> bool:
    jan = datetime(year, 1, 1, tzinfo=tz).utcoffset()
    jul = datetime(year, 7, 1, tzinfo=tz).utcoffset()
    return jan != jul


def build_rrule(next_utc: datetime, frequency: str, weekday: str | None) -> str:
    parts = [f"FREQ={'DAILY' if frequency in {'daily', 'weekday'} else 'WEEKLY'}"]
    if frequency == "weekday":
        parts.append("BYDAY=MO,TU,WE,TH,FR")
    elif frequency == "weekly" and weekday:
        parts.append(f"BYDAY={WEEKDAY_MAP[weekday.lower()]}")
    parts.extend([
        f"BYHOUR={next_utc.hour}",
        f"BYMINUTE={next_utc.minute}",
        "BYSECOND=0",
    ])
    return ";".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timezone", required=True)
    parser.add_argument("--time", required=True, type=parse_time)
    parser.add_argument("--frequency", choices=["daily", "weekday", "weekly"], required=True)
    parser.add_argument("--weekday", choices=list(WEEKDAY_MAP), help="Required for weekly schedules")
    parser.add_argument("--now-utc", help="ISO datetime for tests, defaults to current UTC")
    args = parser.parse_args()

    tz = ZoneInfo(args.timezone)
    now_utc = (
        datetime.fromisoformat(args.now_utc.replace("Z", "+00:00")).astimezone(timezone.utc)
        if args.now_utc
        else datetime.now(timezone.utc)
    )
    local_next = next_local_run(now_utc, tz, args.time, args.frequency, args.weekday)
    utc_next = local_next.astimezone(timezone.utc)
    rrule = build_rrule(utc_next, args.frequency, args.weekday)
    verified = local_next.hour == args.time.hour and local_next.minute == args.time.minute
    dst_sensitive = observes_dst(tz, local_next.year)

    if args.frequency == "daily":
        frequency_label = "Daily"
    elif args.frequency == "weekday":
        frequency_label = "Every weekday"
    else:
        frequency_label = f"Weekly on {args.weekday.title()}"

    warning = None
    if dst_sensitive:
        warning = "This timezone observes daylight saving. A fixed UTC RRULE may not preserve the local wall-clock time after DST changes."

    print(json.dumps({
        "intent_label": f"{frequency_label} at {args.time.strftime('%H:%M')} {args.timezone}",
        "storage_rrule_utc": rrule,
        "next_run_utc": utc_next.isoformat(),
        "next_run_local": local_next.isoformat(),
        "verified": verified,
        "dst_sensitive": dst_sensitive,
        "warning": warning,
    }, indent=2))


if __name__ == "__main__":
    main()
