from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),# create addTask func in views.py of todo app
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    #mark_as_undone func in views.py of todo app
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    #edit_task func in views.py of todo app
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    #delete_task func in views.py of todo app
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]