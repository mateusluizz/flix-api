from django.contrib import admin
from django.urls import include, path

api_v1 = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_v1}authentication/', include('authentication.urls')),
    path(f'{api_v1}genres/', include('genres.urls')),
    path(f'{api_v1}actors/', include('actors.urls')),
    path(f'{api_v1}movies/', include('movies.urls')),
    path(f'{api_v1}reviews/', include('reviews.urls')),
]
