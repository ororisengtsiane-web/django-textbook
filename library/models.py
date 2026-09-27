from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
    )
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(
        max_length=50,
        default="South Africa"
    )

    def short_bio(self):
        if self.bio:
          return self.bio[:50] + "..."
        return "No biography available."

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_description(self):
        return f"{self.name} is an author from {self.country}."

class AuthorProfile(models.Model):
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE
    )
    bio = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        null=True,
        blank=True
    )

    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

class Meta:
     ordering = ['title']