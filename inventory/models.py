from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=50)
    tag_no = models.PositiveIntegerField(default=0)
    curr_owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name="current_products")
    prev_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="previous_products")
    is_available = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name} - {'Available' if self.is_available else 'Unavailable'}"