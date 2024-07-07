from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('list', views.AllProductViewset)
router.register('color', views.ColorViewset)
router.register('category', views.CategoryViewset)
router.register('receiving_time', views.ReceivingTimeViewset)
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
]