from django.urls import path

from . import views

urlpatterns = [
    path("functionAnnotation/1", views.function_annotation_1),
    path("exception/1", views.exception_1),
    path("typing/1", views.typing_1),
    path("call/1", views.call_1),
    path("inheritance/1", views.inheritance_1),
    path("decorator/1", views.decorator_1),
    path("orm/1", views.orm_1),
    path("middleware/1", views.middleware_1),
    path("log/1", views.log_1),
]
