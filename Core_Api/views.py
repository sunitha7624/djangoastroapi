from Core_Api.Serializers import BioSerializer,TimeZoneWorldSerializer,UsTimeZoneSerializer,RussiaTimeZoneSerializer,CanadaTimeZoneSerializer,DstUsSerializer,DstRussiaSerializer,DstCanadaSerializer

from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.serializers import Serializer
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_multiple_model.views import FlatMultipleModelAPIView


class BioViewSet(viewsets.ModelViewSet):
    queryset = Biodata.objects.all()
    serializer_class = BioSerializer
    permission_classes = (AllowAny,)

class TimeZoneWorldViewSet(viewsets.ModelViewSet):
    queryset = Time_Zone_Rest_Of_The_World_Table.objects.all()
    serializer_class = TimeZoneWorldSerializer
    permission_classes = (AllowAny,)  
        
class UsTimeZoneViewSet(viewsets.ModelViewSet):
    queryset = Us_Time_Zones_By_State_Table.objects.all()
    serializer_class = UsTimeZoneSerializer
    permission_classes = (AllowAny,)      

class RussiaTimeZoneViewSet(viewsets.ModelViewSet):
    queryset = Russia_Time_Zones_By_City_Table.objects.all()
    serializer_class = RussiaTimeZoneSerializer
    permission_classes = (AllowAny,)
    
class CanadaTimeZoneViewSet(viewsets.ModelViewSet):
    queryset = Canada_Time_Zones_By_Province_Territory_Table.objects.all()
    serializer_class = CanadaTimeZoneSerializer
    permission_classes = (AllowAny,)
    
class DstUsViewSet(viewsets.ModelViewSet):
    queryset = Dst_Us_Correction_Timing_Table.objects.all()
    serializer_class = DstUsSerializer
    permission_classes = (AllowAny,)
    
class DstRussiaViewSet(viewsets.ModelViewSet):
    queryset = Dst_Russia_Correction_Timing_Table.objects.all()
    serializer_class = DstRussiaSerializer
    permission_classes = (AllowAny,)
    
class DstCanadaViewSet(viewsets.ModelViewSet):
    queryset = Dst_Canada_Correction_Timing_Table.objects.all()
    serializer_class = DstCanadaSerializer
    permission_classes = (AllowAny,)  
    
# class MyViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         if self.action == 'list':
#             return Time_Zone_Rest_Of_The_World_Table.objects.all()
#         elif self.action == 'retrieve':
#             return Us_Time_Zones_By_State_Table.objects.all(id=self.kwargs['pk'])
#         else:
#             return Russia_Time_Zones_By_City_Table.objects.all()
#     permission_classes = (AllowAny,)    

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return TimeZoneWorldSerializer
#         elif self.action == 'retrieve':
#             return UsTimeZoneSerializer
#         else:
#             return RussiaTimeZoneSerializer    
#     permission_classes = (AllowAny,)
# class MyViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         queryset = Time_Zone_Rest_Of_The_World_Table.objects.all()
#         queryset2 = Us_Time_Zones_By_State_Table.objects.all()
#         return queryset1.union(queryset2)
         

#     def get_serializer_class(self):
#         if self.action == 'Time_Zone_Rest_Of_The_World_Table':
#             return TimeZoneWorldSerializer
#         elif self.action == 'Us_Time_Zones_By_State_Table':
#             return UsTimeZoneSerializer
          
        
 
    
    # def aboutview(request):
#     # queryset = Time_Zone_Rest_Of_The_World_Table.objects.all().values()
#     # queryset1 = Us_Time_Zones_By_State_Table.objects.all().values()
#     # queryset2 = Russia_Time_Zones_By_City_Table.objects.all().values()
#     serializer = TimeZoneWorldSerializer(Time_Zone_Rest_Of_The_World_Table.objects.all().values(), many=True)
#     # result_list = queryset | queryset1 | queryset3
#     return serializer                    


# class DualSerializerViewSet(viewsets.ModelViewSet):
   
    
#     def list(self, *args, **kwargs):
#         self.serializer_class = self.TimeZoneWorldSerializer
#         return viewsets.ModelViewSet.list(self, *args, **kwargs)

#     def retrieve(self, *args, **kwargs):
#         self.serializer_class = self.DstCanadaSerializer
#         return viewsets.ModelViewSet.retrieve(self, *args, **kwargs)
    
    
# class TextAPIViewSet(FlatMultipleModelAPIView):
#     querylist = [
#         {'queryset': Time_Zone_Rest_Of_The_World_Table.objects.all(), 'serializer_class': TimeZoneWorldSerializer},
#         {'queryset': Us_Time_Zones_By_State_Table.objects.all(), 'serializer_class': UsTimeZoneSerializer},
#         {'queryset': Russia_Time_Zones_By_City_Table.objects.all(), 'serializer_class': RussiaTimeZoneSerializer},
#         {'queryset': Canada_Time_Zones_By_Province_Territory_Table.objects.all(), 'serializer_class': CanadaTimeZoneSerializer},
#         {'queryset': Dst_Us_Correction_Timing_Table.objects.all(), 'serializer_class': DstUsSerializer},
#         {'queryset': Dst_Russia_Correction_Timing_Table.objects.all(), 'serializer_class': DstRussiaSerializer},
#         {'queryset': Dst_Canada_Correction_Timing_Table.objects.all(), 'serializer_class': DstCanadaSerializer},
      
#     ]
    
# class MyMultiQuerysetViewSet(viewsets.ModelViewSet):
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['queryset1'] = Time_Zone_Rest_Of_The_World_Table.objects.all()
#         context_data['queryset2'] = Us_Time_Zones_By_State_Table.objects.all()
#         context_data['queryset3'] = Russia_Time_Zones_By_City_Table.objects.all()
#         context_data['queryset4'] = Canada_Time_Zones_By_Province_Territory_Table.objects.all()
#         context_data['queryset5'] = Dst_Us_Correction_Timing_Table.objects.all()
#         context_data['queryset6'] = Dst_Russia_Correction_Timing_Table.objects.all()
#         context_data['queryset7'] = Dst_Canada_Correction_Timing_Table.objects.all()
#         return context_data
