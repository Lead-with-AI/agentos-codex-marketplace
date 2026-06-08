# AgentOS Cohort 3

Sets up and runs a personal AgentOS — a portable operating layer that keeps a leader's work organized, their agents aligned, and their context available across sessions and tools.

An AgentOS is a folder of plain files (`AGENTS.md`, `IDENTITY.md`, `SOUL.md`, `USER.md`, `ORG.md`, `PRINCIPLES.md`, `CLAUDE.md`, `DECISIONS.md`). Because it is just files, it travels: any AI tool that reads `AGENTS.md` can pick up the same context. This Codex plugin builds, loads, and extends that folder for a non-technical business leader, without requiring them to touch the files directly.

## What each capability does

You can trigger every capability two ways in Codex: explicitly invoke the skill, or just say what you want in plain words. Both run the same skill logic.

- **Set up the AgentOS** — "set up my AgentOS", "create the AgentOS", "get this AgentOS started"
  Runs once in an empty folder. Interviews the leader, researches their company, and writes the AgentOS files. Never overwrites an existing setup.

- **Load the AgentOS** — "load my AgentOS", "load my AgentOS into this conversation", "get my AgentOS running"
  Run at the beginning of every new conversation. Reads all context files (and any agent folders), then gives a short plain-language briefing. Use this because a fresh conversation does not always load context on its own.

- **Create an agent** — "create a new agent", "add an agent", "build me a chief of staff"
  Interviews the leader and scaffolds a new scoped agent folder, using the Chief of Staff reference agent as the quality bar.

- **Capture a decision** — "remember this decision", "log this decision", "save this for later"
  Records a decision into the portable `DECISIONS.md` so it persists outside any single tool, with an optional mirror into memory.

- **Design a workflow** — "create a workflow", "build my daily briefing", "set up an automation"
  Run inside an agent. Reads the agent and its connectors, suggests fitting workflows (e.g. daily or weekly briefing for a Chief of Staff), builds a real tested skill for the workflow in the agent's `workflows/` folder, and offers to schedule it as an automation.

- **Upgrade an existing AgentOS** — "upgrade my AgentOS", "migrate my AgentOS", "check my AgentOS"
  For an AgentOS built earlier (often by hand). Backs everything up, then analyzes each file, keeps the leader's worthwhile work, and migrates it to the current standard structure. Setup also offers this automatically when it detects an existing AgentOS.

## Components

| Type | Name | Purpose |
|------|------|---------|
| Skill | setup | One-time AgentOS initialization |
| Skill | load | Per-conversation context loading and briefing |
| Skill | create-agent | Scaffold a new scoped agent |
| Skill | decision-capture | Record durable, portable decisions |
| Skill | workflow-designer | Build a tested workflow skill for an agent, optionally scheduled |
| Skill | upgrade | Migrate an existing AgentOS to the current structure, keeping the leader's work |

The plugin also bundles `core-files/` (the portable AgentOS files copied in during setup), `reference-agents/chief-of-staff/` (a complete example agent), and `Templates/` (scaffolds the create-agent skill populates).

## Setup

No environment variables or external services are required. Web search is used during setup to research the leader's organization.

## Notes for the leader

You do not need to read the skill files. They are written for Codex to execute precisely. You only need to know what each one does — see the list above.
