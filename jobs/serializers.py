from rest_framework import serializers
from .models import Job,JobApplication,Category

class JobSerializer(serializers.ModelSerializer):
    employer = serializers.ReadOnlyField(source='employer.username')

    class Meta:
        model = Job
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.ReadOnlyField(source='applicant.username')
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['job']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
