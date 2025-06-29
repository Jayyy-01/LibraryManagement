from django.db import models

class Author(models.Model):
    auth_name = models.CharField(max_length=100)

    def __str__(self):
        return self.auth_name
    class Meta:
        verbose_name = 'Authors'
        verbose_name_plural = 'Authors'

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    book_price = models.IntegerField()

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Books'
        verbose_name_plural = 'Books'



