from django.db import models

# Product Model

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = (( LIVE, 'Live'), (DELETE, 'Delete'))

    title = models.CharField(max_length=200)
    price = models.FloatField()
    desciption = models.TextField()
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField(default=0)
    
    delete_status = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title 

