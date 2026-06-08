# Lead with AI Codex Marketplace

This repository hosts the Lead with AI Codex marketplace for AgentOS cohort users.

The supported cohort install path is the Codex app UI:

```text
Codex -> Plugins -> Add marketplace
```

No command-line steps, archive files, local file editing, or scripts are required for cohort users.

## Install AgentOS Cohort 3

1. Open Codex.
2. Open **Plugins**.
3. Click **Add marketplace**.
4. Fill in:

```text
Source:
Lead-with-AI/agentos-codex-marketplace

Git ref:
main

Sparse paths:
.agents/plugins
plugins/agentos-cohort3
```

5. Click **Add marketplace**.
6. Open the **Lead with AI** marketplace.
7. Click **Add to Codex** on **AgentOS Cohort 3**.
8. Start a new local project folder.
9. Prompt Codex:

```text
Set up my AgentOS.
```

## If Sparse Paths Need The Broader Setting

Use this only if the exact sparse paths above fail during Mac and Windows validation:

```text
.agents/plugins
plugins
```

The cohort instructions should use whichever sparse path input succeeds on both Mac and Windows.

## Updating The Plugin

Updates are managed through this GitHub repository.

1. Update the plugin source locally.
2. Validate the plugin manifest and structure.
3. Copy the updated plugin into:

```text
plugins/agentos-cohort3
```

4. Bump the plugin version in:

```text
plugins/agentos-cohort3/.codex-plugin/plugin.json
```

5. Push to `main`.
6. Test the Codex UI refresh or update path.
7. Tell cohort users to refresh or update the **Lead with AI** marketplace from the Codex plugin UI.

## Repository Contents

```text
.agents/
  plugins/
    marketplace.json
plugins/
  agentos-cohort3/
    .codex-plugin/
      plugin.json
    README.md
    skills/
    Templates/
    core-files/
    reference-agents/
README.md
```
