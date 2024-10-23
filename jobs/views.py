import requests
from rest_framework import generics
from .models import Job,JobApplication,Category
from .serializers import JobSerializer,JobApplicationSerializer,CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny

IMAGEBB_API_KEY = '60f5767e7375b712f0cc7276b0840596'

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        if self.request.user.user_type == "employer":
            serializer = JobSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(employer=request.user)
                return Response({"success" : "job list create successfully"})
        else:
            raise PermissionDenied({"error":"Only employer can create job listing"})

    def get_queryset(self):
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            return Job.objects.filter(category__id=category_id)
        return Job.objects.all()

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobApplicationCreateView(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        job_id = self.kwargs.get('job_id')  # URL theke job ID pawa holo
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            raise PermissionDenied({"error": "Job not found."})

        # Jodi current user employer hoy, tahole application korte parbe na
        if request.user.user_type == 'employer':
            raise PermissionDenied({"error": "Employers cannot apply for jobs."})

        # Application create kora hocche
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            application = serializer.save(job=job, applicant=request.user)

            # Email pathano hocche
            
            subject = 'Job Application Successful Message'
            message = f'Congratulations {self.request.user.username} have applied for the post of {job}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [self.request.user.email,job.employer.email]
            send_mail( subject, message, email_from, recipient_list)
            

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployerDashboardView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Job.objects.filter(employer=user)


class JobDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user)

class JobApplicantsView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return JobApplication.objects.filter(job_id=job_id, job__employer=self.request.user)


class JobSeekerDashboardView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    ermission_classes = [IsAuthenticated]
    def get_queryset(self):
        return JobApplication.objects.filter(applicant=self.request.user)
    
class JobSeekerDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(applicant=self.request.user)
    
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()
       
class JobListByCategoryView(generics.ListAPIView):
    serializer_class = JobSerializer

    