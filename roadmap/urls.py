from django.urls import path
from .views import (
    SyllabusListCreateView,
    SyllabusDetailView,
    generate_roadmap
)

urlpatterns = [
    path('syllabus/', SyllabusListCreateView.as_view(), name='syllabus-list'),
    path('syllabus/<int:pk>/', SyllabusDetailView.as_view(), name='syllabus-detail'),
    path('syllabus/<int:syllabus_id>/generate-roadmap/', generate_roadmap, name='generate-roadmap'),
]