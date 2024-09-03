from django.db.models import Avg
from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

    def validate_release_date(self, value):
        if value.year < 1920:
            raise serializers.ValidationError('The release date cant be lower then 1920')
        return value

    def validate_resume(self, value):
        if len(value) > 400:
            raise serializers.ValidationError('Resume cant have more than 400 characters')
        return value
