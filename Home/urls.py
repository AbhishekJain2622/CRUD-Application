from django.urls import path
from Home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('show/',views.show,name='show'),
    path('send/',views.send,name='send'),
    path('delete/',views.delete,name='delete'),
    path('edit/',views.edit,name='edit'),
    path('RecordEdited/',views.RecordEdited,name='recordedited'),
]