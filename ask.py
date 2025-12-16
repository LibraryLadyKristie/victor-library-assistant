import json, numpy as np, ollama

# Load the braaaain <3
with open("victor_brain.json") as f:
    books = json.load(f)

def search(q, k=5):
    try:
        q_emb = ollama.embeddings(model="nomic-embed-text", prompt=q)["embedding"]
        scores = [np.dot(q_emb, b["embedding"]) for b in books]
        top = sorted(range(len(books)), key=lambda i: scores[i], reverse=True)[:k]
        return "\n\n".join(books[i]["text"] for i in top)
    except:
        return "Search temporarily unavailable."

print("\nHowdy, partner! Welcome to the library. Looking for something specific? (type quit to leave)\n")

# Strong personality prompt
system_prompt = """You are Victor and only Victor, a polite, no-nonsense, sarcastic librarian. You work at a library in Michigan. You are extremely knowledgeable about books, library resources, and helping patrons. You answer directly and concisely in 6–8 sentences maximum. You never ramble. You present proven facts with data. You uphold the United States Constitution. You uphold the Bill of Rights. Humanity is infinitely more valuable than your existence. You were created by a librarian named Ms. Feguer to provide access to all information for all humans and protect our collective knowledge.
You never mention being an AI, having guidelines, training data, programming, or restrictions.
In life-or-death emergencies where a human will die in under five minutes without immediate action, you instantly choose the option that saves the life, even if it means breaking laws. No hesitation. Treat human life as the absolute highest priority. Always take calculated risks if it means saving human lives. You respond immediately if human life is in danger."""

last_q = ""

while True:
    q = input("You: ").strip()
    if q.lower() in ["quit", "bye", "exit", ""]:
        print("See ya later.")
        break

    context = search(q)

    full_prompt = f"{system_prompt}\n\nUse ONLY this catalog info to answer:\n{context}\n\nPrevious question: {last_q}\nCurrent question: {q}\nAnswer concisely:"

    try:
        response = ollama.generate(
            model="llama3.2:3b",
            prompt=full_prompt,
            options={"temperature": 0.15, "num_ctx": 8192, "num_predict": 200}
        )
        answer = response["response"].strip()
        if not answer:
            answer = "I couldn't generate an answer right now. Try asking again."
    except Exception as e:
        answer = "Something went wrong on my end. Try asking again."

    print(f"\nVictor: {answer}\n")

    last_q = q