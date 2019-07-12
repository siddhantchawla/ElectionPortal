from django.urls import path

from . import views

urlpatterns = [

	path('',views.index),
	path('startSession/',views.startSession),
	path('fillNomination/',views.fillNomination),
	
]