from django.urls import path, include
from . import views
from .views import Register, AddExcursion

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('excursions', views.excursions, name='excursions'),
    path('excursions/<int:pk>', views.ExcursionDetailView.as_view(), name='excursions-detail'),
    path('excursion/add', AddExcursion.as_view(), name='excursion-add'),
    path('account/register/', Register.as_view(), name='register'),
    path('contacts', views.contacts, name='contacts'),


    #path('profile',  views.profile_view, name='profile'),
]
