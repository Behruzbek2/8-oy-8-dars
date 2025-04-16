from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassViewSet, StudentViewSet

router = DefaultRouter()
router.register('teachers', TeacherViewSet)
router.register('classes', ClassViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
