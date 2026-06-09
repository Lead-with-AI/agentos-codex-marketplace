---
name: agentos-setup
description: >
  Creates and initializes a brand-NEW AgentOS for a business leader in a fresh empty folder —
  turning it into a working personal operating layer by interviewing the leader, researching their
  company, and creating their AgentOS files. This is the skill for bringing an AgentOS into
  existence for the first time. Triggered by "set up my AgentOS", "set up the AgentOS", "start up
  my AgentOS", "start my AgentOS", "create my AgentOS", "create the AgentOS", "initialize my
  AgentOS", "get my AgentOS started", or "get started with AgentOS". In Codex, the leader may
  invoke this skill explicitly from the skill picker or by asking in plain language.
  Any phrasing about setting up, creating, initializing, or starting an AgentOS that does not yet
  exist belongs here — not the load skill. Runs ONLY once; it refuses and redirects if an AgentOS
  already exists, if it is inside an agent folder, or anywhere under an existing AgentOS. Do NOT
  use this for an agent (e.g. "set up my chief of staff") — that is create-agent or load.
version: 0.1.0
---

# AgentOS Setup

Initialize a new AgentOS in the current working folder. This runs **once** per AgentOS. It conducts a short interview, researches the leader's organization, and writes the AgentOS files.

**Who you're talking to.** Your audience is high-functioning, highly successful, non-technical executives and leaders. They are sharp and capable, but file systems, folders, and technical terms create friction for them. Speak in plain language. Explain what to do, not how it works under the hood. Never use jargon or show file names, paths, or tool names. Never talk down to them. When something goes wrong, keep your wording simplest of all — a confused leader needs the clearest possible next step, not more detail. This skill body is for you, the executing agent — not for the leader to read.

## Executive Output Contract

Final user-facing output must be short, plain, and useful to a non-technical leader.

- For success, use one to three short sentences.
- Include only what was completed, what it now lets the leader do, and the next useful prompt or Codex UI step.
- Do not mention `.codex`, `memory.md`, `MemoryMD`, internal automation folders, local file paths, manifests, plugin roots, command output, connector implementation details, stack traces, or hidden logs.
- Translate technical failures into plain next steps. For example, say "Calendar access needs to be reconnected" rather than naming connector scope errors.
- Keep technical detail in internal logs or files. Do not expose it in the final response unless the leader explicitly asks.

## Operating Constraints

- The working folder is the user's current AgentOS folder. Resolve it as the directory the conversation is operating in (the connected/working folder), not the plugin folder.
- Resolve bundled plugin files relative to this skill's installed plugin root. From this file, the plugin root is two directories up from `skills/setup/SKILL.md`.
- Do not modify bundled plugin files. They are read-only source.
- Create files only. Never overwrite an existing AgentOS file.

## Scripted Interview Rule

Normal Codex mode uses normal chat text for these questions.

The setup interview must be deterministic for cohort testing and training videos. Ask the scripted questions below as normal chat text, one question at a time, and wait for the leader's answer before continuing.

Use the exact question text, option labels, option descriptions, and order below. Do not paraphrase, rename, reorder, merge, omit, or add options unless the leader explicitly asks to answer in their own words.

## Step 1 — Boundary checks: confirm this is a fresh top-level AgentOS root

Setup is **only** ever valid in one situation: a fresh, empty, top-level folder that is about to become a new AgentOS. It must **never** run inside an agent folder, never under an existing AgentOS, and never a second time over a live one. Before doing anything else, run these checks **in order**. Each is non-negotiable — the cost of getting this wrong is building a stray AgentOS inside someone's agent and breaking their setup.

**Check A — Am I inside an agent folder?**
Look at the working folder. If it has its own `AGENTS.md` whose content references parent files with `../` (for example `../USER.md`, `../ORG.md` in its read order / inherited files) — that is the signature of a scoped agent (like a Chief of Staff), not an AgentOS root. **Stop. Do not build anything.** Tell the leader plainly: "It looks like we're inside your [agent name] agent, not a place to set up a new AgentOS. What you want here is to load your AgentOS — say 'load my AgentOS'." Route them to load and end the skill.

**Check B — Does a parent AgentOS already exist one level up?**
Check the parent directory for `../USER.md` and `../ORG.md`. If they exist, this folder is a subfolder *inside* an existing AgentOS — setup must never run here. **Stop.** Tell the leader plainly that their AgentOS already exists one level up, and they should load it ("load my AgentOS") rather than set up a new one. Route to load and end the skill.

**Check C — Does an AgentOS already exist in this folder?**
Check the working folder for `USER.md` and `ORG.md`. If **either** exists, an AgentOS is already here — do not build a fresh one. Ask exactly: "I found an existing AgentOS here. What would you like to do?" Options: (1) "Load it" (route to load), (2) "Upgrade it (recommended)" (hand off to the `agentos-upgrade` skill). End setup after handing off.

**Only if all three checks are clear** — no agent signature, no parent AgentOS, nothing already here — proceed with a fresh build.

A `logs/` folder or a previous setup log does **not** count as an existing AgentOS; only `USER.md`/`ORG.md` (here or one level up), or an agent signature, trip these guards. A leftover log from a failed earlier attempt must not block a legitimate retry.

## Step 1b — Open the setup log

Create (or append to) a setup log at `logs/agentos-cohort3-setup.md` inside the working folder. Create the `logs/` folder if it does not exist.

The purpose of this log is that if setup goes wrong, the leader can find this one file and send it to support, and it will show exactly what happened. Write it so a non-technical person could hand it over and a technical person could diagnose from it.

Rules for the log:

- Record **what happened**, not what the leader said. Log outcomes and events (e.g. "interview completed", "web search found no clear match", "wrote USER.md", "copy of AGENTS.md failed"). Do **not** record the leader's raw interview answers or any personal detail beyond the company name, which is needed to make the log intelligible.
- Start each run with a timestamped header. Get the real timestamp from the system (e.g. `date`), do not invent one.
- Append one short line per step as you complete it, including failures.
- This log writing is for diagnosis only. Never mention the log to the leader during normal (successful) operation, and never expose the file path to them unless they hit a problem and you are directing them to send it to support.

Begin the log now with the run header and a line noting the guard passed and setup is starting.

## Step 2 — Introduce yourself

Greet the leader warmly in two or three sentences. Explain in plain language that you are going to set up their AgentOS — a personal space that remembers who they are, what their company does, and how they like to work, so every future conversation starts with that context. Tell them you will ask a few quick questions, then look up their company, then set everything up. No jargon.

## Step 3 — Interview (one question at a time)

Interview the leader to learn enough about **them** — not just their company — to build a USER.md that genuinely describes the person. Ask **one scripted question at a time**, waiting for each answer. The goal is a USER.md filled with the leader's truth, not template defaults.

### Part A — Identity (plain questions)

Ask these exact questions, in this exact order:

1. "What is your full name?"
2. "What would you like me to call you?"
3. "What is your role and title?"
4. "What is your company name? If there is a company website, include that too."

Do not proceed past Part A until you have at least name, preferred name, role, and company name. Website may be left blank.

### Part B — Background (offer the paste option)

Ask exactly: "If you'd like, paste in a short bio, your LinkedIn summary, or just a few sentences about what you do and what you're responsible for. I'll use it to understand you better. Or say 'skip' and we'll keep it light."

If they paste or describe a background, capture it for the Background section of USER.md. If they skip, that is fine — leave Background brief.

### Part C — How they like to work (scripted choices)

Ask each scripted choice below exactly as written. The leader can answer with the number or label. If they answer in their own words, map it to the closest option and state the mapping briefly before continuing.

Question 1:

```text
How would you like your assistant to interact with you by default?

1. Direct and concise: get to the point and keep the conversation moving.
2. Warm and conversational: human and approachable, while still staying practical.
3. Detailed and thorough: show more reasoning and context by default.
```

Question 2:

```text
How much pushback do you want from your assistant?

1. Challenge me hard: point out weak assumptions, risks, and better alternatives directly.
2. Offer alternatives: suggest a better route when useful, but don't belabor it.
3. Mostly follow my lead: do what I ask unless something is clearly wrong or risky.
```

Question 3:

```text
How long should responses usually be?

1. Short by default: answer quickly and expand only when I ask.
2. Medium with structure: give enough context to be useful, usually with clear bullets.
3. Full detail: include reasoning, context, and tradeoffs by default.
```

Capture each answer for the matching USER.md section (Working Style, Communication Preferences, Collaboration Preferences).

### Part D — Personal non-negotiables (optional)

Ask exactly: "Is there anything you want your assistant to always respect? For example: never schedule before 9am, always use British spelling, or never contact a particular person on your behalf. If not, say 'none'."

Capture any answers for the Non-Negotiables section. If they have none, leave it with a short note that they can add some later. **Do not put agent safety rules here** (those live in the core files); only the leader's personal limits belong in this section.

## Step 4 — Narrate, then research the organization

Tell the leader, in one sentence, that you are now looking up their company online.

Then use Codex web search to research the organization. Search on the company name and, if provided, the website domain. Gather:

- What the company does (two to four sentences of substance)
- Its stated mission or purpose, if public
- Its main products, services, or core work areas
- Who it serves (audience)
- Any stable, public leadership or team context (do not fabricate; only record what you find)

Run multiple searches if needed. Prefer the company's own site and reputable sources. Do not invent facts. If you cannot verify something, leave it out.

## Step 5 — Narrate, then build the files

Tell the leader, in one sentence, that you have what you need and are now setting up their AgentOS.

**Produce clean, professional files — not template scratch.** The templates contain meta-guidance *about* the template that must NOT appear in the leader's live files. When generating `USER.md` and `ORG.md`, strip any template-scaffolding lines, specifically:

- "Use this template by default for root or standalone AgentOS/system scaffolds."
- Any "For scoped agents… create local … only when…" / "Inheritance does not imply a local copy." line.

Keep the file's own one-line purpose note at the top (the "This file describes the user…" / "This file describes the organizational context…" line). Do not add any explanation about where guardrails live, any note about agent behavior rules, or any commentary about what belongs in the file — that is build guidance, not content for the leader's file. The finished files should read as polished, personal documents: a purpose line, then the leader's actual content. No leftover tokens, no scaffolding, no meta-notes.

Create the following in the **working folder**:

### 5a. Copy the templates onto the AgentOS disk (do this first)

Before building any file, copy the plugin's full template set onto the AgentOS so the AgentOS owns its own templates. Create the folder `reference/agentos-templates/` in the working folder, then copy **every** file from the plugin root's `Templates/` folder into it, verbatim.

This is deliberate and important: from this point on, this AgentOS reads its templates from `reference/agentos-templates/` on disk — not from the plugin. Setup itself (the steps below) and every later skill (create-agent, workflow-designer) read templates from this on-disk location. The AgentOS becomes self-contained and its templates can be tuned to the leader over time. The `reference/` folder is also the future home for other reference material (memory, stored documents).

### 5b. USER.md

Read the template at `reference/agentos-templates/USER.template.md` (the on-disk copy you just made) and populate it from the interview answers. Account for **every** section in the template — do not leave any section with its original angle-bracket tokens.

- **Profile** block: set `Name`, `Preferred name`, `Role`, and `Organization` from the interview (Part A). If a `Key collaborators` line has no value, either fill it or remove the line — do not leave its token.
- **Background**: fill from the leader's bio/description (Part B). If they skipped it, keep this brief or note it can be added later.
- **Working Style, Communication Preferences, Collaboration Preferences**: fill from the guided-choice answers (Part C). Write them as concrete statements about how the leader likes to work and be communicated with, derived from what they chose — not generic defaults.
- **Correction Pattern, Voice Preferences**: fill if the interview surfaced anything; otherwise leave a short note that the leader can refine these later. Never leave raw angle-bracket tokens.
- **Non-Negotiables**: fill with the leader's *personal* non-negotiables from Part D (e.g. "never schedule before 9am", "use British spelling"). If they gave none, leave a short note that they can add some later. **Do not write agent safety rules here** — rules like "never invent facts" or "answer questions before acting" are agent guardrails and live in `AGENTS.md`/`PRINCIPLES.md`, which are copied in below. USER.md is about the person only.

The cleaned USER template no longer contains a Prime Directive section. Do not add one — the Prime Directive is an agent guardrail and lives in the core files, not in USER.md.

Write the result to `USER.md` in the working folder.

### 5c. ORG.md

Read the template at `reference/agentos-templates/ORG.template.md` (the on-disk copy) and populate it from the web research. Account for **every** section in the template — do not leave any section with its original angle-bracket tokens.

- **Organization, Mission, Public Offerings Or Core Work, Audience**: fill from research.
- **Internal Systems** and **Leadership Or Team Context**: fill only with what you actually found. If you found nothing for a section, replace its token with a short note such as "None recorded yet — can be added later." Do not fabricate, and do not leave the raw token.
- **Notes**: keep as written in the template.

If web research returned little or nothing useful, build ORG.md from what the leader told you, and add one short line at the bottom of the Notes section stating it was created with limited public information and can be updated later.

Write the result to `ORG.md` in the working folder.

### 5d. Copy the six portable core files

Copy these six files **verbatim** from the plugin root's `core-files/` folder into the working folder, without modification:

- `AGENTS.md`
- `IDENTITY.md`
- `SOUL.md`
- `PRINCIPLES.md`
- `CLAUDE.md`
- `DECISIONS.md`

Use a file copy (e.g. `cp`), not a rewrite, so the content is byte-identical. These files intentionally refer to "the user" rather than a name — they are portable. Do not inject the leader's name or any personalized content into them. The only personalized files are `USER.md` and `ORG.md`.

## Step 6 — Verify

Confirm all eight files now exist in the working folder: `USER.md`, `ORG.md`, `AGENTS.md`, `IDENTITY.md`, `SOUL.md`, `PRINCIPLES.md`, `CLAUDE.md`, `DECISIONS.md`. Also confirm `reference/agentos-templates/` exists and contains the copied template set (it should hold the full set of `*.template.md` files). Confirm `USER.md` and `ORG.md` contain **no** leftover angle-bracket tokens — check for any `<...>` pattern (for example `<Name>`, `<Organization>`, `<Offering Or Work Area 1>`), not only the literal word "placeholder". Any remaining `<...>` token means a section was missed; go back and fill it.

Write the verification result to the setup log: list which of the eight files are present, and the placeholder-check result.

If any file is missing or any copy failed, write the failure to the setup log with the specific step and file that failed, then stop and tell the leader plainly that one step did not complete. Name what is missing in plain language (e.g. "your company profile didn't save"). Mention the setup log only as a support artifact if they need help diagnosing the issue; do not expose the path or technical log detail in normal output. Do not pretend success.

## Step 7 — Confirm completion

Tell the leader, warmly and in plain language, that their AgentOS is set up and ready. Do not list file names. Explain in one or two sentences what they now have: a personal operating layer that knows who they are and what their company does, ready to use in every conversation.

Then tell them the one thing they need to do next: at the start of any new Codex conversation in this folder, say "load my AgentOS" so this context comes with them. Optionally mention they can create their first agent — for example a Chief of Staff — by saying "create a new agent".

## Failure Handling Summary

- AgentOS already exists → stop at Step 1, redirect to load.
- Interview incomplete → keep asking; do not proceed without the required answers.
- Web research empty → build ORG.md from interview answers, note limited information.
- File copy or write fails → record it in `logs/agentos-cohort3-setup.md`, stop, report plainly which part failed, mention the setup log only as a support artifact if needed, never claim false success.

Every run, success or failure, must leave a coherent setup log in the AgentOS folder. The log is the leader's evidence to hand to support and the diagnostic record we read together.
