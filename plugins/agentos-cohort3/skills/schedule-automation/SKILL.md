---
name: agentos-schedule-automation
description: >
  Creates, updates, or verifies AgentOS/Codex automations with timezone-safe scheduling.
  Use when a leader asks to schedule a workflow or routine, set a daily or weekly automation,
  run something every weekday morning, or fix an automation time. Verifies the computed next run
  against the leader's intended local wall-clock time before saying the automation is scheduled.
version: 1.0.0
---

# AgentOS Schedule Automation

Create, update, or verify a Codex automation for an AgentOS workflow. This skill exists because a simple "schedule this at 7:00 a.m." can be wrong if Codex stores the schedule hour in UTC while the leader means local time.

**Who you're talking to.** Your audience is high-functioning, highly successful, non-technical executives and leaders. Speak plainly. The leader cares that the routine runs at the right local time, not how the automation record is stored.

## Executive Output Contract

Final user-facing output must be short, plain, and useful.

- Say "scheduled" only after the next run is verified against the intended local time.
- Give the verified local next run: date, time, and timezone.
- Do not show raw RRULEs, file paths, automation records, command output, UTC math, or implementation details unless the leader asks.
- If Codex stores a UTC workaround, explain it in one plain sentence only when needed.
- If verification fails, say the automation was created or updated but is not verified.

## Step 1 — Resolve The Intended Timezone

Resolve timezone in this order:

1. Explicit timezone in the leader's request, e.g. "7am Singapore time".
2. Current thread or environment timezone, if available.
3. User profile or location timezone, if already loaded.
4. Local machine timezone.
5. If still unclear, ask exactly: "What timezone should this run in?"

Represent the schedule intent in plain language before creating anything, for example:

```text
Daily at 7:00 a.m. Asia/Ho_Chi_Minh.
```

If the leader corrects the timezone or time, update the intent before continuing.

## Step 2 — Build The Schedule Safely

Use the helper script in this skill when converting local time to a storage schedule:

```bash
python3 skills/schedule-automation/scripts/schedule_helper.py \
  --timezone Asia/Ho_Chi_Minh \
  --time 07:00 \
  --frequency daily
```

Run it from the plugin root or pass the script path explicitly. The helper returns JSON with:

- `intent_label`
- `storage_rrule_utc`
- `next_run_utc`
- `next_run_local`
- `verified`
- `dst_sensitive`
- `warning`

If Codex supports timezone-aware schedules in the current environment, use the timezone-aware schedule and still verify the computed next run.

If Codex does not support timezone-aware schedules and stores RRULE hours as UTC, prefer the actual verified next run over a pretty repeat label. For example, 7:00 a.m. Asia/Ho_Chi_Minh stores as midnight UTC.

If the timezone observes daylight saving and Codex only supports fixed UTC RRULEs, do not promise permanent wall-clock accuracy across DST changes. Tell the leader plainly that this schedule needs a timezone-aware automation or future DST check.

## Step 3 — Create Or Update The Automation

Create or update the Codex automation only after the schedule intent is clear.

The automation prompt must be self-contained. It must say:

- which agent is operating
- which workflow is running
- which sources/connectors it may use
- what output to produce
- that final output must avoid hidden runtime details, local paths, run logs, connector internals, command output, and implementation detail

Do not claim success immediately after creation. Continue to verification.

## Step 4 — Verify The Stored Result

After creating or updating the automation:

1. Inspect the automation record.
2. Inspect the computed next run if Codex exposes it.
3. Convert the next run into the intended timezone.
4. Compare the local wall-clock time against the leader's requested time.

Only say "scheduled" when the verified next run matches the intended local wall-clock time.

If the displayed repeat label and the actual next run disagree:

- prioritize the actual next run
- say the display is inconsistent
- do not treat the schedule as verified unless the actual next run is correct

If the actual next run is unavailable, say the automation was created but the schedule could not be verified in this environment.

## Step 5 — Final Response

Use one of these patterns.

Verified:

```text
Your daily brief is scheduled for 7:00 a.m. Vietnam time. I verified the next run is Wednesday, 10 June 2026 at 7:00 a.m.
```

Verified with UTC workaround:

```text
Your daily brief is scheduled for 7:00 a.m. Vietnam time. Codex stores this internally as midnight UTC, which maps to 7:00 a.m. Vietnam time, and I verified the next run.
```

Not verified:

```text
The automation was created, but I could not verify that it will run at 7:00 a.m. Vietnam time. Please check it in Codex Automations before relying on it.
```

Display conflict:

```text
The automation was created, but the schedule display is inconsistent. The actual next run is Wednesday, 10 June 2026 at 7:00 a.m. Vietnam time, so I am not treating this as fully verified yet.
```

## Failure Handling

- Timezone unclear -> ask the timezone question and wait.
- Helper cannot compute the schedule -> do not create the automation; explain that the schedule could not be prepared.
- Automation creation unavailable -> tell the leader it was not created and point them to Codex Automations.
- Next run cannot be inspected -> do not claim verified scheduling.
- DST-sensitive fixed UTC schedule -> warn that the local time may shift when daylight saving changes.
