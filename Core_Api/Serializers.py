from rest_framework import serializers
from .models import * 

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodata
        fields = '__all__'


class TimeZoneWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_Zone_Rest_Of_The_World_Table
        fields = '__all__'

class UsTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Us_Time_Zones_By_State_Table
        fields = '__all__'    
        
class RussiaTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Russia_Time_Zones_By_City_Table
        fields = '__all__' 
        
class CanadaTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canada_Time_Zones_By_Province_Territory_Table
        fields = '__all__' 
        
class DstUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dst_Us_Correction_Timing_Table
        fields = '__all__' 
        
class DstRussiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dst_Russia_Correction_Timing_Table
        fields = '__all__'  
        
class DstCanadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dst_Canada_Correction_Timing_Table
        fields = '__all__'    
        
        
class D2UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UMA_SHAMBHU_Hora_D2_US_Table
        fields = '__all__'                                                     




