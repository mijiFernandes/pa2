from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    #Example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    #Example: /photo/album/
    path('album', views.AlbumLV.as_view(), name='album_list'),

    #Example: /photo/album/int/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    #Example: /photo/photo/int/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),

    #Example: /photo/album/add/
    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),
    #Example: /photo/album/change/
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),
    #Example: /photo/album/int/update/
    path('album/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album_update'),
    #Example: /photo/album/int/delete/
    path('album/<int:pk>/delete/', views.AlbumDelV.as_view(), name='album_delete'),

    # Example: /photo/photo/add/
    path('photo/add/', views.PhotoCV.as_view(), name='photo_add'),
    # Example: /photo/photo/change/
    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'),
    # Example: /photo/photo/int/update/
    path('photo/<int:pk>/update/', views.PhotoUV.as_view(), name='photo_update'),
    # Example: /photo/photo/int/delete/
    path('photo/<int:pk>/delete/', views.PhotoDelV.as_view(), name='photo_delete'),
]
