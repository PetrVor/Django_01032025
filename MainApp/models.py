from django.db import models

class Color(models.Model):
   name=models.CharField(max_length=32)

   def __repr__(self):
      return f"Color({self.name})"

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description = models.TextField(max_length=200, default='Base item description') 
   colors = models.ManyToManyField(to=Color)

   def __repr__(self):
      return f"Item({self.name})"

