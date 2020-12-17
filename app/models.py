from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField("name", max_length=255, blank = True, null = True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.name