from django.urls import path, include
from .views import TodoList, TodoRetrieve, TodoUpdate

urlpatterns = [
    path(route='tasks/', view=TodoList.as_view(), name='todo-list'),
    path(route='tasks/<int:id>/', view=TodoRetrieve.as_view(), name='todo-detail'),
    path(route='update/<int:id>/', view=TodoUpdate.as_view(), name='todo-update'),
    path(route='api-auth/', view=include('rest_framework.urls')),
    path(route='', view=include(arg='allauth.urls')),
]