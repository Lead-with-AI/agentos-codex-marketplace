# AgentOS Template Guidance

This directory contains AgentOS templates owned by `agent-os-system`.

Templates are not a default file list. The scaffold mode decides which templates apply.

## Core Rule

Inheritance does not imply local copies.

A scoped agent using this AgentOS inherits the root baseline. It does not need local copies of root-equivalent files unless there is a specific, justified local override.

Scoped agents are separate from day one. They may sit as subfolders inside the AgentOS for local convenience, but they are not part of the AgentOS core files.

## Scoped Agent Adjacent To This AgentOS

Default templates:

- `AGENTS.template.md`
- `PROJECT.template.md`

Optional templates, only when justified:

- `README.template.md`
- `SKILL.template.md`
- `RUNBOOK.template.md`
- `MEMORY-README.template.md`
- `LOGS-README.template.md`

Conditional local overrides, only when explicitly justified:

- `IDENTITY.template.md`
- `SOUL.template.md`
- `USER.template.md`
- `ORG.template.md`
- `PRINCIPLES.template.md`
- `DECISIONS.template.md`
- `BRAND.template.md`
- `DESIGN.template.md`

Do not create local root-equivalent files for a scoped agent just because those files exist at the root.

Do not add scoped-agent folders to the AgentOS core repo.

## Standalone AgentOS/System

Default full baseline:

- `AGENTS.template.md`
- `IDENTITY.template.md`
- `SOUL.template.md`
- `USER.template.md`
- `ORG.template.md`
- `PRINCIPLES.template.md`
- `DECISIONS.template.md`

Use the full baseline when the new folder is a root or standalone AgentOS/system that will not inherit this AgentOS root.

## Project Inside This AgentOS

Use this only for projects that are genuinely part of maintaining AgentOS itself.

General content systems, production systems, and leaf-agent projects should be separate sibling repos.

Likely templates:

- `PROJECT.template.md`
- `AGENTS.template.md`, only if scoped operating instructions are needed
- `README.template.md`, only if useful for human onboarding or handoff

Optional folders and files should be created only with a current use.

## Verification

Before using templates, confirm:

- the scaffold mode is explicit
- scoped agents default to `AGENTS.md` and `PROJECT.md`
- scoped agents are excluded from the AgentOS core repo
- full baseline templates are reserved for root or standalone AgentOS/system use
- conditional templates are local overrides only
- no optional folder is created as a placeholder
