from django.urls import path

from genres.views import genre_view

urlpatterns = [
    path('', genre_view, name='genres-list')
]
