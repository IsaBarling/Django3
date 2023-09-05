from django.urls import path
from . import views


urlpatterns = [
    path('', views.general, name='general'),
    path('fakes/', views.fake_datas, name='fakes'),
    path('lu/', views.list_users, name='list_users'),
    path('lp/', views.list_products, name='list_products'),
    path('lo/', views.list_orders, name='list_orders'),
    path('basket/<int:uid>/', views.basket, name='basket'),
    path('us_pr/<int:uid>/', views.us_products, name='us_pr'),
    path('us_pr_tm/<int:uid>/<int:dif_day>/', views.us_products_time, name='us_pr_tm'),
]
