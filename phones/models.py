from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=400)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name
