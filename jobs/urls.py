from django.urls import path
from .views import JobListCreateView, JobDetailView,JobApplicationCreateView,EmployerDashboardView,JobSeekerDashboardView,JobDetailUpdateView,JobApplicantsView,JobSeekerDetailView,CategoryListView

urlpatterns = [
   
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),#job create and joblist view api
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),#job detail api
     #employer api
    path('employer/dashboard/', EmployerDashboardView.as_view(), name='employer_dashboard'),#employer dashboard api
    path('employer/job/<int:pk>/', JobDetailUpdateView.as_view(), name='job_detail_update'),#employer dashboard updat api
    path('employer/job/<int:job_id>/applicants/', JobApplicantsView.as_view(), name='job_applicants'),#employer job application view api
    #job-seeker api
    path('jobs/<int:job_id>/apply/', JobApplicationCreateView.as_view(), name='job-apply'),#apply api
    path('job-seeker/dashboard/', JobSeekerDashboardView.as_view(), name='job-seeker-dashboard'),#dashboard or View api
    path('job-seeker/dashboard/<int:pk>',JobSeekerDetailView.as_view(), name='job-seeker-detail-view'),#dashboard update api
    #category api
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
