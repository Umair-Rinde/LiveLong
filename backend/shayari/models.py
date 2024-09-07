from django.db import models
from portal.models import BaseModel

class Category (BaseModel):
    name= models.CharField(max_length=20,unique=True, blank=False)
    

class Shayaries (BaseModel):
    sher= models.TextField(unique= True, blank=False)
    caption= models.CharField(max_length=100, blank=True)
    is_featured= models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="ShayariImage/", default="ShayariImage/default.png"
    )
    category= models.ForeignKey(Category,on_delete=models.SET_NULL, related_name='shayari')