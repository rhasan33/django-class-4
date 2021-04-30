from django.db import models
from simple_history.models import HistoricalRecords

from base.models import BaseModel


class Wallet(BaseModel):
    amount = models.FloatField()
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)
    history = HistoricalRecords(
        history_change_reason_field=models.TextField(null=True)
    )

    class Meta:
        db_table = 'wallets'

    def __str__(self):
        return self.user.username
