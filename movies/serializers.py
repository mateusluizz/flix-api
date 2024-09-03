from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('The release date cant be lower then 1990')
        return value

    def validate_resume(self, value):
        if len(value.resume) > 200:
            raise serializers.ValidationError('Resume cant have more than 200 characters')
