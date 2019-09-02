from django.urls import path, re_path
from officeaccounts import views

app_name="office_accounts"

urlpatterns = [
    path('', views.AccountListView.as_view(), name="account"),
    path('t/',views.TransactionListView.as_view(), name='transaction_list'),
    path('t_create/', views.TransactionCreateView.as_view(), name="transaction_create_view"),
]