from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Route for the course list (Home page)
    path(route='', view=views.CourseListView.as_view(), name='index'),
    
    # Authentication routes
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
    # Course detail route: /onlinecourse/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    
    # Enrollment route: /onlinecourse/5/enroll/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Route for exam submission: /onlinecourse/5/submit/
    path('<int:course_id>/submit/', views.submit, name="submit"),

    # Route for showing exam results: /onlinecourse/course/5/submission/10/result/
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name="show_exam_result"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)