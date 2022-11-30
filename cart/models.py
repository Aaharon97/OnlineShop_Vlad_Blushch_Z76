from django.db import models


class Cart(models.Model):
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    product = models.ForeignKey('catalog.Book', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product
