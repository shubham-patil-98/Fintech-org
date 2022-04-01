from rest_framework import viewsets
from .serializers import ComplaintSerializer,DetailSerializer,RechargeSerializer
from .models import Complaint,Detail,recharge
from .mypagination import MyPageNumberPagination

class ComplaintViewset(viewsets.ModelViewSet):
    queryset=Complaint.objects.all().order_by('complaints')
    serializer_class=ComplaintSerializer
    pagination_class=MyPageNumberPagination
    
class DetailViewset(viewsets.ModelViewSet):
    queryset=Detail.objects.all().order_by('details')
    serializer_class=DetailSerializer
    pagination_class=MyPageNumberPagination

class RechargeViewset(viewsets.ModelViewSet):
    queryset=recharge.objects.all().order_by('status')
    serializer_class=RechargeSerializer
    pagination_class=MyPageNumberPagination