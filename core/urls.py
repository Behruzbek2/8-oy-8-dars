from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassViewSet, StudentViewSet

router = DefaultRouter()
router.register('teachers', TeacherViewSet, basename='teacher')
router.register('classes', ClassViewSet, basename='class')
router.register('students', StudentViewSet, basename='student')



urlpatterns = [
    path('', include(router.urls)),
]
