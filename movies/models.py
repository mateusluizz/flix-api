from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(
        'genres.Genre',
        on_delete=models.PROTECT,
        related_name='movies'
    )
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(
        'actors.Actor',
        related_name='movies'
    )
    resume = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
