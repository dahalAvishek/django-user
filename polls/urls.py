from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<intLquestion_id>/", views.detail, name="detail"),
    path("<intLquestion_id>/results/", views.results, name="result"),
    path("<intLquestion_id>/vote/", views.vote, name="vote"),
    
    
    
]