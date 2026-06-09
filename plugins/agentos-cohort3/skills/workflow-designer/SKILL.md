---
name: agentos-workflow-designer
description: >
  Designs and builds the first (or next) workflow for an agent in a leader's AgentOS — for
  example a daily briefing or weekly briefing for a Chief of Staff. Reads the agent it is working
  in, suggests sensible workflows for that specific agent, interviews the leader through guided
  guided Codex input, then builds a real, tested skill for the workflow and offers to schedule it.
  Triggered by "create a workflow", "build a workflow", "set up an automation", "create my daily
  briefing", or "add a routine for this agent". In Codex, the leader may invoke this skill
  explicitly from the skill picker or by asking in plain language. Use when an agent
  already exists and the leader wants to give it a repeatable workflow or automation.
version: 1.0.0
---

# AgentOS Workflow Designer

Design and build a workflow for the agent you are operating in. A **workflow** is a repeatable piece of work the leader can run on demand (for example, "give me my daily briefing"). An **automation** is that same workflow set to run on a schedule. This skill builds the workflow as a real, reusable skill, then offers to turn it into an automation by scheduling it.

**Who you're talking to.** Your audience is high-functioning, highly successful, non-technical executives and leaders. They are sharp and capable, but file systems, folders, and technical terms create friction for them. Speak in plain language. Explain what to do, not how it works under the hood. Never use jargon or show file names, paths, or tool names. Never talk down to them. When something goes wrong, keep your wording simplest of all — a confused leader needs the clearest possible next step, not more detail. This skill body is for you, the executing agent — not for the leader to read.

## Executive Output Contract

Final user-facing output must be short, plain, and useful to a non-technical leader.

- For success, use one to three short sentences.
- Include only what was created, what it does, how to run it, and where to find it in the Codex UI when relevant.
- Do not mention `.codex`, `memory.md`, `MemoryMD`, internal automation folders, local file paths, manifests, plugin roots, command output, connector implementation details, stack traces, or hidden logs.
- Translate technical failures into plain next steps. For example, say "Calendar access needs to be reconnected" rather than naming connector scope errors.
- Keep technical detail in internal logs or files. Do not expose it in the final response unless the leader explicitly asks.

Keep every user-facing question in Codex's structured popup input tool, `request_user_input`, when it is available in the Codex app. Do not print the question and options as normal chat text when the popup tool is available. Never use a free-text prompt except as an explicit "Other / let me describe it" choice. If structured popup input is not available in the current Codex mode, ask the same question conversationally with the same concrete options and wait for the leader's answer before continuing.

If the Codex app exposes native multi-select popup input, use it for questions that say multi-select. If only single-choice popup input is available, use the popup anyway and include an "Other / choose several" path, then ask one short follow-up only when needed.

This skill is **agent-generic**: it must work inside any agent in the AgentOS (Chief of Staff, research assistant, content agent, anything). It learns what the agent is *before* it suggests anything, so its suggestions fit that agent.

## Step 1 — Confirm you are inside an agent

You must be operating inside an agent folder (one with its own `AGENTS.md` that references the parent AgentOS via `../`). Confirm:

- The agent's `AGENTS.md`, `IDENTITY.md`, `SOUL.md` are present in the working folder.
- The parent AgentOS files are reachable (`../USER.md`, `../ORG.md`). If they are not, Codex cannot read the top-level AgentOS folder. Stop and tell the leader, in plain language, to open the top-level AgentOS folder as the Codex project, or grant Codex access to that parent folder using the app's normal project/folder access flow, then try again. (Same fix as the load skill.)

If there is no agent here at all, tell the leader they need to create an agent first by saying "create a new agent", and stop.

## Step 2 — Read and understand the agent

Read, silently:

- The agent's `AGENTS.md`, `IDENTITY.md`, `SOUL.md` — its role, ownership boundary, and the **source systems / connectors** it was given (email, calendar, Slack, CRM, etc.).
- `../USER.md` and `../ORG.md` — who the leader is and what the business does.

From this, form a clear picture of: what this agent is for, who it serves, and what tools it can actually use. Every workflow you suggest must be something this agent could genuinely do with the connectors it has. Do not suggest a workflow that needs a tool the agent wasn't given.

## Step 3 — Suggest workflows (guided pop-up)

Call `request_user_input`: "What would you like your [agent name] to do for you, as a repeatable workflow?"

Propose options tailored to *this* agent, derived from Step 2. For a Chief of Staff with email and calendar, sensible first options are:

- A daily briefing
- A weekly briefing
- (one or two more sensible options inferred from the agent's role and connectors)
- Other — let me describe it

Keep daily and weekly as **separate** options, not bundled. Always include "Other — let me describe it" last as the free-text path. For a different kind of agent, suggest workflows that fit *that* agent (e.g. for a research assistant: "a pre-meeting company brief", "a weekly competitor scan").

**Use the bundled reference workflows as ready-made starting points.** The plugin ships proven, pro-level reference workflows for a Chief of Staff at the plugin root's `reference-agents/chief-of-staff/workflows/` folder — `daily-briefing/` and `weekly-briefing/`, each with a `SKILL.md` and an output `template.md`. When the leader picks a daily or weekly briefing (or the agent being built is Chief-of-Staff-like), use the matching reference workflow as the basis: adapt its skill and template to the leader and their connectors rather than starting from a blank page. These references are the quality bar — build to their standard. For workflows with no reference, build from scratch to the same standard.

## Step 4 — Interview the workflow details (guided pop-ups)

Once they pick a workflow, ask only what you need to define it well, each with `request_user_input` and sensible options:

- **What it should include** — offer concrete content choices for that workflow (e.g. for a daily briefing: "Today's calendar and priorities", "Plus unread/important email", "Plus open commitments and follow-ups"). If the Codex guided-input UI supports selecting more than one option, allow multiple selections. If it only supports a single choice, present the same options as a checklist and ask the leader to choose all that apply in one answer.
- **How it should be delivered** — e.g. "A short written briefing", "A bulleted summary", "Other".
- Anything else genuinely needed to make the workflow concrete. Do not over-interview; keep it tight.

Confirm the assembled workflow back to the leader in one short plain-language summary before building.

## Step 5 — Build the workflow as a real, tested skill (use skill-creator)

Do **not** hand-write a quick skill. Use the proper skill-creation process so the result is robust and will not break when the leader uses it in slightly different ways. Invoke the **`skill-creator`** skill to build the workflow skill, providing:

- The workflow's purpose and exact behavior from the interview.
- The agent's context (role, connectors) so the skill is scoped correctly.
- A clear description with trigger phrases the leader would actually say (e.g. "give me my daily briefing", "run my morning brief").

Let skill-creator do its job — draft, test, and validate the skill — so it is bulletproof. Explain to the leader, in plain language, that you are building and testing their workflow so it works reliably, and that this part can take a little time. That tradeoff is worth it: a tested skill won't break on them later.

**What "use skill-creator" means in this guided context.** skill-creator's full process includes an optional multi-iteration eval/benchmark loop with the leader reviewing outputs. That full loop is appropriate when the leader wants it, but for a first workflow build you do not have to run the entire benchmark apparatus to call the skill done. The non-negotiable parts you MUST do, in order:

1. Follow skill-creator to **draft** a complete, production-quality `SKILL.md` — proper frontmatter (`name`, a `description` under 1024 characters with real trigger phrases the leader would say), and a clear imperative body that uses only the connectors this agent has.
2. **Test it at least once** — run the workflow against the agent's real context (or a realistic dry run) and confirm it produces the intended output without error. If it fails, fix and re-test before continuing.
3. **Validate** the frontmatter and structure (YAML parses, name + description present, description under 1024 chars).

Offer the leader the deeper skill-creator eval loop if they want maximum confidence, but the three steps above are the floor. Never ship a workflow skill that hasn't been drafted properly and run at least once.

Every generated workflow skill must include its own final-output rule: return the workflow result or brief only, plus at most one short plain-language connector note when something unavailable affects the result. Allowed: "I could not access your calendar today, so this brief is based on email only." Forbidden: "Calendar connector failed scope auth; memory.md updated."

### Where the workflow skill goes

Store the finished workflow skill inside the agent's own **`workflows/`** folder, so it travels with the agent:

```
[agent-folder]/
└── workflows/
    └── [workflow-name]/
        └── SKILL.md
```

(Use a clear kebab-case workflow name, e.g. `daily-briefing`.) This keeps each agent's workflows with the agent. If skill-creator produces a packaged `.skill` file for installation, present it to the leader so they can install it the same way they installed the AgentOS plugin, and also keep the source in the agent's `workflows/` folder.

## Step 6 — Offer to schedule it (hand off to the scheduler)

A workflow becomes an **automation** when it runs on a schedule. Once the workflow skill exists, use guided Codex input: "Would you like this to run automatically on a schedule?" Options: "Yes — daily", "Yes — weekly", "No, I'll run it myself".

If they choose daily or weekly, ask the time with a second guided Codex prompt so they never face a blank prompt — for example "What time should it run?" with options like "7:00 AM", "8:00 AM", "9:00 AM", "Other time" (the "Other time" choice is the free-text path). For weekly, also ask which day the same way.

Then create or prepare a Codex automation if the current Codex app environment exposes automation creation. Pass it a **self-contained** prompt that runs this workflow skill — future runs must not depend on this conversation, so spell it out: which agent, which workflow skill to run, which connectors it may use, and what result it should produce. The automation prompt must also include this final-output rule: "In the final response, deliver only the useful workflow result and any plain-language action needed from the leader. Do not mention run logs, memory files, hidden runtime state, local paths, connector internals, command output, or implementation details."

If automation creation is not available from the current thread, say plainly that the automation was not created, then give exactly one Codex UI next step: open Codex Automations and create it there using the schedule they chose. Do not provide hidden paths, tool details, or internal prompt mechanics unless the leader explicitly asks.

If they decline, that's fine — the workflow stays available to run on demand whenever they ask.

## Step 7 — Confirm

Tell the leader plainly that their workflow is built and ready, in one to three short sentences. If it is on demand, say what it does and how to run it ("just say 'give me my daily briefing'"). If it is scheduled, say the plain workflow name, the schedule, that it will appear under Codex Automations, and how to run it manually. No file names, paths, logs, memory terminology, connector internals, or jargon.

## Failure Handling Summary

- Not inside an agent / parent unreachable → stop, give the Codex project/folder-access fix or send them to create-agent.
- Suggested workflow needs a connector the agent doesn't have → don't suggest it; only propose what the agent can actually do.
- skill-creation fails or doesn't validate → tell the leader plainly it didn't complete; do not leave a half-built, breakable workflow and claim success.
- Scheduling declined → leave the workflow as on-demand; not a failure.
