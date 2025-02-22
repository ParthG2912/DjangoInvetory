from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=50)
    tag_no = models.IntegerField(default=0)
    curr_owner = models.CharField(max_length=50)
    prev_owner = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)