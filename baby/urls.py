from django.urls import path
from . import views

urlpatterns = [
    path('', views.CurrentDayViews.as_view(), name='home'),
    path('history/', views.HistoryView.as_view()),
    path('baby_weight/', views.BabyWeightView.as_view()),
    path('delete/', views.delete),
    path('save/', views.save)
]
