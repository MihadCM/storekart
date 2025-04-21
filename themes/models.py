from django.db import models

# Theme Model

class SiteSetting(models.Model):
    banner = models.ImageField(upload_to='media/site/')
    caption = models.TextField(max_length=200)
