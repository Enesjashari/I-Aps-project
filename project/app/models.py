from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Paper(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    publication_date = models.DateField()


    def __str__(self):
        return self.title
