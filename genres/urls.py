from django.urls import path

from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', GenreCreateListView.as_view(), name='genres-create-list'),
    path('<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-detail-view'),
]
