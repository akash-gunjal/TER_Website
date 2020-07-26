
from django.urls import path
from .views import (
    TransactionListView,
    TransactionDetailView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDeleteView,
    UserTransactionListView
)

from . import views

urlpatterns = [
    path('', TransactionListView.as_view(), name='Account-Dashboard' ),
    path('user/<str:username>/', UserTransactionListView.as_view(), name='User-Transaction' ),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='Transaction-Detail' ),
    path('transaction/new/', TransactionCreateView.as_view(), name='Transaction-Add' ),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='Transaction-Update' ),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='Transaction-Delete' ),

]
