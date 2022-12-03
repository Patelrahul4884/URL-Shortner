from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import URL
from .serializers import URLShortnerSerializer
from django.views import View
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class URLShortnerListAPIView(ListAPIView):
    queryset=URL.objects.all()
    serializer_class=URLShortnerSerializer

class URLShortnerCreateAPIView(CreateAPIView):
    serializer_class=URLShortnerSerializer

class RedirectURL(View):
    def get(self,request,shorten_url,*args,**kwargs):
        shorten_url = settings.HOST_URL+'/'+self.kwargs['shorten_url']
        try:
            redirect_url = URL.objects.filter(shorten_url=shorten_url).first().original_url
        except:
            return Response(data={"status": status.HTTP_400_BAD_REQUEST,
            "message": "Something went wrong."},)
        return redirect(redirect_url)
