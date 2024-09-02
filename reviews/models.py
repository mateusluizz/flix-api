from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(
        'movies.Movie',
        on_delete=models.PROTECT,
        related_name='reviews',
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Review cant be lower than 0 stars'),
            MaxValueValidator(5, 'Review cant be higher than 5 stars'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.movie
