<p align="center">
  <img src="docs/source/_static/jupyter_logo.png" alt="Jupyter logo" width="120">
</p>

<h1 align="center">Jupyter AI</h1>

<p align="center"><i>An open source extension that connects AI agents to computational notebooks in JupyterLab.</i></p>

Jupyter AI brings agentic AI to JupyterLab. It provides a native chat UI where you can collaborate with frontier AI agents — including Claude, Codex, GitHub Copilot, Gemini, Goose, Kiro, Mistral Vibe, and OpenCode — all integrated through the [Agent Client Protocol (ACP)](https://agentclientprotocol.com). Agents are automatically detected when their dependencies are installed, so getting started is as simple as installing Jupyter AI and the agent of your choice.

Agents in Jupyter AI can read and write files, run terminal commands, and interact with notebooks through a built-in [Jupyter MCP server](https://github.com/jupyter-ai-contrib/jupyter-server-mcp). A permission system gives you guardrails over agent actions — agents request approval before writing files or executing commands. You can also create multiple concurrent chats, drag and drop files or notebook cells as context, and collaborate in real time with other users connected to the same server.

Jupyter AI is designed to be flexible and extensible. You can add custom [MCP servers](https://modelcontextprotocol.io) to give agents access to domain-specific tools, resources, and prompts. Developers can build and register their own AI personas using the entry points API. By building on open standards like ACP and MCP, Jupyter AI avoids vendor lock-in and gives you access to the full ecosystem of compatible agents and tools.

## Cloudera Copilot

This branch tracks **upstream Jupyter AI v3** (`jupyterlab/jupyter-ai`) and keeps Cloudera-only add-ons that do **not** restrict which chat models appear in the UI.

**Chat models are chosen dynamically** in JupyterLab agent chat: Jupyter AI 3 serves the model list from **`jupyter_ai_litellm`** (`GET /api/ai/models/chat`), i.e. LiteLLM’s catalog. Users pick any model that API exposes.

### Cloudera Copilot branding (this fork)

Product copy and assistant identity match **Cloudera Copilot**, not generic “Jupyter AI” / “Jupyternaut” in user-visible strings where we control them:

- **`packages/jupyter-ai-jupyternaut`** — Vendored from [`jupyter-ai-contrib/jupyter-ai-jupyternaut`](https://github.com/jupyter-ai-contrib/jupyter-ai-jupyternaut), version **0.0.12**, with Cloudera Copilot naming in the Lab UI, status bar, settings, inline completions label, and the **default persona** (`name="Cloudera Copilot"`) plus an updated **system prompt** intro. **`jupyter_ai_jupyternaut/static/cloudera-copilot.svg`** is served at **`/api/ai/static/cloudera-copilot.svg`** so **`jupyter-ai-magics`** `ClouderaCopilotPersona` avatars resolve. This fork **tracks a built** `jupyter_ai_jupyternaut/labextension/` in git (see package `.gitignore`); after changing TypeScript run `yarn install`, `./node_modules/.bin/tsc`, and `jupyter labextension build .` (or use a local venv with `jupyterlab` installed), then commit the updated `labextension/` and `lib/` outputs. Rebase when upgrading upstream.
- **`packages/jupyter-ai-magics`** — Synced from [`cloudera/copilot`](https://github.com/cloudera/copilot) `main` (`packages/jupyter-ai-magics`), including **`CHAT_SYSTEM_PROMPT`** (“You are Cloudera Copilot…”) and **`ClouderaCopilotPersona`** for the `%%ai` path.

**Engine / image installs** (pin your fork SHA): install **`jupyter-ai` 3.x** from PyPI, then override the persona stack and magics from this repo, for example:

```text
jupyter_ai_jupyternaut @ https://github.com/<org>/copilot/archive/<sha>.zip#subdirectory=packages/jupyter-ai-jupyternaut
jupyter_ai_magics @ https://github.com/<org>/copilot/archive/<sha>.zip#subdirectory=packages/jupyter-ai-magics
cloudera_ai_inference_package @ https://github.com/<org>/copilot/archive/<sha>.zip#subdirectory=packages/cloudera-ai-inference-package
```

### Cloudera AI Inference (still supported)

**`packages/cloudera-ai-inference-package`** registers Cloudera-hosted **language** and **embedding** providers via `jupyter_ai.model_providers` and `jupyter_ai.embeddings_model_providers`. Configure with **`COPILOT_CONFIG_DIR`** (JSON with **`aiInferenceModels`**: `name`, `endpoint`, …) and optionally **`COPILOT_EMBEDDING_CONFIG_DIR`**. Details: `packages/cloudera-ai-inference-package/README.md`.

**Compatibility with Jupyter AI v3:**

| Surface | How Cloudera inference appears |
|--------|--------------------------------|
| **JupyterLab agent chat (v3)** | LiteLLM model list only. Cloudera HTTP APIs that are **OpenAI-compatible** can be exposed through **LiteLLM** (custom base URL / env) so they appear like other LiteLLM models. |
| **Notebook `%%ai`** | Use **`jupyter-ai-magics`** (2.x) + this package: `%load_ext jupyter_ai_magics`, then `cloudera:<model-name>` matching `aiInferenceModels[].name`. Entry points are loaded by **`jupyter_ai_magics`**, not by **`jupyter_ai_magic_commands`** (`jupyter-ai[magics]`). |

Install **Jupyter AI 3** and **`jupyter-ai-magics` 2.x** together when you need both agent chat and Cloudera-backed `%%ai`:

```bash
pip install "jupyter-ai>=3" jupyter-ai-magics
pip install -e ./packages/cloudera-ai-inference-package
```

**`copilot_models.json`** / **`copilot_embedding_models.json`** — optional reference only; they do **not** drive JupyterLab’s LiteLLM model picker on this branch.

To sync this branch with upstream: `git fetch public && git merge public/main` (resolve conflicts if any).

## Quick Links

- [Getting Started](https://jupyter-ai.readthedocs.io/en/latest/getting-started.html) — installation, agent setup, and first chat
- [User Guide](https://jupyter-ai.readthedocs.io/en/latest/users/index.html) — chat features, notebook tools, and custom MCP servers
- [Contributor Guide](https://jupyter-ai.readthedocs.io/en/latest/contributors/index.html) — how to contribute to Jupyter AI
- [Developer Guide](https://jupyter-ai.readthedocs.io/en/latest/developers/index.html) — building custom agents and MCP servers
- [Troubleshooting](https://jupyter-ai.readthedocs.io/en/latest/users/troubleshooting.html) — common issues and solutions

## Governance

Jupyter AI is currently under incubation as part of the JupyterLab organization.
