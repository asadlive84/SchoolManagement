from django.forms import models
from officeaccounts.models import Transaction
from users.models import CustomUser
from django import forms


class TransactionCreateForm(models.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'debit', 'credit', 'notes',)

    def __init__(self, *args, **kwargs):
        account = kwargs.pop('account', '')

        super(TransactionCreateForm, self).__init__(*args, **kwargs)
        self.fields['account'] = forms.ModelChoiceField(queryset=CustomUser.objects.get(username=account))
