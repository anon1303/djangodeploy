from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # path('api/token/', views.TokenList.as_view()),
    path('api/user/', views.UserList.as_view()),
    path('api/user/<int:pk>/', views.UserDetail.as_view()),
    path('api/superadmin/', views.SuperadminList.as_view()),
    path('api/superadmin/<int:pk>/', views.SuperadminDetail.as_view()),
    path('api/subadmin/', views.SubadminList.as_view()),
    path('api/subadmin/<int:pk>/', views.SubadminDetail.as_view()),
    path('api/borrower/', views.BorrowerList.as_view()),
    path('api/borrower/<int:pk>/', views.BorrowerDetail.as_view()),
    path('api/facility/', views.FacilityList.as_view()),
    path('api/facility/<int:pk>/', views.FacilityDetail.as_view()),
    path('api/equipment/', views.EquipmentList.as_view()),
    path('api/equipment/<int:pk>/', views.EquipmentDetail.as_view()),
    path('api/reservation/', views.ReservationList.as_view()),
    path('api/reservation/<int:pk>/', views.ReservationDetail.as_view()),
    path('api/schedule/', views.ScheduleList.as_view()),
    path('api/schedule/<int:pk>', views.ScheduleDetail.as_view()),
    path('api/logs/', views.LogsList.as_view()),
    path('api/logs/<int:pk>', views.LogsDetail.as_view())
    ]

urlpatterns = format_suffix_patterns(urlpatterns)