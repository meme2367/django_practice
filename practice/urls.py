from django.urls import path

from . import views

urlpatterns = [
    path("functionAnnotation/1", views.functionAnnotation1),
    path("exception/1", views.exception1),
    path("typing/1", views.typing1),
    path("call/1", views.call1),
    path("inheritance/1", views.inheritance1),
    path("decorator/1", views.decorator1),
    path("orm/1", views.orm1),
    path("middleware/1", views.middleware1),
    path("log/1", views.log1),
]
