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
    
class D1RashiSerializer(serializers.ModelSerializer):
    class Meta:
        model =Rashi_Chart_D1_Table
        fields = '__all__'        
        
class D2UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UMA_SHAMBHU_Hora_D2_US_Table
        fields = '__all__' 
        
        
class D3PrashariDrekkanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRASHARI_DREKKANA_D3_PD_Table
        fields = '__all__'
        
class D45AkshavedamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AKSHAVEDAMSA_D45_Table
        fields = '__all__' 
        
class D7SaptamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SAPTAMSHA_D7_Table
        fields = '__all__'   
        
class D2ParashariHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARASHARI_HORA_D2_PH_Table
        fields = '__all__'
        
class D2JagannathHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = JAGANNATH_Hora_D2_JH_Table
        fields = '__all__'
        
class D2KashiNathHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = KASHI_NATH_Hora_D2_KN_Table
        fields = '__all__'        
        
class D2SamaSaptakHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = SAMA_SAPTAK_Hora_D2_SS_Table
        fields = '__all__'
        
class D2MandukaHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = MANDUKA_Hora_D2_MH_Table
        fields = '__all__'
        
class D2LabhMandookHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = LABH_MANDOOK_Hora_Table
        fields = '__all__'
        
class D2SomNathHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOM_NATH_Hora_D2_SN_Table
        fields = '__all__'  
        
class D2ParivriittiDwayaHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARIVRIITTI_DWAYA_Hora_D2_PD_Table
        fields = '__all__' 
        
class D3ParivitritTrayaDrekkanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARIVITRII_TRAYA_DREKKANA_D3_PT_Table
        fields = '__all__'
        
class D3JagannathDrekkanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = JAGANNATH_DREKKANA_D3_JD_Table
        fields = '__all__' 
        
class D3SomnathmDrekkanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOMNATH_M_DREKKANA_D3_SMD_Table
        fields = '__all__'
        
class D4ParashariChaturthamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARASHARI_CHATURTHAMSA_OR_TURYA_D4_PC_Table
        fields = '__all__'
        
class D4VedaamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VEDAAMSA_D4_V_Table
        fields = '__all__'
        
class D5ParivrittiPanchamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARIVRITTI_PANCHAMSHA_D5_PP_Table
        fields = '__all__'
        
class D5TajikPanchamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TAJIK_PANCHAMSHA_D5_TP_Table
        fields = '__all__' 
        
class D6KaulukaShastamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KAULUKA_SHASTAMSA_D6_KS_Table
        fields = '__all__' 
        
class D6ParivrittiSHashtamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARIVRITTI_SHASHTAMSA_D6_PS_Table
        fields = '__all__'  
        
class D8TajikAshtamamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TAJIK_ASHTAMAMSHA_D8_TA_Table
        fields = '__all__'
        
class D9ParashariNavamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARASHARI_NAVAMSHA_D9_PN_Table
        fields = '__all__' 
        
class D9SomnathNavamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOMNATH_NAVAMSHA_D9_SN_Table
        fields = '__all__' 
        
class D9PadaNavamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PADA_NAVAMSHA_D9_PN_Table
        fields = '__all__'
        view_name = 'pada_navamsha_d9_pn_table-detail' 
        
class D9NadiNavamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NADI_NAVAMSHA_D9_NN_Table
        fields = '__all__' 
        
class D10DashamanshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DASHAMANSHA_D10_Table
        fields = '__all__' 
        
class D11ParashariRudramsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARASHARI_RUDRAMSA_D11_PR_Table
        fields = '__all__'         
        
class D11IyerLabhamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IYER_LABHAMSA_D11_IL_Table
        fields = '__all__'    
        
class D11labhamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LABHAMSA_D11_Table
        fields = '__all__'  
        
class D12DvadashamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DVADASHAMSA_D12_Table
        fields = '__all__'  
        
class D16ParashriSodashamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARASHARI_SODASHAMSA_D16_PS_Table
        fields = '__all__' 
        
class D16IyerSodashamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IYER_SODASHAMSA_D16_IS_Table
        fields = '__all__'
        
class D20VimsamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VIMSAMSHA_D20_Table
        fields = '__all__'     
        
class D24ParasharSiddhaamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARASHAR_SIDDHAAMSHA_D24_PSI_Table
        fields = '__all__'  
        
class D24ParaVidhyaSiddhamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARA_VIDHYA_SIDDHAMSHA_D24_PVSI_Table
        fields = '__all__'    
        
class D27BhamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BHAMSHA_D27_Table
        fields = '__all__'   
        
class D30ParashariTattvamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARASHARI_TATTVAMSA_D30_PT_Table
        fields = '__all__'      
        
class D30VenketshwarTrimshamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VENKETSHWAR_TRIMSHAMSA_D30_VT_Table
        fields = '__all__'  
        
class D40KhadvedamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khadvedamsa_D40_Table
        fields = '__all__'  
        
class D60SastiamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sastiamsa_D60_Table
        fields = '__all__'  
        
class D81NavaNavamshaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavaNavamsha_D81_Table
        fields = '__all__'  
        
class D108AshtottaramsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ashtottaramsa_D108_Table
        fields = '__all__'
        
class D144DwadasamsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dwadasamsa_Dwadasamsa_D144_Table
        fields = '__all__'
        
class ArudhaLagnaDeterminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arudha_lagna_determination_Table
        fields = '__all__'    
        
class RasiNamesAndSymbolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasi_Names_And_Symbols
        fields = '__all__'                                                                                                                                                                                                                 
         
class NakshatraExtent27Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nakshatra_Extent_27_in_terms_of_Degree_table
        fields = '__all__'   
        
class KaranaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karana_Table
        fields = '__all__'                                                                                             

class NatalFirstTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natal_First_Time_Table
        fields = '__all__'                                             

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Registration_Table
        fields = '__all__' 

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Setting_Table
        fields = '__all__' 

class NakshatraLordDasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nakshatra_Lord_For_Dasa_Table
        fields = '__all__' 
        
class AshtottariDasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ashtottari_Dasa_Table
        fields = '__all__'         


