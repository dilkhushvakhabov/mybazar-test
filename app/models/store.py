from django.db import models

from .base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name
