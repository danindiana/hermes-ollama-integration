import yaml
import os
import requests
from pathlib import Path

def integrate_ollama():
    config_path = Path.home() / ".hermes" / "config.yaml"
    ollama_url = "http://localhost:11434/v1"
    
    print("⚕ Hermes-Ollama Integration Wizard")
    print("-----------------------------------")
    
    # 1. Check if Ollama is running
    try:
        resp = requests.get("http://localhost:11434/api/tags", timeout=2)
        models = [m['name'] for m in resp.json().get('models', [])]
        print(f"✓ Detected Ollama with {len(models)} local models.")
    except Exception:
        print("✗ Could not connect to Ollama at http://localhost:11434")
        return

    # 2. Load existing config
    if config_path.exists():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {}

    # 3. Ensure custom_providers list exists
    if "custom_providers" not in config:
        config["custom_providers"] = []

    # 4. Check if "Local Ollama" is already there
    exists = any(p.get("name") == "Local Ollama" for p in config["custom_providers"])
    
    if exists:
        print("ℹ 'Local Ollama' provider is already configured.")
    else:
        # 5. Inject the provider
        new_provider = {
            "name": "Local Ollama",
            "base_url": ollama_url,
            "api_key": "ollama",
            "model": "" # Empty triggers the multi-select menu
        }
        config["custom_providers"].append(new_provider)
        
        with open(config_path, "w") as f:
            yaml.dump(config, f, default_flow_style=False)
        
        print("✓ Successfully injected 'Local Ollama' into your config.yaml.")
        print("✓ Note: The 'model' field was left empty to enable the interactive menu.")

    print("\nNext Steps:")
    print("1. Run: hermes model")
    print("2. Select: 'Local Ollama'")
    print("3. Choose your desired model from the secondary menu.")

if __name__ == "__main__":
    integrate_ollama()
