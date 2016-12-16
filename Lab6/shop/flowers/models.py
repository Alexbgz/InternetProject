from django.db import models
from django.utils import timezone

class Catalog(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    product = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'catalog'

