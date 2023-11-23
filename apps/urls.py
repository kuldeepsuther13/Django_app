from django.contrib import admin
from django.urls import path
from app_users.views import PatientListView,PatientDetailsView,TestsListView,TestsDetailsView,SampleListView,SampleDetailsView,DoctorListView,DoctorDetailsView,ResultListView,ResultDetailsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/patientlist/',PatientListView.as_view()),
    path('api/patientlist/<int:pk>',PatientDetailsView.as_view(),name='Patient1-detail'),
    path('api/testslist/',TestsListView.as_view()),
    path('api/testslist/<int:pk>',TestsDetailsView.as_view(),name='Test1-detail'),
    path('api/samplelist/',SampleListView.as_view()),
    path('api/samplelist/<int:pk>',SampleDetailsView.as_view(),name='Sample1-detail'),
    path('api/doctorlist/',DoctorListView.as_view()),
    path('api/doctorlist/<int:pk>',DoctorDetailsView.as_view(),name='Doctor1-detail'),
    path('api/resultlist/',ResultListView.as_view()),
    path('api/resultlist/<int:pk>',ResultDetailsView.as_view(),name='Result1-detail'),
]