from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Define the app name
app_name = 'onlinecourse'

# Define URL patterns
urlpatterns = [
    # Enroll URL
    path(route='course/<int:pk>/enroll/', view=views.EnrollView.as_view(), name='enroll'),
    # Popular course list URL
    path(route='', view=views.CourseListView.as_view(), name='popular_course_list'),
    # Course details URL
    path(route='course/<int:pk>/', view=views.CourseDetailsView.as_view(), name='course_details'),
    # Authentication related URLs
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('registration/', views.registration_request, name='registration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)