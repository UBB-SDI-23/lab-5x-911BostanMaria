from django.db.models import Avg, Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Songs.rest_API.models import Song, Album, Singer, AlbumSong
from Songs.rest_API.serializers import SongSerializer, AlbumSerializer, SingerSerializer, AlbumSongSerializer, StatisticsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def SongView(request):
    # get all songs
    # serialize them
    # return json
    if request.method == 'GET':
        playlist = Song.objects.all()
        serializer = SongSerializer(playlist, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, id):
    try:
        song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def AlbumView(request):
    # get all albums
    # serialize them
    # return json
    if request.method == 'GET':
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, id):
    try:
        album = Album.objects.get(pk=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def SingerView(request):
    # get all singers
    # serialize them
    # return json
    if request.method == 'GET':
        singer = Singer.objects.all()
        serializer = SingerSerializer(singer, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def singer_detail(request, id):
    try:
        singer = Singer.objects.get(pk=id)
    except Singer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SingerSerializer(singer)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SingerSerializer(singer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        singer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def AlbumSongView(request, format=None):
    if request.method == 'GET':
        albumsong = AlbumSong.objects.all()
        serializer = AlbumSongSerializer(albumsong, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AlbumSongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def AlbumSongDetail(request, id):

    try:
        albumsong = AlbumSong.objects.get(pk=id)
    except albumsong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSongSerializer(albumsong)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlbumSongSerializer(albumsong, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        albumsong.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Statistics(APIView):
    @api_view(['GET'])
    def statistics_albums(request):
        # songs ordered by the average of their albums no_of_songs
        statistics = Album.objects.annotate(
            avg=Avg('no_of_songs'),
            song_count=Count('albumsong')
        ).order_by('-avg')

        serializer = StatisticsSerializer(statistics, many=True)
        return Response(serializer.data)
