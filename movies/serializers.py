from django.db.models import Avg

from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1920:
            raise serializers.ValidationError('The release date cant be lower then 1920')
        return value

    def validate_resume(self, value):
        if len(value) > 400:
            raise serializers.ValidationError('Resume cant have more than 400 characters')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movie_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    avg_stars = serializers.FloatField()
