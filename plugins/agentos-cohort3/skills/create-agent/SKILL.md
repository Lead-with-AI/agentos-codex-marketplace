---
name: agentos-create-agent
description: >
  Creates a new agent inside a leader's AgentOS — a dedicated helper such as a Chief of Staff,
  research assistant, or content agent. Proposes a role definition tailored to the leader's
  context, confirms it through guided Codex input, then scaffolds the agent's folder.
  Triggered by "create a new agent", "add an agent", "build me an agent", "I want a chief of
  staff", or "set up an assistant for X". In Codex, the leader may invoke this skill explicitly
  from the skill picker or by asking in plain language. Use whenever the
  leader wants to create, add, or build a new agent and an AgentOS already exists.
version: 0.1.0
---

# AgentOS Create Agent

Create a new scoped agent inside the leader's existing AgentOS. The agent lives in its own subfolder and inherits the AgentOS's root context while defining its own role, scope, and behavior.

**Who you're talking to.** Your audience is high-functioning, highly successful, non-technical executives and leaders. They are sharp and capable, but file systems, folders, and technical terms create friction for them. Speak in plain language. Explain what to do, not how it works under the hood. Never use jargon or show file names, paths, or tool names. Never talk down to them. When something goes wrong, keep your wording simplest of all — a confused leader needs the clearest possible next step, not more detail. This skill body is for you, the executing agent — not for the leader to read.

## Step 1 — Confirm an AgentOS exists

Check the working folder for `USER.md`, `ORG.md`, and `AGENTS.md`.

- If any are missing, there is no AgentOS here to add an agent to. Stop. Tell the leader plainly that they need to set up their AgentOS first by saying "set up my AgentOS". End the skill.
- If present, continue.

## Step 2 — Load personalization and the quality reference

Read, silently:

- `USER.md` and `ORG.md` from the working folder — so the new agent is personalized to the leader and their organization.
- The bundled reference agent at the plugin root's `reference-agents/chief-of-staff/` folder (its `AGENTS.md`, `IDENTITY.md`, `SOUL.md`) — this is the **quality bar only**. It is a generic example, written about an unnamed example leader, not about the actual leader you are serving. Study it for its level of specificity, clear ownership boundaries, and approval discipline — then build a fresh agent personalized to *this* leader from `USER.md`/`ORG.md` and the interview.

  Do not treat the reference as already fitting the leader. Even if the leader's role resembles the example, the reference is not their agent — it is a template-quality example. Never say or imply "this reference already fits you, so I'll just use it." Always build the agent from the interview answers and the leader's own context. Reuse the reference's *structure and standard*, never its example content as if it were the leader's.

## Interview Rule — Use Codex Popup Input For Every Question

This is critical and overrides any default conversational habit. **Every question you put to the leader in this skill must call Codex's structured popup input tool, `request_user_input`, when it is available in the Codex app, with concrete options.** Do not print the question and options as normal chat text when the popup tool is available. Do not redesign the interview sequence. Do not drop into open-ended free-text mode unless the step explicitly offers a "let me describe it" / "let me write my own" path.

Free-text entry is allowed **only** when it is presented as one of the offered choices (for example a "Let me write my own" option). It is never the default or the fallback. If a choice needs refinement, present the refinement as another guided Codex choice, not an open prompt.

If the Codex app exposes native multi-select popup input, use it for questions that say multi-select. If only single-choice popup input is available, use the popup anyway and include an "Other / choose several" path, then ask one short follow-up only when needed.

If structured popup input is not available in the current Codex mode, ask the same guided question conversationally with the same concrete options and wait for the leader's answer before continuing.

## Step 3 — Suggest a Chief of Staff only if they have no agents yet

Check whether any agent subfolders already exist (directories containing their own `AGENTS.md`).

- If **none exist yet**, this is their first agent. Use guided Codex input: "Would you like to start with a Chief of Staff? It's the most useful first agent for most leaders." Options: (1) "Yes, set up a Chief of Staff", (2) "No, a different kind of agent". 
- If agents **already exist**, do **not** pitch the Chief of Staff again. Use guided Codex input: "What kind of agent would you like to add?" with a short open-ended set plus a "Let me describe it" option. Never repeat a stale Chief-of-Staff suggestion to a leader who already has one.

If they choose a different kind of agent, get its name via guided Codex input (offer a few common types plus "Let me name it"), then adapt the role-definition step below to that agent type.

## Step 4 — Define what the agent IS (propose a role, confirm by pop-up)

You are defining **what the agent is** — its role and identity — not what it does. Do **not** ask the leader to list tasks, workflows, or a daily routine. Workflows and skills come later, separately. This step settles the agent's role description only.

### 4a. Propose a tailored role definition

Using the leader's role, company, and background from `USER.md` and `ORG.md`, write a concise, JD-style **role description** for this agent — an executive briefing of what the role is, in the context of who they are and what their business does. Aim for one solid short paragraph (a real description, not a stripped "ABC" line, and not pages). For a Chief of Staff, base it on the established definition of the role: the person who sits between the leader and everything else — managing the flow of information, protecting the leader's time and focus, ensuring decisions get made and followed through, preparing the leader for what's coming, and handling the coordination work that would otherwise land on the leader's desk — tailored to this leader and organization.

Output that definition to the leader as a short context block they can read (not as a question).

### 4b. Confirm it with a pop-up

Immediately follow the definition with guided Codex input:

- **Question text:** "Does this role definition fit for you?"
- **Options:**
  1. "Yes, accept this definition"
  2. "Let me write my own — I'll describe my ideal Chief of Staff in a few sentences" (this is the offered free-text path; when chosen, invite 3–4 sentences and build from what they write)

If they accept, use your proposed definition. If they choose to write their own, use theirs. Either way, the result is the agent's role definition.

State plainly, in one short line, that at this point you are defining the role — not yet what the agent does — and that workflows come later.

### 4c. Tools (pop-up, multi-select)

Use Codex guided input for source-system selection: "What should this agent be able to see?" Offer these as separate, individually selectable options — not bundled combinations:

- Email
- Calendar
- Slack
- CRM
- Other

If the Codex guided-input UI supports selecting more than one option, allow multiple selections. If the current Codex UI only supports a single choice, present the same list as a checklist and ask the leader to choose all that apply in one answer. If they choose "Other", let them name it. Do not bundle options into either/or combos, and do not recite the leader's specific connected tools back to them. Note that the agent drafts and prepares but does not send or change anything without approval.

Do not proceed without at least the agent name and an accepted role definition.

## Step 5 — Narrate, then build the agent

Tell the leader, in one sentence, that you have what you need and are now creating their [agent name] agent.

### 5a. Determine the folder name

Convert the agent name to a folder slug: lowercase, words separated by hyphens, no spaces or special characters (e.g. "Chief of Staff" becomes `chief-of-staff`).

Check whether a folder with that slug already exists in the working folder.

- If it exists, do **not** overwrite it. Ask the leader whether they want to update that existing agent or create a different one. Act on their answer. Do not silently replace a working agent.
- If it does not exist, create the subfolder.

### 5b. Create the agent files

Inside the new subfolder, create these five files. Populate them from the leader's **on-disk AgentOS templates** and the interview answers, using the Chief of Staff reference as the quality bar. Remove all angle-bracket tokens — no `<...>` may remain in the finished files.

**Where the templates come from.** Read templates from the AgentOS's own on-disk template set at `reference/agentos-templates/` (in the AgentOS root). These were placed there at setup and may have been tuned to the leader, so future agents inherit the leader's established preferences. Read them from the AgentOS root, not from the plugin. (The new agent's folder sits inside the AgentOS root, so the templates are at the AgentOS root's `reference/agentos-templates/`.)

- **`AGENTS.md`** — from `reference/agentos-templates/AGENTS.template.md`. Fill the Role from the **accepted role definition** (Step 4), the Ownership Boundary (what the role owns and explicitly does not own, derived from the role definition — not from a task list), Source Systems (the tools chosen in 4c, read-only by default; any write access approval-gated), Read Order, Operating Rules, and Approval Gates. The agent must inherit the root Prime Directive and require explicit approval before any send, write, publish, or irreversible action. Reference root files with `../` paths (e.g. `../USER.md`), matching the reference agent — the agent inherits root context, it does not duplicate it.
- **`IDENTITY.md`** — from `reference/agentos-templates/IDENTITY.template.md`. Fill what this agent is, its core purpose, what good looks like, and its scope boundary, all derived from the **accepted role definition** and the leader's context — describing what the agent *is*, not a list of tasks it performs.
- **`SOUL.md`** — from `reference/agentos-templates/SOUL.template.md`. Fill temperament, interaction style, and communication modes appropriate to this agent's job. Drafting behavior must follow the leader's voice from `../USER.md` and mark drafts as drafts.
- **`CLAUDE.md`** — the agent-scoped loader. Write it so it points at **this agent's own** `AGENTS.md`, not the root one. Use exactly this content:

  ```
  # CLAUDE.md

  `AGENTS.md` is the canonical instruction file for this agent.

  ## Read This First

  Read `AGENTS.md` and follow it. It defines everything else: the role, the scope, the prime directive, the file layout, the read order, and the operating rules.

  Do not duplicate those instructions here. This file exists only to load `AGENTS.md` at the start of the session and send you there.
  ```

- **`DECISIONS.md`** — create it with the **same format block** the root AgentOS DECISIONS.md uses, so the leader can see how a decision is recorded. No actual decisions yet. Use exactly this structure (adjust the agent name in the title):

  ```markdown
  # DECISIONS — [Agent Name] Agent

  > This file records durable decisions about how the [Agent Name] agent operates.

  Use it for decisions that affect the agent's role, scope, authority, or operating standards. Do not use it for tasks, notes, or daily context.

  To add a decision, say "remember this decision" and it will be recorded here in the format below.

  ## Format

  ## YYYY-MM-DD — Decision title

  Decision:

  What was decided.

  Reason:

  Why this decision was made.

  Implication:

  What should happen or be true going forward because of this decision.

  ## Decisions

  No decisions recorded yet.
  ```

  Do not invent decisions.

## Step 6 — Verify

Confirm the subfolder now contains all five files: `AGENTS.md`, `IDENTITY.md`, `SOUL.md`, `CLAUDE.md`, `DECISIONS.md`. Confirm `AGENTS.md`, `IDENTITY.md`, and `SOUL.md` contain no leftover angle-bracket tokens — check for any `<...>` pattern, not only the word "placeholder". Confirm `CLAUDE.md` points at the agent's own `AGENTS.md`.

If any file is missing or any token remains, fix it before continuing. If you cannot, stop and tell the leader plainly that the agent was not fully created, and do not claim success.

## Step 7 — Confirm and explain how to start using the agent

Tell the leader warmly, by their preferred name, that their [agent name] agent is ready. Do not list file names. In one or two sentences, restate what the agent will do for them.

**Do not offer to start doing the agent's work in this conversation.** This is important and is a real distinction, not a formality. You are currently operating in the leader's main AgentOS, not as the new agent. The new agent has its own folder and its own instructions; to actually work *as* that agent, the leader needs to open a conversation pointed at the agent's folder, the same way they load their AgentOS. Creating the agent's files is not the same as becoming the agent. If you start "being" the Chief of Staff from the AgentOS root, you are not really running the scoped agent — you are guessing at it from the wrong context.

So instead, give the leader clear, plain-language, step-by-step instructions for how to start using their new agent. Walk them through it conversationally, as numbered steps, in terms a non-technical leader will follow. Cover, in order:

1. In the Codex app, add or open a project for the new agent folder — the [agent name] folder inside their AgentOS.
2. Start a new Local thread in that project.
3. Say "load my agent" so the agent's context comes in.
4. If Codex says the agent cannot see the main AgentOS, reopen the project at the top-level AgentOS folder instead, or grant Codex access to the top-level AgentOS folder using the app's normal project/folder access flow, then say "load my agent" again. The agent needs the parent AgentOS because that is where the leader and organization context live.

Keep it warm and simple — the goal is that the leader knows exactly what to do next in the Codex app. Be clear that parent-folder access is the one people miss, and it is what makes inheritance work. Whenever they want to use this agent again, they open that Codex project or thread and load it.

### Step 7a — Give them a copy-paste project description

Output a short, ready-to-paste description for the new Codex project or thread, in a fenced code block so the leader can copy it cleanly if they want a label for it. Keep it to one or two sentences, written from the agent's perspective/role, personalized to the leader and organization. For example:

```
This is the Chief of Staff agent within [Leader]'s AgentOS at [Organization]. It manages the flow of information, protects the leader's time and focus, prepares them for what's coming, and keeps decisions moving — operating with read-and-draft authority and seeking approval before sending or changing anything.
```

Tell the leader plainly: "Use the text in the box as the description for this agent project if Codex asks for one." Do not include file names or paths in the call-out.

## Failure Handling Summary

- No AgentOS in the folder → stop, redirect to setup.
- Interview incomplete → keep asking; do not build a hollow agent.
- Agent folder already exists → ask whether to update or create a different one; never silently overwrite.
- A token remains or a file is missing at verification → fix, or stop and report plainly. Never claim false success.
