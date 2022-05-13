from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)
    # optional name for front-end
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__ (self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    # allowing to be null in the database and blank in forms on the front-end, if category is deleted products will have value of null for category key
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # every product require name description and price and rest is optional

    def __str__(self):
        return self.name