import json

from models import Author, Quote

# Зчитайте дані з файлів
with open("authors.json", "r", encoding="utf-8") as file:
    authors_data = json.load(file)

with open("quotes.json", "r", encoding="utf-8") as file:
    quotes_data = json.load(file)

# Збереження авторів у колекції authors
for author_info in authors_data:
    author = Author(**author_info)
    author.save()

# Збереження цитат у колекції quotes
for quote_info in quotes_data:
    author_name = quote_info["author"]
    author = Author.objects(fullname=author_name).first()
    if author:
        quote_info["author"] = author
        quote = Quote(**quote_info)
        quote.save()
    else:
        print(f"Author '{author_name}' not found for quote.")

print("Data loaded successfully.")