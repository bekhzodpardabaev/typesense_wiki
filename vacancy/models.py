from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    search_tags = ArrayField(models.CharField(max_length=100), blank=True, null=True)

    def __str__(self):
        return self.name


class CategorySynonyms(models.Model):
    class TypeChoices(models.TextChoices):
        one_way = "one_way", "One way"
        multi_way = "multi_way", "Multi way"

    id = models.CharField(max_length=100, primary_key=True, unique=True)
    type = models.CharField(max_length=100, choices=TypeChoices.choices)
    root_word = models.CharField(max_length=100, null=True, blank=True)
    words = ArrayField(models.CharField(max_length=100))
    is_active = models.BooleanField(default=False)

    def construct_typesense_synonyms(self):
        synonym = {
            "synonyms": list(self.words),
        }
        if self.type == self.TypeChoices.one_way:
            synonym["root"] = self.root_word

        return synonym


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    salary = models.IntegerField()
    location_lat = models.FloatField(null=True, blank=True)
    location_lon = models.FloatField(null=True, blank=True)
    search_tags = ArrayField(models.CharField(max_length=100), blank=True, null=True)

    def __str__(self):
        return self.title
