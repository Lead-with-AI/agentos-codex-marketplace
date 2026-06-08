# PROJECT - <Agent Name>

Use this template by default for scoped agents inside this AgentOS.

Scoped agents inherit root AgentOS context. Inheritance does not imply local copies.

## What This Agent Is

<One paragraph describing the scoped agent and the folder it operates in.>

## Why It Matters

<Why this agent earns a scoped folder inside AgentOS.>

## Ownership

This agent owns:

- <Owned workflow, system, or artifact>

This agent does not own:

- <Out-of-scope workflow, system, or artifact>

## Source Systems

The agent may inspect:

- <Read-only source system>

The agent may prepare changes for:

- <Write-capable source system, if any>

Every write, send, publish, schedule, delete, move, or system-of-record change requires explicit approval unless the user later defines a narrower approved automation.

## Goals

1. <Goal 1>
2. <Goal 2>
3. <Goal 3>

## First Workflows

- <Workflow 1>
- <Workflow 2>

## Folder Design

Required files:

- `PROJECT.md` defines agent purpose, ownership, source systems, risks, and success.
- `AGENTS.md` defines scoped operating behavior.

Optional files and folders:

- `README.md` only when human onboarding or handoff requires it.
- `skills/` only for repeated workflows.
- `runbooks/` only for operating procedures, setup, demos, or recovery.
- `memory/` only for curated durable facts.
- `logs/` only for dated operating or verification notes.
- `templates/` only for repeated artifacts.
- `audits/` only for structured reviews.

Do not add optional folders without a current use.

Do not add local `IDENTITY.md`, `SOUL.md`, `USER.md`, `ORG.md`, `PRINCIPLES.md`, or `DECISIONS.md` unless the scaffold records a specific local override reason.

## Inheritance

This folder inherits the root AgentOS baseline:

- `AGENTS.md`
- `IDENTITY.md`
- `SOUL.md`
- `USER.md`
- `ORG.md`
- `PRINCIPLES.md`

Conditional root files stay conditional:

- `DECISIONS.md` for prior AgentOS decisions.
- `BRAND.md` for brand, voice, naming, messaging, or public-facing material.
- `DESIGN.md` for visual standards, interfaces, or design systems.
- Archived `CONTEXT.md` for historical lookup only.

Local root-equivalent files are not part of the default scoped-agent scaffold.

## Risks

- **<Risk name>.** <Risk and mitigation.>

## Success Looks Like

- <Observable success condition>

## Definition Of Done

- <Verification condition>
