from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_jpg(value):
    ext = os.path.splitext(value.name)[1]  # file extension
    valid_extensions = ['.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Only .jpg and .jpeg files are allowed.')

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/", validators=[validate_jpg], blank=True, null=True)

    def __str__(self):
        return self.name
