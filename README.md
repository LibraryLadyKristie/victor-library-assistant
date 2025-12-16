# Victor - Library AI 

Victor is Ollama model (prompt) that was set up to be your library's circulation assistant. It was set up by Ms. Kristie Feguer(me!), a librarian.  
No cloud, no OpenAI/Claude/Gemini/xAI, no internet required after setup. Intended to help find items and answer general questions while prioritizing patron curiosity and privacy. Collection added using csv. Takes 5 minutes to load "brain" around 20,000 items. 

- Run on Llama 3.2 3B (or 1B) 
- Greets patrons on startup
- Uses RAG to pull your library's catalog information

Perfect for small libraries that want a local, private AI that is secure and answers questions in public setting.

## Quick start
```bash
ollama create victor -f Victor.ModelFile
ollama run victor
Howdy, Partner! Welcome to the library, how can I help you today?

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
=======
# victor-library-assistant
Victor is a 100% local, Ollama-powered LLM. No OpenAI/Gemini/xAI/Etc... No data leaves, intended for use without internet. Library and information assistant. Created with people and privacy as top priority. Cowboy quirks, unnecessary? Maybe...
>>>>>>> 2db21056df8e5baa9fe35c69ffe41f17344c9c35
