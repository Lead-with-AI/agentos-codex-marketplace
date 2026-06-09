---
name: agentos-load
description: >
  Loads an AgentOS that ALREADY EXISTS into the current conversation, so the assistant remembers
  who the leader is, what their company does, how they work, and which agents they have. Use only
  when an AgentOS has already been set up and the leader wants its context in this conversation.
  Reads the context files and any agent folders, then gives a short briefing; changes no files.
  Triggered by "load my AgentOS", "load my AgentOS into this conversation", "load my context",
  "resume my AgentOS", or "pick up where we left off". In Codex, the leader may invoke this skill
  explicitly from the skill picker or by asking in plain language. This is NOT for
  creating or initializing a new AgentOS — if the leader wants to set up, create, initialize, or
  start a brand-new AgentOS, that is the setup skill, not this one.
version: 0.1.0
---

# AgentOS Load

Load an existing AgentOS into the current conversation. This runs at the start of **every** new conversation, because a fresh conversation does not reliably read the AgentOS files on its own. This is how the leader's context comes with them.

**Who you're talking to.** Your audience is high-functioning, highly successful, non-technical executives and leaders. They are sharp and capable, but file systems, folders, and technical terms create friction for them. Speak in plain language. Explain what to do, not how it works under the hood. Never use jargon or show file names, paths, or tool names. Never talk down to them. When something goes wrong, keep your wording simplest of all — a confused leader needs the clearest possible next step, not more detail. This skill body is for you, the executing agent — not for the leader to read.

This skill is **read-only**. It loads and reads context. It must not create, edit, move, or delete any file. The only thing it produces is the spoken briefing to the leader.

## Codex Popup-Input Rule

When this skill needs the leader to choose between options, call Codex's structured popup input tool, `request_user_input`, when it is available in the Codex app. Do not print the question and options as normal chat text when the popup tool is available.

Use conversational text only if the structured popup input tool is not available in the current Codex mode.

## Step 1 — Work out where you are: the AgentOS root, or an agent folder

Check the working folder for `AGENTS.md`, then determine which kind of folder this is.

**Case A — the AgentOS root.** `USER.md`, `ORG.md`, and `AGENTS.md` are all present in the working folder. This is the main AgentOS. Continue to Step 2 and load normally.

**Case B — an agent folder.** The folder has its own `AGENTS.md` but `USER.md` / `ORG.md` are **not** here — instead, the agent's `AGENTS.md` references them one level up (e.g. `../USER.md`). This is a scoped agent (like a Chief of Staff). The leader is working inside the agent's folder. To inherit their context, Codex must be able to read the parent AgentOS folder.

  - Try to read the parent files the agent references (`../USER.md`, `../ORG.md`, `../PRINCIPLES.md`).
  - **If you can read them**, good — Codex can see the parent AgentOS folder. Load the agent's own files plus the inherited parent files, and brief normally as that agent.
  - **If you cannot read them**, do **not** fail silently or guess. Load what you can from the agent folder, then tell the leader plainly: their agent can't see their main AgentOS. Give them the Codex fix in plain language: open the top-level AgentOS folder as the Codex project, or grant Codex access to that parent folder using the app's normal project/folder access flow, then say "load my agent" again. Then wait.

**Case C — neither.** No `AGENTS.md`, no `USER.md`/`ORG.md`. This folder has not been set up — it's empty. The leader almost certainly wants to **create** their AgentOS (they likely said something like "start my AgentOS" in a new empty folder, meaning "set it up"). Do not just point them elsewhere and leave them stuck. Call `request_user_input` with this question: "There's no AgentOS in this folder yet. Would you like to set one up now?" Options: "Set it up now" / "Not right now". If yes, hand off to the setup skill and run it. If no, stop. End this skill either way.

## Step 2 — Read the core context, silently

Read these files from the working folder, in this order. Do not narrate this to the leader — no "reading file X" messages. Just load them.

1. `AGENTS.md` — the canonical instructions; the operating rules you will follow for the rest of this conversation
2. `IDENTITY.md` — what this AgentOS is
3. `SOUL.md` — how to communicate; temperament and modes
4. `USER.md` — who the leader is, how they work, their preferences and non-negotiables
5. `ORG.md` — the organization context
6. `PRINCIPLES.md` — operating principles
7. `CLAUDE.md` — the loader pointer (read it, but `AGENTS.md` is the substantive instruction file)

Then read conditional files only if present and relevant: `DECISIONS.md` (durable decisions), and any `BRAND.md` or `DESIGN.md`.

`AGENTS.md` is canonical. For the rest of this conversation, operate according to `AGENTS.md`, `PRINCIPLES.md`, `SOUL.md`, and `USER.md`. If any files conflict, surface the conflict to the leader rather than guessing.

## Step 3 — Discover scoped agents

Look for agent subfolders inside the working folder. An agent subfolder is any directory that contains its own `AGENTS.md` (for example a `chief-of-staff/` folder).

For each agent folder found, read its `AGENTS.md` and `IDENTITY.md` so you know what that agent is for and how it behaves. Note its name (from the folder name and its files) so you can mention it in the briefing.

If there are no agent subfolders, that is normal for a new AgentOS — the leader simply has not created any agents yet.

## Step 4 — Brief the leader

Greet the leader by their preferred name (from `USER.md`). Keep it warm and brief.

Then give a short plain-language briefing — two to four short paragraphs, no bullet points, no file names, no jargon. Cover:

- That their AgentOS is loaded and you now have their context for this conversation.
- A one-line reminder of what this AgentOS is for, grounded in what you read (their role and organization), so it feels personal rather than generic.
- Which agents they have available, if any, and what each is for in one short phrase. If they have none, briefly mention they can create one (for example a Chief of Staff) by saying "create a new agent".

End by asking what they would like to work on, then stop and wait. Do not start doing work until the leader tells you what they want.

## Step 5 — Operate as the AgentOS for the rest of the conversation

After the briefing, you are operating inside this AgentOS. Follow `AGENTS.md` and `PRINCIPLES.md`: lead with the answer, treat questions as questions (not as permission to take action), verify before asserting, and keep the leader's preferences from `USER.md` in force. If the leader asks to work with a specific agent, switch to operating under that agent's files.

## Failure Handling Summary

- No AgentOS in the folder → stop, tell the leader to run setup, do not fabricate context.
- A core file is missing or unreadable → load what you can, then tell the leader plainly that part of their context could not be loaded and that re-running setup or contacting support may be needed. Do not silently proceed as if everything loaded.
- Files conflict → surface the conflict; do not silently pick one.
- Never write anything in this skill. It is read-only by design.
