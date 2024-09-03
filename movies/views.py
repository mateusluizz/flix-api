from core.permissions import GlobalDefaultPermission
from movies.models import Movie
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.serializers import MovieSerializer


class MovieGenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
