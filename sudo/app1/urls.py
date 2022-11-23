from django.urls import path,include
from .views import userview,customerview
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('userview',userview,basename='user')
router.register('customerview',customerview,basename='customer')
urlpatterns=[
    path('',include(router.urls))
]