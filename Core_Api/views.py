from Core_Api.Serializers import BioSerializer,TimeZoneWorldSerializer,UsTimeZoneSerializer,RussiaTimeZoneSerializer,CanadaTimeZoneSerializer,DstUsSerializer,DstRussiaSerializer,DstCanadaSerializer,D2UsSerializer,D3PrashariDrekkanaSerializer,D45AkshavedamsaSerializer,D7SaptamshaSerializer,D2ParashariHoraSerializer,D2JagannathHoraSerializer,D2KashiNathHoraSerializer,D2SamaSaptakHoraSerializer,D2MandukaHoraSerializer,D2LabhMandookHoraSerializer,D2SomNathHoraSerializer,D2ParivriittiDwayaHoraSerializer,D3ParivitritTrayaDrekkanaSerializer,D3JagannathDrekkanaSerializer,D3SomnathmDrekkanaSerializer,D4ParashariChaturthamsaSerializer,D4VedaamsaSerializer,D5ParivrittiPanchamshaSerializer,D5TajikPanchamshaSerializer,D6KaulukaShastamsaSerializer,D6ParivrittiSHashtamsaSerializer ,D8TajikAshtamamshaSerializer,D9ParashariNavamshaSerializer,D9SomnathNavamshaSerializer,D9PadaNavamshaSerializer,D9NadiNavamshaSerializer,D10DashamanshaSerializer,D11ParashariRudramsaSerializer,D11IyerLabhamsaSerializer,D12DvadashamsaSerializer,D16ParashriSodashamsaSerializer,D16IyerSodashamsaSerializer,D20VimsamshaSerializer,D24ParasharSiddhaamshaSerializer,D24ParaVidhyaSiddhamshaSerializer,D27BhamshaSerializer,D30ParashariTattvamsaSerializer,D30VenketshwarTrimshamsaSerializer,D40KhadvedamsaSerializer,D60SastiamsaSerializer,D81NavaNavamshaSerializer,D108AshtottaramsaSerializer,D144DwadasamsaSerializer,ArudhaLagnaDeterminationSerializer,RasiNamesAndSymbolsSerializer,D1RashiSerializer,NakshatraExtent27Serializer,KaranaSerializer,NatalFirstTimeSerializer,UserRegistrationSerializer,UserSettingSerializer,NakshatraLordDasaSerializer,AshtottariDasaSerializer

from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.serializers import Serializer
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_multiple_model.views import FlatMultipleModelAPIView
from rest_framework.views import APIView



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
       
class NatalFirstTimeViewSet(viewsets.ModelViewSet):
    queryset = Natal_First_Time_Table.objects.all()
    serializer_class = NatalFirstTimeSerializer
    permission_classes = (AllowAny,)
    
class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User_Registration_Table.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    
class UserSettingViewSet(viewsets.ModelViewSet):

    queryset = User_Setting_Table.objects.all()
    serializer_class = UserSettingSerializer
    permission_classes = (AllowAny,) 
  
class CombinedDataView(APIView):
    def get(self, request, *args, **kwargs):
        rashichartd1_data = Rashi_Chart_D1_Table.objects.all()
        umashambhuhora_data = UMA_SHAMBHU_Hora_D2_US_Table.objects.all()
        parasharihora_data = PARASHARI_HORA_D2_PH_Table.objects.all()
        jagannathhora_data = JAGANNATH_Hora_D2_JH_Table.objects.all()
        kashinathhora_data = KASHI_NATH_Hora_D2_KN_Table.objects.all()
        mandukahora_data = MANDUKA_Hora_D2_MH_Table.objects.all()
        labhmandookhora_data = LABH_MANDOOK_Hora_Table.objects.all()
        somnathhora_data = SOM_NATH_Hora_D2_SN_Table.objects.all()
        parivriittidwayahora_data = PARIVRIITTI_DWAYA_Hora_D2_PD_Table.objects.all()
        prasharidrekkana_data = PRASHARI_DREKKANA_D3_PD_Table.objects.all()
        parivitriitrayadrekkana_data = PARIVITRII_TRAYA_DREKKANA_D3_PT_Table.objects.all()
        jagannathdrekkana_data = JAGANNATH_DREKKANA_D3_JD_Table.objects.all()
        somnathmdrekkana_data = SOMNATH_M_DREKKANA_D3_SMD_Table.objects.all()
        parasharichaturthamsaorturya_data = PARASHARI_CHATURTHAMSA_OR_TURYA_D4_PC_Table.objects.all()
        vedaamsa_data = VEDAAMSA_D4_V_Table.objects.all()
        parivrittipanchamsha_data = PARIVRITTI_PANCHAMSHA_D5_PP_Table.objects.all()
        tajikpancham_data = TAJIK_PANCHAMSHA_D5_TP_Table.objects.all()
        kaulukashastamsa_data = KAULUKA_SHASTAMSA_D6_KS_Table.objects.all()
        parivrittishashtamsa_data = PARIVRITTI_SHASHTAMSA_D6_PS_Table.objects.all()
        saptamsha_data = SAPTAMSHA_D7_Table.objects.all()
        tajikashtamamsha_data = TAJIK_ASHTAMAMSHA_D8_TA_Table.objects.all()
        parasharinavamsha_data = PARASHARI_NAVAMSHA_D9_PN_Table.objects.all()
        somnathnavamsha_data = SOMNATH_NAVAMSHA_D9_SN_Table.objects.all()
        padanavamsha_data = PADA_NAVAMSHA_D9_PN_Table.objects.all()
        nadinavamsha_data = NADI_NAVAMSHA_D9_NN_Table.objects.all()
        dashamansha_data = DASHAMANSHA_D10_Table.objects.all()
        parasharirudramsa_data = PARASHARI_RUDRAMSA_D11_PR_Table.objects.all()
        iyerlabhamsa_data = IYER_LABHAMSA_D11_IL_Table.objects.all()
        dvadashamsa_data = DVADASHAMSA_D12_Table.objects.all()
        parasharisodashamsa_data = PARASHARI_SODASHAMSA_D16_PS_Table.objects.all()
        iyersodashamsa_data = IYER_SODASHAMSA_D16_IS_Table.objects.all()
        vimsamsha_data = VIMSAMSHA_D20_Table.objects.all()
        parasharsiddhaamsha_data = PARASHAR_SIDDHAAMSHA_D24_PSI_Table.objects.all()
        paravidhyasiddhamsha_data = PARA_VIDHYA_SIDDHAMSHA_D24_PVSI_Table.objects.all()
        bhamsha_data = BHAMSHA_D27_Table.objects.all()
        parasharitattvamsa_data = PARASHARI_TATTVAMSA_D30_PT_Table.objects.all()
        venketshwartrimshamsa_data = VENKETSHWAR_TRIMSHAMSA_D30_VT_Table.objects.all()
        khadvedamsa_data = Khadvedamsa_D40_Table.objects.all()
        akshavedamsa_data = AKSHAVEDAMSA_D45_Table.objects.all()
        sastiamsa_data = Sastiamsa_D60_Table.objects.all()
        navanavamsha_data = NavaNavamsha_D81_Table.objects.all()
        ashtottaramsa_data = Ashtottaramsa_D108_Table.objects.all()
        dwadasamsa_data = Dwadasamsa_Dwadasamsa_D144_Table.objects.all()
        arudhalagna_data = Arudha_lagna_determination_Table.objects.all()
        rasinamelord_data = Rasi_Names_And_Symbols.objects.all()
        nakshatra27degree_data = Nakshatra_Extent_27_in_terms_of_Degree_table.objects.all()
        karanadegree_data =  Karana_Table.objects.all()
        nakshatradasa_data =  Nakshatra_Lord_For_Dasa_Table.objects.all()
        ashtottaridasa_data =  Ashtottari_Dasa_Table.objects.all()

        d1rashi_serializer = D1RashiSerializer(rashichartd1_data, many=True)
        umashambhuhora_serializer = D2UsSerializer(umashambhuhora_data, many=True)
        parasharihora_serializer = D2ParashariHoraSerializer(parasharihora_data, many=True)
        jagannathhora_serializer = D2JagannathHoraSerializer(jagannathhora_data, many=True)
        kashinathhora_serializer = D2KashiNathHoraSerializer(kashinathhora_data, many=True)
        mandukahora_serializer = D2MandukaHoraSerializer(mandukahora_data, many=True)
        labhmandookhora_serializer = D2LabhMandookHoraSerializer(labhmandookhora_data, many=True)
        somnathhora_serializer = D2SomNathHoraSerializer(somnathhora_data, many=True)
        parivriittidwayahora_serializer = D2ParivriittiDwayaHoraSerializer(parivriittidwayahora_data, many=True)
        prasharidrekkana_serializer = D3PrashariDrekkanaSerializer(prasharidrekkana_data, many=True)
        parivitriitrayadrekkana_serializer = D3ParivitritTrayaDrekkanaSerializer(parivitriitrayadrekkana_data, many=True)
        jagannathdrekkana_serializer = D3JagannathDrekkanaSerializer(jagannathdrekkana_data, many=True)
        somnathmdrekkana_serializer = D3SomnathmDrekkanaSerializer(somnathmdrekkana_data, many=True)
        parasharichaturthamsaorturya_serializer = D4ParashariChaturthamsaSerializer(parasharichaturthamsaorturya_data, many=True)
        vedaamsa_serializer = D4VedaamsaSerializer(vedaamsa_data, many=True)
        parivrittipanchamsha_serializer = D5ParivrittiPanchamshaSerializer(parivrittipanchamsha_data, many=True)
        tajikpancham_serializer = D5TajikPanchamshaSerializer(tajikpancham_data, many=True)
        kaulukashastamsa_serializer = D6KaulukaShastamsaSerializer(kaulukashastamsa_data, many=True)
        parivrittishashtamsa_serializer = D6ParivrittiSHashtamsaSerializer(parivrittishashtamsa_data, many=True)
        saptamsha_serializer = D7SaptamshaSerializer(saptamsha_data, many=True)
        tajikashtamamsha_serializer = D8TajikAshtamamshaSerializer(tajikashtamamsha_data, many=True)
        parasharinavamsha_serializer = D9ParashariNavamshaSerializer(parasharinavamsha_data, many=True)
        somnathnavamsha_serializer = D9SomnathNavamshaSerializer(somnathnavamsha_data, many=True)
        padanavamsha_serializer = D9PadaNavamshaSerializer(padanavamsha_data, many=True)
        nadinavamsha_serializer = D9NadiNavamshaSerializer(nadinavamsha_data, many=True)
        dashamansha_serializer = D10DashamanshaSerializer(dashamansha_data, many=True)
        parasharirudramsa_serializer = D11ParashariRudramsaSerializer(parasharirudramsa_data, many=True)
        iyerlabhamsa_serializer = D11IyerLabhamsaSerializer(iyerlabhamsa_data, many=True)
        dvadashamsa_serializer = D12DvadashamsaSerializer(dvadashamsa_data, many=True)
        parasharisodashamsa_serializer = D16ParashriSodashamsaSerializer(parasharisodashamsa_data, many=True)
        iyersodashamsa_serializer = D16IyerSodashamsaSerializer(iyersodashamsa_data, many=True)
        vimsamsha_serializer = D20VimsamshaSerializer(vimsamsha_data, many=True)
        parasharsiddhaamsha_serializer = D24ParasharSiddhaamshaSerializer(parasharsiddhaamsha_data, many=True)
        paravidhyasiddhamsha_serializer = D24ParaVidhyaSiddhamshaSerializer(paravidhyasiddhamsha_data, many=True)
        bhamsha_serializer = D27BhamshaSerializer(bhamsha_data, many=True)
        parasharitattvamsa_serializer = D30ParashariTattvamsaSerializer(parasharitattvamsa_data, many=True)
        venketshwartrimshamsa_serializer = D30VenketshwarTrimshamsaSerializer(venketshwartrimshamsa_data, many=True)
        khadvedamsa_serializer = D40KhadvedamsaSerializer(khadvedamsa_data, many=True)
        akshavedamsa_serializer = D45AkshavedamsaSerializer(akshavedamsa_data, many=True)
        sastiamsa_serializer = D60SastiamsaSerializer(sastiamsa_data, many=True)
        navanavamsha_serializer = D81NavaNavamshaSerializer(navanavamsha_data, many=True)
        ashtottaramsa_serializer = D108AshtottaramsaSerializer(ashtottaramsa_data, many=True)
        dwadasamsa_serializer = D144DwadasamsaSerializer(dwadasamsa_data, many=True)
        arudhalagna_serializer = ArudhaLagnaDeterminationSerializer(arudhalagna_data, many=True)
        rasinamelord_serializer = RasiNamesAndSymbolsSerializer(rasinamelord_data, many=True)
        nakshatraextent27degree_serializer = NakshatraExtent27Serializer(nakshatra27degree_data, many=True)
        karanadegree_serializer = KaranaSerializer(karanadegree_data, many=True)
        nakshatralorddasa_serializer = NakshatraLordDasaSerializer(nakshatradasa_data, many=True)
        ashtottarilorddasa_serializer = AshtottariDasaSerializer(ashtottaridasa_data, many=True)

        combined_data = {
            'Rashi_Chart_D1': d1rashi_serializer.data,
            'UMA_SHAMBHU_HORA_D2US': umashambhuhora_serializer.data,
            'PARASHARI_HORA_D2PH': parasharihora_serializer.data,
            'JAGANNATH_HORA_D2JH': jagannathhora_serializer.data,
            'KASHINATH_HORA_D2KH': kashinathhora_serializer.data,
            'MANDUKA_HORA_D2MH': mandukahora_serializer.data,
            'LABHMANDOOK_HORA_D2LH': labhmandookhora_serializer.data,
            'SOMNATH_HORA_D2SN': somnathhora_serializer.data,
            'PARIVRIITTIDWAYA_Hora_D2PD': parivriittidwayahora_serializer.data,
            'PRASHRI_DREKKANA_D3PD': prasharidrekkana_serializer.data,
            'PARIVITRII_TRAYA_DREKKANA_D3PT': parivitriitrayadrekkana_serializer.data,
            'JAGANNATH_DREKKANA_D3JD': jagannathdrekkana_serializer.data,
            'SOMNATH_M_DREKKANA_D3SMD': somnathmdrekkana_serializer.data,
            'PARASHARI_CHATURTHAMSA_OR_TURYA_D4PCT': parasharichaturthamsaorturya_serializer.data,
            'VEDAAMSA_D4V': vedaamsa_serializer.data,
            'PARIVRITTI_PANCHAMSHA_D5PP': parivrittipanchamsha_serializer.data,
            'TAJIK_PANCHAMSHA_D5TP': tajikpancham_serializer.data,
            'KAULUKA_SHASTAMSA_D6KS': kaulukashastamsa_serializer.data,
            'PARIVRITTI_SHASHTAMSA_D6PS': parivrittishashtamsa_serializer.data,
            'SAPTAMSHA_D7': saptamsha_serializer.data,
            'TAJIK_ASHTAMAMSHA_D8TA': tajikashtamamsha_serializer.data,
            'PARASHARI_NAVAMSHA_D9PN': parasharinavamsha_serializer.data,
            'SOMNATH_NAVAMSHA_D9SN': somnathnavamsha_serializer.data,
            'PADA_NAVAMSHA_D9PN': padanavamsha_serializer.data,
            'NADI_NAVAMSHA_D9NN': nadinavamsha_serializer.data,
            'DASHAMANSHA_D10': dashamansha_serializer.data,
            'PARASHARI_RUDRAMSA_D11PR': parasharirudramsa_serializer.data,
            'IYER_LABHAMSA_D11IL': iyerlabhamsa_serializer.data,
            'DVADASHAMSA_D12': dvadashamsa_serializer.data,
            'PARASHARI_SODASHAMSA_D16PS': parasharisodashamsa_serializer.data,
            'IYER_SODASHAMSA_D16IS': iyersodashamsa_serializer.data,
            'VIMSAMSHA_D20': vimsamsha_serializer.data,
            'PARASHAR_SIDDHAAMSHA_D24PSI': parasharsiddhaamsha_serializer.data,
            'PARA_VIDHYA_SIDDHAMSHA_D24PVSI': paravidhyasiddhamsha_serializer.data,
            'BHAMSHA_D27': bhamsha_serializer.data,
            'PARASHARI_TATTVAMSA_D30PT': parasharitattvamsa_serializer.data,
            'VENKETSHWAR_TRIMSHAMSA_D30VT': venketshwartrimshamsa_serializer.data,
            'Khadvedamsa_D40': khadvedamsa_serializer.data,
            'AKSHAVEDAMSA_D45': akshavedamsa_serializer.data,
            'Sastiamsa_D60': sastiamsa_serializer.data,
            'NavaNavamsha_D81': navanavamsha_serializer.data,
            'Ashtottaramsa_D108': ashtottaramsa_serializer.data,
            'Dwadasamsa_D144': dwadasamsa_serializer.data,
            'Arudha_Lagna_Determination': arudhalagna_serializer.data,
            'Rasi_Names_And_Symbols': rasinamelord_serializer.data,
            'Nakshatra_Extent_27_Degree': nakshatraextent27degree_serializer.data,
            'Karana_From_To_Degree': karanadegree_serializer.data,
            'nakshatra_Lord_Dasa': nakshatralorddasa_serializer.data,
            'Ashtittari_Lord_Dasa': ashtottarilorddasa_serializer.data,
        }

        return Response(combined_data, status=status.HTTP_200_OK)

