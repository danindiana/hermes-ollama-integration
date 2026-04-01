# Hermes Agent: Native Ollama Integration Fork

This repository documents the commissioning, integration, and proposed fork of the [Hermes Agent](https://github.com/nousresearch/hermes-agent) to provide a seamless, native experience for local **Ollama** users.

## Motivation
Hermes Agent is an incredibly powerful terminal-native AI "Chief of Staff" built by Nous Research. While it supports custom OpenAI-compatible endpoints, it lacks a dedicated, interactive menu option for local Ollama instances. For users with high-end consumer hardware (e.g., dual NVIDIA RTX GPUs and 128GB RAM), maintaining a local, private fleet of models (like \`qwen2.5-coder:14b\` or \`deepseek-r1:32b\`) is essential.

This project outlines a strategy to fork the Hermes CLI to include a dedicated **Ollama Integration Wizard**.

## The Proposed Wizard (Hermes Ollama Integration)
Instead of manually editing \`~/.hermes/config.yaml\` to add a generic "Custom endpoint" with a blank model field, the proposed fork adds:
1. **Auto-Discovery:** An explicit \`/model ollama\` route that automatically queries \`http://localhost:11434/api/tags\`.
2. **Interactive Selection:** A dedicated interactive menu (\`TerminalMenu\`) populated directly from the local Ollama catalog.
3. **Wizard Integration:** Adding "Local Ollama" as a top-level provider during the initial \`hermes setup\` process.

## Current Working Solution (No Fork Required)
Until the fork is merged, we achieved native integration by injecting a named custom provider into the user's \`config.yaml\` with a cleared \`model:\` field. This forces Hermes to probe the endpoint and display an interactive menu of all available models whenever the user selects "Local Ollama" from the \`/model\` menu.

See \`QUICKSTART.md\` for instructions on implementing this workaround.

## Architecture
See the included \`architecture.png\` and \`architecture.svg\` diagrams for a visual representation of how the Hermes CLI, the custom provider shim, and the Ollama local API interact.

## Credits
- Commissioning Session Date: 2026-04-01
- Target System: AMD Ryzen 9 5950X, 128GB RAM, RTX 3080 + RTX 3060.
- Orchestrated by: Gemini CLI.
