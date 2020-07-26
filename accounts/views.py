
from .models import Transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
     ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView
)

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'
    ordering= ['-date_posted']
    paginate_by = 10

class UserTransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'accounts/user_transactions.html'
    context_object_name = 'transactions'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Transaction.objects.filter(responsible = user).order_by('-date_posted')

class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'accounts/transaction_detail.html'

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['Type', 'Expenditure_on', 'Income_Source','Amount']
    def form_valid(self, form):
        form.instance.responsible = self.request.user
        return super().form_valid(form)

class TransactionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transaction
    fields = ['Type', 'Expenditure_on', 'Income_Source','Amount']

    def form_valid(self, form):
        form.instance.responsible = self.request.user
        return super().form_valid(form)

    def test_func(self):
        transaction = self.get_object()
        if self.request.user ==transaction.responsible:
            return True
        else:
            return False

class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    success_url='/'
    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.responsible:
            return True
        else:
            return False
