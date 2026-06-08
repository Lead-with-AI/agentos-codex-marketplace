# Codex UI Test Checklist

Test only through the Codex app UI before cohort rollout.

## Matrix

- macOS with a clean Codex install or clean plugin state
- Windows with a clean Codex install or clean plugin state
- existing Codex plugins already installed
- no existing custom marketplaces
- after a plugin version update

## Test Cases

1. Add marketplace using the exact UI fields:

```text
Source:
Lead-with-AI/agentos-codex-marketplace

Git ref:
main

Sparse paths:
.agents/plugins
plugins/agentos-cohort3
```

2. Confirm **Lead with AI** appears as a marketplace.
3. Confirm **AgentOS Cohort 3** appears inside it.
4. Install via **Add to Codex**.
5. Start a new local project in an empty folder.
6. Run:

```text
Set up my AgentOS.
```

7. Confirm setup creates the expected AgentOS files.
8. Run:

```text
Load my AgentOS.
Create a new agent.
Remember this decision: AgentOS was installed from the Lead with AI Codex marketplace.
```

9. Confirm the workflow uses Codex language, not Claude Cowork install language.

## Sparse Path Fallback

If the sparse path field fails with:

```text
.agents/plugins
plugins/agentos-cohort3
```

test:

```text
.agents/plugins
plugins
```

The final cohort instructions must use whichever UI input succeeds on both Mac and Windows.
