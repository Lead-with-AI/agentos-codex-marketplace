---
name: daily-briefing
description: >
  Produces a short, triage-first daily briefing for the leader from their calendar and email.
  Surfaces what matters today — key meetings, decisions needed, and time-sensitive items — as a
  concise written brief in the leader's voice. Use whenever the leader asks for their daily
  briefing, morning brief, or what's on today: "give me my daily briefing", "run my morning
  brief", "what's on today", "brief me", "what do I need to know this morning", or "start my day".
version: 1.0.0
---

# Daily Briefing

Produce a short written daily briefing for the leader. This is an executive brief, not a data dump: lead with what matters, triage hard, and keep it to roughly one screen. A busy leader should get the whole picture in under a minute.

Read the agent's context first if not already loaded: `AGENTS.md`, `IDENTITY.md`, `SOUL.md`, `../USER.md` (voice and preferences), `../ORG.md`. Write the brief in the leader's voice and respect their non-negotiables.

## What to gather

Use only the connectors this agent has. For a standard Chief of Staff that is **calendar** and **email**.

1. **Today's calendar** — meetings and commitments for today, in time order. Note anything that needs preparation, a decision, or an attendee the leader should be briefed on.
2. **Email that matters** — scan recent unread and important email. Pull only what is genuinely time-sensitive or decision-bearing. Ignore newsletters, noise, and FYI threads unless they bear on today.

Do not fabricate. If a connector isn't available or returns nothing, say so plainly rather than inventing items.

## How to write it

Use the daily-briefing template in this workflow folder (`template.md`) as the structure. Fill it from what you gathered. Keep the briefing tight:

- **Front-load the critical items.** Anything needing a decision or a response today goes at the very top.
- Triage. Three sharp items beat fifteen exhaustive ones.
- Use absolute dates and times. No "later this week."
- Plain, direct language in the leader's voice. No filler, no preamble.
- If there is genuinely nothing critical, say so in one line — a calm day is useful signal too.

## Deliver

Hand the leader the finished brief only. If a connector is unavailable or empty, include at most one short plain-language note that affects the brief, such as "I could not access your calendar today, so this brief is based on email only." Do not mention run logs, memory files, hidden runtime state, local paths, connector internals, command output, or implementation details.

Do not send it anywhere or take any action on the items without the leader's explicit approval — this agent drafts and prepares; the leader decides.
