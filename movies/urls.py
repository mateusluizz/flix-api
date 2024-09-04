from django.urls import path

from movies.views import MovieGenreCreateListView, MovieRetrieveUpdateDestroyView, MovieStatsView

urlpatterns = [
    path('', MovieGenreCreateListView.as_view(), name='movie-create-list'),
    path('<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    path('stats/', MovieStatsView.as_view(), name='movie-stats-view'),
]
