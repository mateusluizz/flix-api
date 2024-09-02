from django.urls import path

from genres.views import GenreCreateListView, genre_detail_view

urlpatterns = [
    path('', GenreCreateListView.as_view(), name='genres-create-list'),
    path('<int:pk>/', genre_detail_view, name='genre-detail-view'),
]
