import uuid

from django.db import models

from base.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100)
    sku = models.UUIDField(default=uuid.uuid4, unique=True)
    price = models.FloatField()
    shop = models.ForeignKey('shop.Shop', on_delete=models.PROTECT)
    is_active = models.BooleanField()
    meta = models.JSONField()

    class Meta:
        ordering = ['-created_at']
        db_table = 'products'

    def __str__(self):
        return self.name
