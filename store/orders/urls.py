from django.urls import path

from orders.views import OrderCreateView, SuccessTemplateView, CancelTemplateView, OrderListView, OrderDetailView

app_name = 'orders'

urlpatterns = [
    path('order-create', OrderCreateView.as_view(), name = 'order_create'),
    path('', OrderListView.as_view(), name = 'orders_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name = 'order'),
    path('order-canceled', CancelTemplateView.as_view(), name = 'order_canceled'),
    path('order-canceled', OrderListView.as_view(), name = 'order_canceled'),
]
