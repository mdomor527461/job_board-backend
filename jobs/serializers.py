from rest_framework import serializers
from .models import Job,JobApplication,Category

class JobSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category')
    employer_name = serializers.StringRelatedField(source='employer')
    class Meta:
        model = Job
        fields = ['id', 'employer','employer_name', 'title', 'description', 'requirements', 'location', 'company_name', 'date_posted', 'category','category_name']

    def get_category(self, obj):
        return obj.category.name

class JobApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.ReadOnlyField(source='applicant.username')
    job = serializers.SerializerMethodField()
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['job']
    def get_job(self,obj):
        return obj.job.title

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
