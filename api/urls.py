from django.urls import path
from api.views import URLShortnerListAPIView, URLShortnerCreateAPIView, RedirectURL

urlpatterns = [
    path('',URLShortnerListAPIView.as_view(),name='list_URL'),
    path('create/',URLShortnerCreateAPIView.as_view(),name='create_URL'),
]