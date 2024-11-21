from django.contrib import admin
from django.urls import path
# from .views import *
from demo import views

urlpatterns = [
    # path('', home),
    # path('add-student/',add_student),
    # path('update-student/<int:id>/',update_student),
    # path('delete-student/<int:id>/',delete_student)
    
    path('', views.StudentList.as_view()),
    path('add-student/',views.StudentAdd.as_view()),
    path('update-student/<int:pk>/',views.StudentUpdate.as_view()),
    path('delete-student/<int:pk>/',views.StudentDelete.as_view()),
    path('get-student/<int:pk>/',views.StudentGetById.as_view()),

]
