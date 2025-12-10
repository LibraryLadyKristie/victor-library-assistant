# Victor tiny, private library assistant

Victor is a 100% local, Ollama-powered LLM that was created by Ms. Kristie Feguer, a librarian.  
No cloud, no OpenAI/Claude/Gemini/xAI, no internet required after setup.

- Runs on Llama 3.2 3B (or 1B) at temperature 0.1
- Greets patrons on startup
- Family-Friendly

Perfect for small libraries that want a local, private AI.

## Quick start
```bash
ollama create victor -f Victor.ModelFile
ollama run victor
Howdy, Partner! Welcome to the library, how can I help you today?

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)