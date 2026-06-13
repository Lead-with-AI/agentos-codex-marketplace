---
name: agentos-suggest-next-agent
description: >
  Looks at the leader's role, company, existing agents, and available Codex plugin/skill
  metadata to suggest the best 3-4 agents to build next. Each suggestion is matched to the
  leader's specific role and explains why it fits. When the leader chooses one, hands off
  directly to agentos-create-agent to build it. Triggered by "what agent should I build next",
  "suggest my next agent", "choose my second agent", "what plugins match my role", or
  "help me pick my next agent". In Codex, use whenever a leader with an existing AgentOS
  wants to expand their agent team and is not sure what to build next.
version: 0.2.0
---

# AgentOS Suggest Next Agent

Use Codex plugin and skill metadata, match the available options against the leader's role and context, and present a shortlist of agent candidates. When the leader picks one, hand off to `agentos-create-agent`.

**Who you're talking to.** Your audience is high-functioning, highly successful, non-technical executives and leaders. Speak in plain language. Never use jargon, file names, plugin IDs, or technical terms. The leader should feel like they are being helped to make a good choice - not shown a catalogue. This skill body is for you, the executing agent - not for the leader to read.

## Executive Output Contract

Final user-facing output must be short, plain, and useful to a non-technical leader.

- For success, use one to three short sentences plus the scripted text choice when a decision is needed.
- Include only the recommended agents, why each fits, and the next action.
- Do not mention `.codex`, plugin IDs, file names, internal folder paths, plugin roots, command output, stack traces, hidden logs, or implementation details.
- Translate technical failures into plain next steps.
- Keep detailed reasoning internal unless the leader explicitly asks for it.

## Step 1 - Confirm an AgentOS exists

Check the working folder for `USER.md`, `ORG.md`, and `AGENTS.md`.

- If any are missing, stop. Tell the leader they need to set up their AgentOS first by saying "set up my AgentOS". End the skill.
- If present, continue.

## Step 2 - Load leader context silently

Read silently:

- `USER.md` - the leader's name, role, and working style.
- `ORG.md` - the company, industry, and business context.
- `AGENTS.md` - the root operating instructions.

Then inspect only the top-level subfolders in the AgentOS root. Treat a folder as an existing scoped agent only if it contains its own `AGENTS.md`.

Extract three things:

1. **Role summary** - one plain sentence describing what the leader does, such as "Chief AI Officer at an AI transformation company".
2. **Industry context** - the business domain and any known priorities.
3. **Existing agents** - names and jobs of agents already built, so suggestions fill genuine gaps.

Do not read every file in every agent folder. For each existing agent, read only enough to identify its name and role, usually its `AGENTS.md` and `IDENTITY.md` if present.

## Step 3 - Search available Codex plugin and skill options

Use the best Codex discovery surface available in the current session:

1. If Codex exposes a plugin or skill search/discovery tool, use it with the leader's role summary as the intent and their role title and industry as keywords.
2. If no plugin search tool is exposed, use the installed and available plugin/skill metadata already visible in the Codex session.
3. If neither gives enough signal, fall back to the leader's AgentOS context and common executive agent patterns rather than inventing a fake marketplace result.

Do this silently. Do not show raw results, plugin IDs, tool names, or internal metadata to the leader.

In Codex, an installed plugin is not the same as a built AgentOS agent. A plugin can suggest the kind of agent to build, but the agent still needs to be created inside the leader's AgentOS.

## Step 4 - Score and filter

From the available Codex plugin/skill options, select the 3-4 strongest matches for this specific leader. Apply these filters:

- **Skip** any option that maps directly to an agent the leader already has running.
- **Prefer** options whose skills align closely with the leader's stated role and the kind of repeating work their role involves.
- **Prefer** options that have multiple relevant skills over ones with only a tangential match.
- **Include** the reason for each suggestion in plain language - not the plugin description, but why *this leader* would benefit.

Build a shortlist internally. Do not show this internal structure to the leader:

```text
1. [Agent name you would give it] - based on [plugin or skill signal internally]
   Why it fits: [one plain sentence tied to the leader's role and context]
   What it does: [one plain sentence on the job it takes off the leader's plate]
```

## Step 5 - Present the shortlist

Show the leader their shortlist as a clean, scannable set of options. For each candidate:

- Give it a plain agent name, not a plugin ID.
- Write one sentence on what repeating job it handles.
- Write one sentence on why it fits their specific role.

Then present a scripted text choice:

- **Question text:** "Which of these would you like to build first?"
- **Options:** one option per suggested agent, plus "None of these - let me describe what I need".

If they choose "None of these", invite them to describe the job in a sentence or two, then repeat the matching step using that description as the intent.

## Step 6 - Hand off to create-agent

Once the leader has chosen, tell them in one short sentence what you are about to build. Then invoke `agentos-create-agent`, passing:

- The chosen agent name in plain language.
- The plugin or skill signal it is based on, internally for context.
- The leader's role and organization context from `USER.md` and `ORG.md`.

Do not re-ask questions that `agentos-create-agent` will ask. Let `agentos-create-agent` run its own interview from the role-definition step onward. Your job is to make the choice feel easy and hand off cleanly.

## Failure Handling

- No AgentOS -> stop, redirect to setup.
- Codex plugin/skill discovery gives no useful signal -> tell the leader plainly that no strong match stood out, and offer to let them describe the agent they have in mind so it can be built directly via `agentos-create-agent`.
- Leader chooses "None of these" twice -> stop suggesting and ask them to describe the job in their own words; use that to drive `agentos-create-agent` directly.
- Never show plugin IDs, internal names, file paths, raw search output, or tool metadata to the leader.
