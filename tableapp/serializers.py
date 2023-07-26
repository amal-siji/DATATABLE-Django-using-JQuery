from rest_framework import serializers
from .models import *
from .models import Person



class table_serializer(serializers.ModelSerializer):
    
    class Meta:
        model=Person
        fields=['name','place']
        
        
class edit_seri(serializers.ModelSerializer):

    class Meta:
        model =Person       
        fields =['name','place']
       
       
       
