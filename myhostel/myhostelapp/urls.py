from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('activities/',views.activities,name='activities'),
    path('admission/',views.admission,name='admission'),
    path('notice/',views.notice,name='notice'),
    path('profile/',views.profile,name='profile'),
    path('staffs/',views.Staffs,name='staffs')
]
