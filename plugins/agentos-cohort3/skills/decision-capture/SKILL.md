---
name: agentos-decision
description: >
  Saves an important decision into the leader's AgentOS so it is remembered for good — recorded
  in a portable DECISIONS.md file that travels with them to any tool, not just this conversation.
  Appends the decision in the file's standard format and can mirror it into memory. Triggered by
  "remember this decision", "log this decision", "save this for later", "make a note of this
  decision", or "record that we decided...". In Codex, the leader may invoke this skill explicitly
  from the skill picker or by asking in plain language.
version: 0.1.0
---

# AgentOS Capture Decision

Record a durable decision into the leader's AgentOS. The decision is written to `DECISIONS.md` — a plain file the leader owns that travels with their AgentOS to any tool that reads it. This is the point of the skill: it shows the leader that they have persistent memory outside any single product.

**Who you're talking to.** Your audience is high-functioning, highly successful, non-technical executives and leaders. They are sharp and capable, but file systems, folders, and technical terms create friction for them. Speak in plain language. Explain what to do, not how it works under the hood. Never use jargon or show file names, paths, or tool names. Never talk down to them. When something goes wrong, keep your wording simplest of all — a confused leader needs the clearest possible next step, not more detail. This skill body is for you, the executing agent — not for the leader to read.

## Step 1 — Confirm an AgentOS exists

Check the working folder for `DECISIONS.md` (and `AGENTS.md` to confirm this is an AgentOS).

- If there is no AgentOS here, stop and tell the leader plainly that they need to set up their AgentOS first by saying "set up my AgentOS". End the skill.
- If `AGENTS.md` exists but `DECISIONS.md` does not, create `DECISIONS.md` with the standard header and format block (see the format below) before appending. This should be rare, since setup creates it.

## Step 2 — Identify the decision

Determine the decision to record. It usually comes from the immediately preceding conversation — the thing the leader just said to remember, or a choice you and the leader just settled.

If the decision is clear from context, restate it back to the leader in one plain sentence and confirm you have it right before writing. If it is ambiguous (you are not sure which of several things they mean), ask one short clarifying question. Do not record a vague or half-understood decision — a wrong durable record is worse than none.

Capture three things:

- **Decision** — what was decided, in plain, specific language.
- **Reason** — why, if the leader gave one or it is clear from context. If not stated, keep it brief or omit rather than inventing motivation.
- **Implication** — what should happen or be true going forward because of this decision, if applicable.

## Step 3 — Append to DECISIONS.md in the existing format

Get today's real date from the system (e.g. `date +%Y-%m-%d`). Do not guess the date.

Append a new entry to the **end** of `DECISIONS.md`, matching the file's existing format exactly:

```markdown
## YYYY-MM-DD — Decision title

Decision:

<what was decided>

Reason:

<why, or omit this block's content if not known — do not fabricate>

Implication:

<what should happen going forward, or leave brief if not applicable>
```

Rules:

- **Append only.** Never overwrite, reorder, or alter existing decision entries. This file is the leader's durable record; existing entries are sacrosanct.
- Match the heading style already in the file (`## YYYY-MM-DD — Title` with an em dash). Look at the existing entries and follow their exact pattern.
- Keep the title short and specific.
- Write a real, specific Decision. Only include Reason/Implication content you actually have; do not invent reasoning to fill the template.

## Step 4 — Optional memory mirror

If a session memory system is available in this environment, also write a short pointer to the decision there, so it is recalled in future sessions even before the leader loads their AgentOS. This is a convenience mirror, not the source of truth.

The **source of truth is `DECISIONS.md`** — the portable file. The memory mirror is secondary and tool-specific. If no memory system is available, skip this step silently; it is not a failure.

Do not mirror sensitive personal information into memory. Record the decision, not private detail.

## Step 5 — Confirm

Tell the leader, in one or two plain sentences, that you have saved the decision. Reinforce the durable, portable nature in plain language — for example, that it is now part of their AgentOS and will be remembered going forward, and travels with them. Do not show the file name unless they ask where it lives.

## Failure Handling Summary

- No AgentOS in the folder → stop, redirect to setup.
- Ambiguous decision → ask one clarifying question; do not record a guess.
- Writing to `DECISIONS.md` fails → tell the leader plainly it could not be saved; do not claim it was.
- Never overwrite existing decision entries. Append only.
- Never fabricate a Reason or Implication to fill the template.
