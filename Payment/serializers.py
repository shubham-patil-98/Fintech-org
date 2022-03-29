from rest_framework import serializers
from .models import Complaint,Detail,recharge

class ComplaintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Complaint
        fields='__all__'

class DetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Detail
        fields='__all__'

class RechargeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=recharge
        fields='__all__'