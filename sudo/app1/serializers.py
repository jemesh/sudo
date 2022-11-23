from rest_framework import serializers
from .models import usermodel,customer
class usermodelserializer(serializers.ModelSerializer):
    class Meta:
        model=usermodel
        fields="__all__"
class customerserializer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields="__all__"