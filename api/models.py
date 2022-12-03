from django.db import models
import string
from random import choice
from django.conf import settings

# Create your models here.
class URL(models.Model):
    original_url = models.URLField()
    shorten_url = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)


    def short_url(self):
        while True:
            random_string=''.join(choice(string.ascii_letters+string.digits) for _ in range(6))
            new_url=settings.HOST_URL+'/'+random_string

            if not URL.objects.filter(shorten_url=new_url):
                break
        return new_url

    def save(self,*args,**kwargs):
        if not self.shorten_url:
            new_url = self.short_url()
            self.shorten_url=new_url
        return super().save(*args,**kwargs)