# serializers.py
from rest_framework import serializers
from .models import Setting

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ['setting_no', 'description', 'sh_desc', 'lastuser']