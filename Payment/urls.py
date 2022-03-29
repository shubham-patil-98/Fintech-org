from django.urls import path,include
from rest_framework import routers
from .import views
# from .models import Domain

routers=routers.DefaultRouter()
routers.register(r'Complaint',views.ComplaintViewset)
routers.register(r'Detail',views.DetailViewset)
routers.register(r'recharge',views.RechargeViewset)

urlpatterns = [
    path('api_auth', include('rest_framework.urls',namespace='rest_framework')),
    path('',include(routers.urls)),
]
