from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Studentdbs(models.Model):

    category = models.ForeignKey(Category ,on_delete=models.DO_NOTHING, related_name='products')
    contact_no = models.CharField(max_length=11,blank=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    email_address = models.CharField(max_length=200, db_index=True)
    # image = ResizedImageField(size=[300, 300], upload_to='products/%Y/%m/%d', blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    machine_learning = models.DecimalField(max_digits=10, decimal_places=2)
    web_tech= models.DecimalField(max_digits=10, decimal_places=2)
    unix = models.DecimalField(max_digits=10, decimal_places=2)
    software_architecture= models.DecimalField(max_digits=10, decimal_places=2)
    information_management_system = models.DecimalField(max_digits=10, decimal_places=2)

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    #
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.id, self.slug])
