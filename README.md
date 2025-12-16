# Victor - Library AI 

Victor is Ollama model that was set up to be your library's circulation assistant. This assistant is intended for small libraries that want AI that can search and access the catalog, give locations, and answer questions for patrons. It was set up by Ms. Kristie Feguer(me!), a librarian.  
No cloud, no OpenAI/Claude/Gemini/xAI, no internet required after setup. Intended to help find items and answer general questions while prioritizing patron curiosity and ensuring their privacy. 

- Run on Llama 3.2 3B (or 1B) 
- Greets patrons on startup
- Family-Friendly 
- Remembers Conversation
- Cowboy Quirks
- Distinguishes Item Types (DVD, picture book, Young Adult, etc...)
- 99% Accurate Answers

How does it work? You export your library's catalog as a CSV. ingest.py reads the csv and builds the "brainnnn" (json file) using embeddings. 
asky.py searches the brain for the patron's questions, pulls, and feeds them to the LLM.

Perfect for small libraries that want a local, private AI that is secure and answers questions in public setting. It is easy to update, local, and can run offline after initial setup. 

Requirements: 
- Windows, Mac, Linux computer/OS
- Ollama installation
- Python 3
