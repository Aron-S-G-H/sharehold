from django.urls import path
from .views import index, ShareholderListView

urlpatterns = [
    path('', index, name='index'),
    path('shareholders/', ShareholderListView.as_view(), name='shareholder-list'),
]
