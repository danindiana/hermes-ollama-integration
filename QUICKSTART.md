# Quickstart: Integrating Ollama with Hermes Agent

If you have a local Ollama server running and want it to appear as an interactive, multi-select menu inside Hermes Agent's `/model` picker, follow these steps.

### 1. Edit your Config
Open your \`~/.hermes/config.yaml\` file.

### 2. Add the Custom Provider
Add the following lines under the \`custom_providers\` section. **Crucially**, leave the \`model:\` field empty (an empty string \`""\`). This empty string is what triggers Hermes to probe the Ollama API and present a menu.

\`\`\`yaml
custom_providers:
  - name: "Local Ollama"
    base_url: "http://localhost:11434/v1"
    api_key: "ollama"
    model: ""
\`\`\`

### 3. Test the Menu
Run the interactive model picker:
\`\`\`bash
hermes model
\`\`\`

You will now see \`Local Ollama (localhost:11434/v1)\` in the list. Select it. Hermes will hit the Ollama \`/models\` endpoint and present a secondary menu containing all your installed local models (e.g., \`qwen2.5-coder:14b\`, \`deepseek-r1:32b\`). Select one to set it as your default.
