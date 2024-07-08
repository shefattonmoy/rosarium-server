from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        customer_id = self.request.query_params.get('customer_id')
        if customer_id:
            queryset = queryset.filter(customer_id = customer_id)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        order = serializer.instance

        self.send_order_received_email(order)

        product = order.all_products
        product.quantity -= 1
        product.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def send_order_received_email(self, order):
        subject = 'Order Received'
        message = render_to_string('admin_received_order_email.html', {
            'customer': order.customer.user.first_name,
            'product': order.all_products.user.first_name,
            'order': order,
        })
        recipient_list = [order.customer.user.email]
        email = EmailMultiAlternatives(subject, message, 'shefathossain7@gmail.com', recipient_list)
        email.attach_alternative(message, "text/html")
        email.send()