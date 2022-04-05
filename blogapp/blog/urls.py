from django.urls import path
from . import views


urlpatterns = [
    path('', views.SampleAPI.as_view(), name='test'),
]
