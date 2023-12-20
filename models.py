from mongoengine import Document, connect, StringField, DateTimeField, ReferenceField, ListField

# Підключення до бази даних
connect("my_mongo_container", host="localhost")


# Модель для колекції authors
class Author(Document):
    fullname = StringField(required=True, max_length=100)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField()


# Модель для колекції quotes
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)
