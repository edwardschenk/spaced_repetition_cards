from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns =  [
    path('', views.index, name='index'),
    path('makeset/', views.create_card_set, name='makeset'),
    path('<str:set_name>/', views.card_set, name='viewset'),
    path('<str:set_name>/makecards/', views.create_cards, name='makecards'),
    path('<str:set_name>/flashcards/', views.flashcards, name='flashcards'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)