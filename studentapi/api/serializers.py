from dataclasses import fields
from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id','name','city','roll']