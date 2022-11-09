from django.urls import path
from . import views
from pages.views import ContactView

urlpatterns = [
    path('',ContactView.as_view(),name='index'),
]

