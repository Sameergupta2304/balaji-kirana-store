from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('grocery', 'Grocery'),
        ('snacks', 'Snacks & Biscuits'),
        ('beverages', 'Beverages'),
        ('personal-care', 'Personal Care'),
        ('household', 'Household'),
        ('chocolates', 'Chocolates & Confectionery'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )
    available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name