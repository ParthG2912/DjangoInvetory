from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=50)
    tag_no = models.PositiveIntegerField(default=0)
    curr_owner = models.CharField(max_length=50, default="H/W room")
    prev_owner = models.CharField(max_length=50, default="H/W room", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (Tag: {self.tag_number})"