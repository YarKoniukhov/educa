from django.urls import path, include
from rest_framework import routers
from . import view


app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', view.CourseViewSet)

urlpatterns = [
    path('subjects/', view.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', view.SubjectDetailView.as_view(), name='subject_detail'),
    # path('courses/<pk>/enroll/', view.CourseEnrollView.as_view(), name='course_enroll'),
    path('', include(router.urls)),
]
