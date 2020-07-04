from django.urls import path

from .views import TourList, TourDetail, DestinationList, DestinationDetail

urlpatterns = [
    path('<int:pk>/', TourDetail.as_view()),
    path('tourpackages', TourList.as_view()),
    path('<int:pk>/', DestinationDetail.as_view()),
    path('destination', DestinationList.as_view())

]
