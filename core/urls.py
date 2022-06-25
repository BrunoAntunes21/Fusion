from django.urls import path
from .views import IndexView,NowtView,ServerErrorView
urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('404/',NowtView.as_view(),name='404'),
    path('500/',ServerErrorView.as_view(),name='500')
]