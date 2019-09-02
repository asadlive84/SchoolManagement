import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save


class Account(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    account_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    balance = models.FloatField("Balance")

    def __str__(self):
        return f"{self.author} - {self.account_name}"


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    balance = models.FloatField(null=True, blank=True)
    notes = models.TextField(max_length=200)
    debit = models.FloatField()
    credit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.transaction_id

    class Meta:
        ordering = ['-created_at']


@receiver(post_save, sender=Transaction)
def transaction_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.account.balance = instance.account.balance + instance.credit - instance.debit
        instance.account.save()


@receiver(post_save, sender=Transaction)
def transaction_uuid_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.transaction_id = "FHS" + str(uuid.uuid4().hex[:8])
        instance.save()


@receiver(post_save, sender=Transaction)
def transaction_balance_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.balance = instance.account.balance
        instance.save()
