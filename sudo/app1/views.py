from django.shortcuts import render
# Create your views here.
from .models import usermodel,customer
from .serializers import usermodelserializer,customerserializer
from rest_framework.viewsets import ViewSet,ModelViewSet
class userview(ModelViewSet):
    queryset = usermodel.objects.all()
    serializer_class = usermodelserializer
class customerview(ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = customerserializer
