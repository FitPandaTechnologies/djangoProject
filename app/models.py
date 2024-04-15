from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    authors = models.ManyToManyField(Author)
    publish_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Stock(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price_excl_vat = models.DecimalField(max_digits=6, decimal_places=2)
    vat_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    @property
    def price_incl_vat(self):
        price_after_discount = self.price_excl_vat * (1 - self.discount / 100)
        return price_after_discount * (1 + self.vat_percentage / 100)

    def __str__(self):
        return f"Stock for {self.book.title}"
