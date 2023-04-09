"""Songs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Songs.rest_API import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('L1/songs/', views.SongView),
    path('L1/songs/<int:id>/', views.song_detail),

    path('L1/albums/', views.AlbumView),
    path('L1/albums/<int:id>/', views.album_detail),

    path('L1/singers/<int:id>/', views.singer_detail),
    path('L1/singers/', views.SingerView),
    path('L1/many/', views.AlbumSongView),
    path('L1/stats/', views.Statistics.statistics_albums)

]


urlpatterns = format_suffix_patterns(urlpatterns)
