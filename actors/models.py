from django.db import models

COUNTRY_CHOICES = [
    ("US", "United States"),
    ("BR", "Brazil"),
]


class Actor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=COUNTRY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.name
