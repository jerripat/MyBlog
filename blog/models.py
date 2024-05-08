from django.db import models
from django.core.validators import MinLengthValidator
class Tag(models.Model):
    caption = models.CharField(max_length=10)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image_name= models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

# Create your models here.
