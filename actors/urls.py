from django.urls import path

from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ActorCreateListView.as_view(), name='actor-create-list'),
    path('<int:pk>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-detail-view'),
]
