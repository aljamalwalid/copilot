# Cloudera AI Inference package

Registers **Cloudera AI Inference** language and embedding providers with Jupyter AI’s
`jupyter_ai.model_providers` and `jupyter_ai.embeddings_model_providers` entry points.

## Configuration

Point **`COPILOT_CONFIG_DIR`** at a JSON file that includes **`aiInferenceModels`**: an array of
objects with at least **`name`** and **`endpoint`**. Non-embedding endpoints are used for chat;
entries whose `endpoint` ends with `/embeddings` are treated as embedding models.

Optional **`COPILOT_EMBEDDING_CONFIG_DIR`**: additional JSON file whose embedding models are merged
into the embedding provider (same schema).

Set these environment variables **before** the IPython kernel imports providers (e.g. before
JupyterLab starts), so model lists load correctly.

## How this fits Jupyter AI v3

- **JupyterLab agent chat (v3)** discovers models primarily through **`jupyter_ai_litellm`** (LiteLLM’s catalog). That path does **not** read `jupyter_ai.model_providers`.
- **Notebook `%%ai` with `jupyter-ai-magics`** (the 2.x magics package) **does** load these entry points. Use:

  ```bash
  pip install "jupyter-ai>=3" jupyter-ai-magics cloudera_ai_inference_package
  ```

  In a notebook:

  ```python
  %load_ext jupyter_ai_magics
  ```

  Then use model IDs like `cloudera:<your-model-name>` where `<your-model-name>` matches a
  `name` in `aiInferenceModels`.

- You can install **`jupyter-ai` 3** and **`jupyter-ai-magics` 2.x** together: the metapackage
  does not replace the magics library. Prefer **`jupyter_ai_magics`** for `%%ai` when you need
  Cloudera inference; **`jupyter_ai_magic_commands`** (from `jupyter-ai[magics]`) is LiteLLM-centric
  and will not list Cloudera models from this package.

## Install from this repo

```bash
pip install -e ./packages/cloudera-ai-inference-package
```
