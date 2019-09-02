from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from officeaccounts.models import Account, Transaction
from users.models import CustomUser
from django.views import generic
from officeaccounts.forms import TransactionCreateForm


class AccountListView(LoginRequiredMixin, generic.ListView):
    model = Account
    template_name = 'accounts/index.html'


class TransactionListView(LoginRequiredMixin, generic.ListView):
    model = Transaction
    template_name = 'accounts/transaction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_list'] = Account.objects.get(author_id=self.request.user)
        return context


class TransactionCreateView(LoginRequiredMixin,generic.CreateView):
    model = Transaction
    # form_class = TransactionCreateForm
    template_name = 'accounts/transaction_create.html'
    fields = ('account', 'credit', 'debit', 'notes',)

    success_url = '/accounts/t/'
