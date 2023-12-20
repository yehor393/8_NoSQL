from mongoengine import Q

from models import Author, Quote

while True:
    command = input("Команда: ")

    if command.startswith("name:"):
        author_name = command[len("name:"):].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.quote)
        else:
            print("Автор не знайдений.")

    elif command.startswith("tag:"):
        tag = command[len("tag:"):].strip()
        quotes = Quote.objects(tags=tag)
        for quote in quotes:
            print(quote.quote)

    elif command.startswith("tags:"):
        tags = command[len("tags:"):].strip().split(",")
        quotes = Quote.objects(Q(tags__in=tags))
        for quote in quotes:
            print(quote.quote)

    elif command == "exit":
        break

    else:
        print("Невірна команда.")
