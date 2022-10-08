from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'singer', SingerView, basename='singer')


urlpatterns = [
                  path('list/', ListTodo.as_view()),
                  path('<int:pk>/', Details.as_view()),
                  path('create/', CreateToDo.as_view()),
                  path('delete/<int:pk>/', DeleteTodo.as_view())
              ] +router.urls