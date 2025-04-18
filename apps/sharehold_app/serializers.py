from rest_framework import serializers
from .models import Shareholdershistory

class ShareholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shareholdershistory
        fields = ['symbol', 'shareholder_percentage', 'shareholder_name']