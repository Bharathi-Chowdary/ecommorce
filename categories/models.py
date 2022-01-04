from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_img = models.ImageField(upload_to='photos/categories', blank = True)
    
    
    class Meta:
  #      ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
        #reverse will take the name of the category_urls
        return reverse('products_by_category', args = [self.url])
    def __str__(self):
        return self.name