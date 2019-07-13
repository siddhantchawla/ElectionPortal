from django.urls import path

from . import views

urlpatterns = [

	path('',views.index),
	path('startSession/',views.startSession),
	path('changestatus/<int:session_id>/',views.changeStatus),
	path('fillNomination/',views.fillNomination),
	path('apply/<str:sessionid>/',views.apply),
	path('applied/',views.applied),
	path('activeSessions/',views.activeSessions),
	path('vote/<int:session_id>/',views.vote),
	path('vote/<int:session_id>/<int:userid>/',views.addVote),
	
]