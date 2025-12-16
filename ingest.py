import csv, json, os
import ollama

print("Building Victor's brain from catalog.csv...")

if not os.path.exists("catalog.csv"):
    print("ERROR: Put your catalog.csv file in this folder first!")
    input("Press Enter to close...")
    exit()

books = []

with open("catalog.csv", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Figure out the item TYPE based on call number
        call = row.get('call_number', '').strip().upper()
        if call.startswith('DVD') or call.startswith('J DVD') or call.startswith('AV'):
            item_type = "DVD / Movie"
        elif call.startswith('J ') or call.startswith('E ') or call.startswith('PIC'):
            item_type = "Children's Book / Picture Book"
        elif call.startswith('FIC') or call.startswith('F '):
            item_type = "Adult Fiction"
        elif call.startswith('YA'):
            item_type = "Young Adult / Teen Book"
        else:
            item_type = "Book"

               # Raw title
        raw_title = row.get('title', '').strip()

        # Aggressive cleaning
        import re
        clean_title = re.split(r'["\.\d]{10,}|videodisc|min\.', raw_title, maxsplit=1)[0].strip() 
        clean_title = re.sub(r' - 1 DVD$', '', clean_title).strip()  # remove trailing format

        # Remove leading A/The/An
        normalized_title = clean_title
        for prefix in ["A ", "The ", "An "]:
            if normalized_title.lower().startswith(prefix.lower()):
                normalized_title = normalized_title[len(prefix):].strip()

        # Use clean_title for display, normalized for search
        text = f"Type: {item_type}\n" \
               f"Title: {clean_title}\n" \
               f"Search Title: {normalized_title}\n" \
               f"Author: {row.get('author','')}\n" \
               f"Call Number: {row.get('call_number','')}\n" \
               f"Location: {row.get('location','')}\n" \
               f"Status: {row.get('status','')}"

        # Get the embedding from Ollama
        embedding = ollama.embeddings(model="nomic-embed-text", prompt=text)["embedding"]

        books.append({"text": text, "embedding": embedding})

# Save the brain <3
with open("victor_brain.json", "w", encoding="utf-8") as f:
    json.dump(books, f)

print(f"Success! Victor now knows {len(books)} items with normalized titles for perfect matching.")
input("Press Enter to close...")