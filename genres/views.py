import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre
from rest_framework import generics
from .serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(
            data, safe=False
        )
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            data, safe=False
        )
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': 'Gender removed sucessfully'},
            status=204,
        )
