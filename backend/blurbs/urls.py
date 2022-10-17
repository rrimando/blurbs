from django.urls import path
from blurbs import views

# define the urls
urlpatterns = [
    path("blurbs/", views.blurbs),
    path("blurbs/<int:pk>/", views.blurb_details),
]
