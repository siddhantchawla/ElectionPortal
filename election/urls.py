from django.urls import path

from . import views

urlpatterns = [

	path('',views.index),
	path('startSession/',views.startSession),
	path('changestatus/<int:session_id>/',views.changeStatus),
	# path('fillNomination/',views.fillNomination),
	
]