from django.db import models
# import uuid

class Author(models.Model):
    name = models.CharField(max_length=100)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

class Paper(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    id = models.CharField(max_length=100,primary_key=True)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    publication_date = models.DateField()


    def __str__(self):
        return self.title
