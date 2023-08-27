import uuid
from django.db import models
from user.models import Account
from market.models import Market


class ProAccountOrder(models.Model):
    user = models.ForeignKey(Account,on_delete = models.CASCADE)
    price = models.PositiveIntegerField()
    transaction_id = models.UUIDField(uuid.uuid4(),primary_key=True,editable=False)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.phone}'


class MarketOrder(models.Model):
    market = models.ForeignKey(Market,on_delete=models.CASCADE)
    client = models.ForeignKey(Account,on_delete=models.CASCADE)
    transaction_id = models.UUIDField(uuid.uuid4(),primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.market.name

