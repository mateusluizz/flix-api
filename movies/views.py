from core.permissions import GlobalDefaultPermission
from movies.models import Movie
from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from movies.serializers import MovieListDetailSerializer, MovieSerializer, MovieStatsSerializer
from django.db.models import Count, Avg
from reviews.models import Review


class MovieGenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.all().count()
        avg_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            "total_movies": total_movies,
            "movie_by_genre": movies_by_genre,
            "total_reviews": total_reviews,
            "avg_stars": round(avg_stars, 1) if avg_stars else 0,
        }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK,
        )
