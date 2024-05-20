from django.urls import path
from .views import task_list, task_detail
from .views import translation_task
from .views import about_view
from .views import contact_view

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/<int:task_id>/', task_detail, name='task_detail'),
    path('translate/', translation_task, name='translation_task'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]
