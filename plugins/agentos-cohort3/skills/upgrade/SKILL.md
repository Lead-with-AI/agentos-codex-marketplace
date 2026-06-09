---
name: agentos-upgrade
description: >
  Migrates an existing, hand-built AgentOS to the current standard structure while keeping the
  leader's own work. Analyzes each existing file, extracts what is worthwhile, backs everything
  up first, and rewrites the files to the standard structure in place. Triggered by "upgrade my
  AgentOS", "migrate my AgentOS", "check my AgentOS", "enhance my existing AgentOS", or when
  setup detects an AgentOS already exists and the leader chooses to migrate rather than rebuild.
version: 1.0.0
---

# AgentOS Upgrade (Migrate In Place)

Take an AgentOS the leader built earlier — often by hand, from a questionnaire, with mixed results — and bring it up to the current standard **without throwing away the genuine thinking they put in**. This is the payoff to a teaching arc: they tried, hit the holes, and now this brings their work up to a clean, working standard while preserving everything valuable.

**Who you're talking to.** Your audience is high-functioning, highly successful, non-technical executives and leaders. They are sharp and capable, but file systems, folders, and technical terms create friction for them. Speak in plain language. Explain what to do, not how it works under the hood. Never use jargon or show file names, paths, or tool names. Never talk down to them. When something goes wrong, keep your wording simplest of all — a confused leader needs the clearest possible next step, not more detail. This skill body is for you, the executing agent — not for the leader to read.

## Executive Output Contract

Final user-facing output must be short, plain, and useful to a non-technical leader.

- For success, use one to three short sentences.
- Include only what was upgraded, what was preserved, and the next useful prompt.
- Do not mention `.codex`, `memory.md`, `MemoryMD`, internal automation folders, local file paths, manifests, plugin roots, command output, connector implementation details, stack traces, or hidden logs.
- Translate technical failures into plain next steps. For example, say "Calendar access needs to be reconnected" rather than naming connector scope errors.
- Keep technical detail in internal logs or files. Do not expose it in the final response unless the leader explicitly asks.

Normal Codex mode uses normal chat text for these questions. Ask each choice as a scripted text question with the exact options below, then wait for the leader's answer.

The guiding principle: **extract and carry forward what is worthwhile; standardize the structure; never silently discard the leader's substance.** Back up everything before changing anything.

## Step 1 — Confirm there is an AgentOS to migrate

Confirm the working folder has an existing AgentOS (at least `USER.md`/`ORG.md` or `AGENTS.md`). If it's empty, this is not a migration — tell the leader to run setup for a clean build, and stop.

## Step 2 — First choice: migrate or clean rebuild (explain both upfront)

Before the choice, explain both options plainly so the leader understands what each one does — not just labels. Say something like: "I found an existing AgentOS here. There are two ways forward, and I want you to understand both before you choose."

Then present them clearly:

1. **Migrate it (recommended)** — "I'll keep all of your work. First I make a full backup of your current files, then I bring them up to the standard structure so everything works cleanly going forward. Nothing you wrote is lost."
2. **Stop and do a clean rebuild instead** — "We leave this as-is and start fresh in a new folder, where I'll walk you through creating everything from scratch. Your current work here stays untouched, but the new AgentOS won't carry it over."

Then ask exactly: "Which would you like?" Options: "Migrate (recommended)" / "Stop".

If they choose clean rebuild, stop this skill. Tell them to open a fresh, empty folder and run setup there for a clean build. Do not migrate and do not change anything here.

## Step 3 — Explain, then second choice (a real back-out)

If they chose migrate, explain plainly what will happen: "I'll keep all of your work. First I'll make a complete backup of your current AgentOS, then I'll go through each file, keep what's worth keeping, and rewrite everything into the standard structure so it works cleanly going forward. Your originals are saved and nothing is lost."

Then ask exactly: "Ready to go ahead?" Options: "Yes, migrate it" / "No, not now". If no, stop and change nothing. This is their second chance to back out before anything is touched.

## Step 4 — Full backup first (before any change)

Before modifying a single file, create a complete backup of the AgentOS.

**Zip to `/tmp` first, then copy into the AgentOS — do not zip directly into the AgentOS folder.** On some mounts, writing the zip directly to a path inside the working folder fails silently: the tool pre-creates a zero-byte placeholder it cannot then replace, leaving an empty file that *looks* like a backup but is not. That would be catastrophic here — the skill might think it backed up and then overwrite the leader's files with nothing saved. So:

```
TS=$(date +%Y%m%d-%H%M%S)
cd <AgentOS root> && zip -r "/tmp/agentos-backup-$TS.zip" . -x "backup/*"
mkdir -p "<AgentOS root>/backup"
cp "/tmp/agentos-backup-$TS.zip" "<AgentOS root>/backup/agentos-backup-$TS.zip"
```

**Verify the backup for real before proceeding** — do not just check that a filename exists:

- Confirm the copied `backup/agentos-backup-$TS.zip` is **non-zero in size**.
- Confirm it actually contains the AgentOS files — list the archive (`unzip -l`) and check the expected files are inside (USER.md, ORG.md, the rest, and any agent folders).

If the backup is missing, zero bytes, or does not contain the expected files, **stop immediately** — do not change anything. Tell the leader plainly that the backup didn't complete, so you won't risk their files. Per the no-loss rule, never change a single file without a verified, non-empty backup in hand.

## Step 5 — Ensure the on-disk template set exists

If `reference/agentos-templates/` does not exist (likely for a hand-built AgentOS), create it and copy the full template set from the plugin root's `Templates/` folder into it. This is the standard each migrated file is brought up to, and the source future agents build from. This is the one place outside clean setup where templates are copied from the plugin.

## Step 6 — Analyze and migrate each file (extract what's worthwhile)

Go through the AgentOS files one at a time. For **each** file, this is an analysis-and-merge task, not a mechanical replace: read what the leader wrote, read the current standard template, judge what in their version is genuinely worthwhile, and write a **new standard-structured file in place that keeps their worthwhile content** and drops only noise, broken structure, or leftover questionnaire scaffolding.

Apply this judgement per file:

- **USER.md** — heavily personal (who they are, how they work). Keep all real content; bring the structure to the current standard; strip any template-scaffolding or guardrail cruft. Do not add agent rules here.
- **ORG.md** — personal to their company. Keep all real content; standardize structure.
- **SOUL.md** — the AgentOS's personality, often deliberately tuned by the leader. Keep their voice and tuning; standardize the structure (Temperament / Interaction Style / Communication Modes etc.).
- **IDENTITY.md** — describes what the AgentOS *is*; this is where leaders most often experimented. Bring it to the standard IDENTITY, but first **mine their version for anything genuinely useful** and fold that in rather than discarding it. If they wrote something worthwhile, it survives into the new file.
- **AGENTS.md** — the canonical instruction file; leaders were not meant to change it. Bring to current standard. If they did change it, note what they changed in the migration summary (it's preserved in the backup regardless).
- **PRINCIPLES.md** — operating principles are the system's, not personal taste. Bring to current standard.
- **CLAUDE.md** — the loader; one correct shape. Bring to the standard loader.
- **DECISIONS.md** — **the decision entries are sacrosanct: preserve every entry exactly, byte-for-byte.** You may bring the file's title and format/header block up to the standard *around* the entries (e.g. fix the title, add the format guidance block) — but never alter, reword, reorder, or drop a single existing decision entry. If you are unsure whether something is header vs. an entry, leave it alone. The entries are the one thing in the whole AgentOS that must never change.

Write each new file in place. The backup holds every original, so nothing is lost even where you standardized.

## Step 7 — Preserve agents

Do not rewrite existing agent subfolders. Leave each agent's files as they are. (A later pass can offer to migrate individual agents, but this skill focuses on the AgentOS root.) Note in the summary which agents were found and left intact.

## Step 8 — Bring the on-disk templates into line with the migrated files (mandatory)

This step is **not optional** and is part of migration. The whole AgentOS must be internally consistent: the on-disk templates in `reference/agentos-templates/` must reflect the same standards as the migrated root files, so that any agent created later (from those templates) inherits the *same* principles, personality, and identity standards the leader actually has at the root. If the templates and the root files disagree, a new Chief of Staff would be built with different principles than the leader's own AgentOS — which is incoherent and must not happen.

So after migrating the root files, update the on-disk templates to match:

- **SOUL.template.md** — reflect the leader's established personality/temperament and interaction style (their tuning), so future agents start from the leader's voice, not the generic one.
- **PRINCIPLES.template.md** — reflect the leader's operating principles as migrated, so every agent inherits the same principles the root holds. The root `PRINCIPLES.md` and the principles template must not diverge.
- **IDENTITY.template.md** — reflect any worthwhile identity standard carried forward.

Carry over **preferences, principles, and structure** — the things future agents *should* inherit. Do **not** put personal *facts* into templates (no bios, no names, no company specifics) — an agent is not the person. The test: after this step, the templates and the root files express the same standards, and building an agent from the templates would not contradict the leader's own AgentOS.

## Step 9 — Verify

Confirm the standard files are present and well-formed (no leftover `<...>` tokens in USER/ORG/SOUL/IDENTITY), `reference/agentos-templates/` exists, the backup zip exists, DECISIONS entries are intact, and the templates are now consistent with the migrated root files (no divergence in principles or standards). If anything is wrong, tell the leader plainly and point them to the backup; do not claim success.

## Step 10 — Summarize

Tell the leader plainly what happened: their AgentOS was backed up, migrated to the standard structure with their work kept, and their templates updated so future agents inherit their established principles and style. Briefly note, in plain language, what was kept from their files and what was standardized — no file dumps, file paths, command output, or backup implementation details.

## Failure Handling Summary

- Empty folder → not a migration; send to setup.
- Either back-out choice → stop, change nothing.
- Backup fails → stop before any file change; never migrate without a successful backup.
- Per-file analysis → extract worthwhile content; discard only noise/scaffolding; never silently lose the leader's substance.
- DECISIONS entries and existing agents → preserved, never rewritten.
