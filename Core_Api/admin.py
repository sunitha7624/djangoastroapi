from typing import overload
from django.contrib import admin
from .models import *
# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Biodata._meta.get_fields()]
    list_editable = list_display[1:]

class TithiAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tithi._meta.get_fields()]
    list_editable = list_display[1:]

class Tithi_Graha_LordshipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tithi_Graha_Lordship._meta.get_fields()]
    list_editable = list_display[1:]

class Tithi_Group_Tattva_LordshipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tithi_Group_Tattva_Lordship._meta.get_fields()]
    list_editable = list_display[1:]

class Vara_LordsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vara_Lords._meta.get_fields()]
    list_editable = list_display[1:]

class Rivers_DietiesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rivers_Dieties._meta.get_fields()]
    list_editable = list_display[1:]

class Gandanta_RashiAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gandanta_Rashi._meta.get_fields()]
    list_editable = list_display[1:]

class Divisional_Charts_CycleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Divisional_Charts_Cycle._meta.get_fields()]
    list_editable = list_display[1:]

class Divisional_Charts_NameAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Divisional_Charts_Name._meta.get_fields()]
    list_editable = list_display[1:]

class Divisional_Charts_GroupingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Divisional_Charts_Groupings._meta.get_fields()]
    list_editable = list_display[1:]

class Rasi_Names_And_SymbolsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rasi_Names_And_Symbols._meta.get_fields()]
    list_editable = list_display[1:]

class rasi_extent_in_zodiac_tableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in rasi_extent_in_zodiac_table._meta.get_fields()]
    list_editable = list_display[1:]


class nakshatra_under_names_28_scheme_tableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in nakshatra_under_names_28_scheme_table._meta.get_fields()]
    list_editable = list_display[1:]


class planets_Names_and_symbols_tableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in planets_Names_and_symbols_table._meta.get_fields()]
    list_editable = list_display[1:]

class Nakshatra_Names_under_27_scheme_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_Names_under_27_scheme_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Nakshatra_Extent_27_in_terms_of_Degree_tableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_Extent_27_in_terms_of_Degree_table._meta.get_fields()]
    list_editable = list_display[1:]

class Nakshatra_Extent_28_in_terms_of_Degree_tableAdmin(admin.ModelAdmin):
     list_display = [field.name for field in Nakshatra_Extent_28_in_terms_of_Degree_table._meta.get_fields()]
     list_editable = list_display[1:]

class Nakshatra_Pada_Table_under_27_nakshatra_schemeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_Pada_Table_under_27_nakshatra_scheme._meta.get_fields()]
    list_editable = list_display[1:]

class Nakshatra_Lord_For_Dasa_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in  Nakshatra_Lord_For_Dasa_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Nakshatra_Deity_Devta_for_REMEDIERAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_Deity_Devta_for_REMEDIER._meta.get_fields()]
    list_editable = list_display[1:]

class Nakshatra_Pada_Rasi_Gyan_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_Pada_Rasi_Gyan_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Rasi_Ayan_and_Tattva_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rasi_Ayan_and_Tattva_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Sapt_Lok_Mandal_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sapt_Lok_Mandal_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Tri_Loka_Chakra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tri_Loka_Chakra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Savya_Apsavya_Nakshatra_Chakra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Savya_Apsavya_Nakshatra_Chakra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Tri_Nadi_Chakra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tri_Nadi_Chakra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Nakshatra_Tattva_Chakra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_Tattva_Chakra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Tattva_Relationship_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tattva_Relationship_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Pushkar_Nakshatra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pushkar_Nakshatra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Panchak_Nakshatra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Panchak_Nakshatra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Pushkar_Navamsa_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pushkar_Navamsa_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Pushkar_Bhaga_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pushkar_Bhaga_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Pushkar_Bhaga_Table_Purva_Kalamrit_c_s_patel_TableAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Pushkar_Bhaga_Table_Purva_Kalamrit_c_s_patel_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Gandanta_Nakshatra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gandanta_Nakshatra_Table._meta.get_fields()]
    list_editable = list_display[1:]

#32-C
class Divisional_Charts_Group_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Divisional_Charts_Group_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Rashi_Chart_D1_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rashi_Chart_D1_Table._meta.get_fields()]
    list_editable = list_display[1:]

class UMA_SHAMBHU_Hora_D2_US_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UMA_SHAMBHU_Hora_D2_US_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARASHARI_HORA_D2_PH_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARASHARI_HORA_D2_PH_Table._meta.get_fields()]
    list_editable = list_display[1:]

class JAGANNATH_Hora_D2_JH_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JAGANNATH_Hora_D2_JH_Table._meta.get_fields()]
    list_editable = list_display[1:]

class KASHI_NATH_Hora_D2_KN_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in KASHI_NATH_Hora_D2_KN_Table._meta.get_fields()]
    list_editable = list_display[1:]

class BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G1_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G1_Table._meta.get_fields()]
    list_editable = list_display[1:]

class BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G2_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G2_Table._meta.get_fields()]
    list_editable = list_display[1:]

class SAMA_SAPTAK_Hora_D2_SS_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SAMA_SAPTAK_Hora_D2_SS_Table._meta.get_fields()]
    list_editable = list_display[1:]

class MANDUKA_Hora_D2_MH_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MANDUKA_Hora_D2_MH_Table._meta.get_fields()]
    list_editable = list_display[1:]

class GOLA_Hora_D2_GH_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GOLA_Hora_D2_GH_Table._meta.get_fields()]
    list_editable = list_display[1:]

class BodyMap_MaleChart_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BodyMap_MaleChart_Table._meta.get_fields()]
    list_editable = list_display[1:]

class BodyMap_FemaleChart_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BodyMap_FemaleChart_Table._meta.get_fields()]
    list_editable = list_display[1:]

class LABH_MANDOOK_Hora_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LABH_MANDOOK_Hora_Table._meta.get_fields()]
    list_editable = list_display[1:]

class SAM_MUKHA_RASHI_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SAM_MUKHA_RASHI_Table._meta.get_fields()]
    list_editable = list_display[1:]

class SAM_MUKHA_Hora_D2_SM_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SAM_MUKHA_Hora_D2_SM_Table._meta.get_fields()]
    list_editable = list_display[1:]

class SOM_NATH_Hora_D2_SN_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SOM_NATH_Hora_D2_SN_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARIVRIITTI_DWAYA_Hora_D2_PD_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARIVRIITTI_DWAYA_Hora_D2_PD_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PRASHARI_DREKKANA_D3_PD_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PRASHARI_DREKKANA_D3_PD_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARIVITRII_TRAYA_DREKKANA_D3_PT_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARIVITRII_TRAYA_DREKKANA_D3_PT_Table._meta.get_fields()]
    list_editable = list_display[1:]

class JAGANNATH_DREKKANA_D3_JD_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JAGANNATH_DREKKANA_D3_JD_Table._meta.get_fields()]
    list_editable = list_display[1:]

class SOMNATH_M_DREKKANA_D3_SMD_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SOMNATH_M_DREKKANA_D3_SMD_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARASHARI_CHATURTHAMSA_OR_TURYA_D4_PC_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARASHARI_CHATURTHAMSA_OR_TURYA_D4_PC_Table._meta.get_fields()]
    list_editable = list_display[1:]

class VEDAAMSA_D4_V_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VEDAAMSA_D4_V_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARIVRITTI_PANCHAMSHA_D5_PP_TableaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARIVRITTI_PANCHAMSHA_D5_PP_Table._meta.get_fields()]
    list_editable = list_display[1:]

class TAJIK_PANCHAMSHA_D5_TP_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TAJIK_PANCHAMSHA_D5_TP_Table._meta.get_fields()]
    list_editable = list_display[1:]

class KAULUKA_SHASTAMSA_D6_KS_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in KAULUKA_SHASTAMSA_D6_KS_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARIVRITTI_SHASHTAMSA_D6_PS_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARIVRITTI_SHASHTAMSA_D6_PS_Table._meta.get_fields()]
    list_editable = list_display[1:]

class SAPTAMSHA_D7_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SAPTAMSHA_D7_Table._meta.get_fields()]
    list_editable = list_display[1:]

class TAJIK_ASHTAMAMSHA_D8_TA_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TAJIK_ASHTAMAMSHA_D8_TA_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARASHARI_NAVAMSHA_D9_PN_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARASHARI_NAVAMSHA_D9_PN_Table._meta.get_fields()]
    list_editable = list_display[1:]

class SOMNATH_NAVAMSHA_D9_SN_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SOMNATH_NAVAMSHA_D9_SN_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PADA_NAVAMSHA_D9_PN_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PADA_NAVAMSHA_D9_PN_Table._meta.get_fields()]
    list_editable = list_display[1:]

class NADI_NAVAMSHA_D9_NN_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NADI_NAVAMSHA_D9_NN_Table._meta.get_fields()]
    list_editable = list_display[1:]    

class DASHAMANSHA_D10_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DASHAMANSHA_D10_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARASHARI_RUDRAMSA_D11_PR_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARASHARI_RUDRAMSA_D11_PR_Table._meta.get_fields()]
    list_editable = list_display[1:]

class IYER_LABHAMSA_D11_IL_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in IYER_LABHAMSA_D11_IL_Table._meta.get_fields()]
    list_editable = list_display[1:]

class LABHAMSA_D11_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LABHAMSA_D11_Table._meta.get_fields()]
    list_editable = list_display[1:]

class DVADASHAMSA_D12_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DVADASHAMSA_D12_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARASHARI_SODASHAMSA_D16_PS_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARASHARI_SODASHAMSA_D16_PS_Table._meta.get_fields()]
    list_editable = list_display[1:]

class IYER_SODASHAMSA_D16_IS_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in IYER_SODASHAMSA_D16_IS_Table._meta.get_fields()]
    list_editable = list_display[1:]

class VIMSAMSHA_D20_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VIMSAMSHA_D20_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARASHAR_SIDDHAAMSHA_D24_PSI_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARASHAR_SIDDHAAMSHA_D24_PSI_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARA_VIDHYA_SIDDHAMSHA_D24_PVSI_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARA_VIDHYA_SIDDHAMSHA_D24_PVSI_Table._meta.get_fields()]
    list_editable = list_display[1:]

class BHAMSHA_D27_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BHAMSHA_D27_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PARASHARI_TATTVAMSA_D30_PT_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PARASHARI_TATTVAMSA_D30_PT_Table._meta.get_fields()]
    list_editable = list_display[1:]

class VENKETSHWAR_TRIMSHAMSA_D30_VT_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VENKETSHWAR_TRIMSHAMSA_D30_VT_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Khadvedamsa_D40_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Khadvedamsa_D40_Table._meta.get_fields()]
    list_editable = list_display[1:]

class AKSHAVEDAMSA_D45_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AKSHAVEDAMSA_D45_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Sastiamsa_D60_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sastiamsa_D60_Table._meta.get_fields()]
    list_editable = list_display[1:]

class NavaNavamsha_D81_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NavaNavamsha_D81_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Ashtottaramsa_D108_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ashtottaramsa_D108_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Dwadasamsa_Dwadasamsa_D144_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dwadasamsa_Dwadasamsa_D144_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Vaiseshikamsaas_varga_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vaiseshikamsaas_varga_Table._meta.get_fields()]
    list_editable = list_display[1:]

class PANCHANG_OVERLORDS_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PANCHANG_OVERLORDS_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Hora_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hora_Table._meta.get_fields()]
    list_editable = list_display[1:]

""" class Navatara_Lagna_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Navatara_Lagna_Table._meta.get_fields()]
    list_editable = list_display[1:] """

""" class Navatara_Moon_Fixed_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Navatara_Moon_Fixed_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Special_Nakshtra_Scheme_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Special_Nakshtra_Scheme_Table._meta.get_fields()]
    list_editable = list_display[1:] """
 
class Nakshatra_element_works_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_element_works_Table._meta.get_fields()]
    list_editable = list_display[1:]
    

class Navratra_Pattern_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Navratra_Pattern_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Special_Navratra_Pattern_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Special_Navratra_Pattern_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Nakshatra_sight_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_sight_Table._meta.get_fields()]
    list_editable = list_display[1:]

class ANDHAADI_NAKSHTRA_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ANDHAADI_NAKSHTRA_Table._meta.get_fields()]
    list_editable = list_display[1:]

class movability_qualities_nakshatra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in movability_qualities_nakshatra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class SAPTA_RISHI_BIRTH_SOURCE_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SAPTA_RISHI_BIRTH_SOURCE_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Natural_Sapt_Rishi_Nakshtra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Natural_Sapt_Rishi_Nakshtra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Characterstic_of_planets_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Characterstic_of_planets_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Characterstics_of_Signs_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Characterstics_of_Signs_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Characterstics_of_Houses_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Characterstics_of_Houses_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Karaka_of_Houses_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Karaka_of_Houses_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Materialistic_things_differentiation_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Materialistic_things_differentiation_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Direction_of_planet_dikpala_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Direction_of_planet_dikpala_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Direction_of_planet_sign_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Direction_of_planet_sign_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Digbala_of_planet_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Digbala_of_planet_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Kundalini_chakra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Kundalini_chakra_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Combination_of_rising_planets_sings_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Combination_of_rising_planets_sings_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Gharba_karak_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gharba_karak_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Pachaakadi_Sambandha_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pachaakadi_Sambandha_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Pachaakadi_Sambandha_B_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pachaakadi_Sambandha_B_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Vaar_Chakra_using_7_planets_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vaar_Chakra_using_7_planets_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Vaar_Chakra_using_9_planets_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vaar_Chakra_using_9_planets_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Houses_from_Pranpada_Lagna_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Houses_from_Pranpada_Lagna_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Life_cycle_of_creature_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Life_cycle_of_creature_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Charakarak_bhava_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Charakarak_bhava_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Form_sun_god_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Form_sun_god_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Primary_argala_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Primary_argala_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Secondary_argala_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Secondary_argala_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Arudha_lagna_determination_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Arudha_lagna_determination_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Arudha_nomenclature_meaning_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Arudha_nomenclature_meaning_Table._meta.get_fields()]
    list_editable = list_display[1:]

class vriddhas_as_per_sahmita_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vriddhas_as_per_sahmita_Table._meta.get_fields()]
    list_editable = list_display[1:]

class tattvas_of_nakshatra_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tattvas_of_nakshatra_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Houses_gunas_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Houses_gunas_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Devta_guna_arudha_strength_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Devta_guna_arudha_strength_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Pancha_prana_tattva_graha_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pancha_prana_tattva_graha_Table._meta.get_fields()]
    list_editable = list_display[1:]
        
class Sub_prana_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sub_prana_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Rasi_graha_varna_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rasi_graha_varna_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Loka_pala_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Loka_pala_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Upa_graha_list_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Upa_graha_list_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Special_points_list_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Special_points_list_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Initiation_chart_list_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Initiation_chart_list_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Name_of_main_topics_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Name_of_main_topics_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Bhava_arudha_list_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bhava_arudha_list_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Graha_arudha_list_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Graha_arudha_list_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Nakshatra_Table_For_Vimshottari_Dasa_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nakshatra_Table_For_Vimshottari_Dasa_Table._meta.get_fields()]
    list_editable = list_display[1:]

class Vimshottari_Dasa_Planetary_Sequence_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vimshottari_Dasa_Planetary_Sequence_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Time_Zone_Rest_Of_The_World_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Time_Zone_Rest_Of_The_World_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Us_Time_Zones_By_State_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Us_Time_Zones_By_State_Table._meta.get_fields()]
    list_editable = list_display[1:] 
    
class Russia_Time_Zones_By_City_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Russia_Time_Zones_By_City_Table._meta.get_fields()]
    list_editable = list_display[1:] 
    
class Canada_Time_Zones_By_Province_Territory_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Canada_Time_Zones_By_Province_Territory_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Dst_Us_Correction_Timing_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dst_Us_Correction_Timing_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Dst_Russia_Correction_Timing_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dst_Us_Correction_Timing_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Dst_Canada_Correction_Timing_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dst_Canada_Correction_Timing_Table._meta.get_fields()]
    list_editable = list_display[1:] 
    
class Karana_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Karana_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Natal_First_Time_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Natal_First_Time_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class User_Registration_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User_Registration_Table._meta.get_fields()]
    list_editable = list_display[1:] 
    
class User_Setting_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User_Setting_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class Ashtottari_Dasa_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ashtottari_Dasa_Table._meta.get_fields()]
    list_editable = list_display[1:]                   
    
    

admin.site.register(Biodata, BiodataAdmin)
admin.site.register(Tithi, TithiAdmin)
admin.site.register(Tithi_Graha_Lordship, Tithi_Graha_LordshipAdmin)
admin.site.register(Tithi_Group_Tattva_Lordship, Tithi_Group_Tattva_LordshipAdmin)
admin.site.register(Vara_Lords, Vara_LordsAdmin)
admin.site.register(Rivers_Dieties, Rivers_DietiesAdmin)
admin.site.register(Gandanta_Rashi, Gandanta_RashiAdmin)
admin.site.register(Divisional_Charts_Cycle, Divisional_Charts_CycleAdmin)
admin.site.register(Divisional_Charts_Name, Divisional_Charts_NameAdmin)
admin.site.register(Divisional_Charts_Groupings, Divisional_Charts_GroupingsAdmin)
admin.site.register(Rasi_Names_And_Symbols, Rasi_Names_And_SymbolsAdmin)
admin.site.register(rasi_extent_in_zodiac_table, rasi_extent_in_zodiac_tableAdmin)
admin.site.register(nakshatra_under_names_28_scheme_table, nakshatra_under_names_28_scheme_tableAdmin)
admin.site.register(planets_Names_and_symbols_table, planets_Names_and_symbols_tableAdmin)
admin.site.register(Nakshatra_Names_under_27_scheme_Table, Nakshatra_Names_under_27_scheme_TableAdmin)
admin.site.register(Nakshatra_Extent_27_in_terms_of_Degree_table,Nakshatra_Extent_27_in_terms_of_Degree_tableAdmin)
admin.site.register(Nakshatra_Extent_28_in_terms_of_Degree_table,Nakshatra_Extent_28_in_terms_of_Degree_tableAdmin)
admin.site.register(Nakshatra_Pada_Table_under_27_nakshatra_scheme,Nakshatra_Pada_Table_under_27_nakshatra_schemeAdmin)
admin.site.register( Nakshatra_Deity_Devta_for_REMEDIER,Nakshatra_Deity_Devta_for_REMEDIERAdmin)
admin.site.register( Nakshatra_Lord_For_Dasa_Table,Nakshatra_Lord_For_Dasa_TableAdmin)
admin.site.register( Nakshatra_Pada_Rasi_Gyan_Table,Nakshatra_Pada_Rasi_Gyan_TableAdmin)
admin.site.register( Rasi_Ayan_and_Tattva_Table,Rasi_Ayan_and_Tattva_TableAdmin)
admin.site.register( Sapt_Lok_Mandal_Table,Sapt_Lok_Mandal_TableAdmin)
admin.site.register( Savya_Apsavya_Nakshatra_Chakra_Table,Savya_Apsavya_Nakshatra_Chakra_TableAdmin)
admin.site.register( Tri_Loka_Chakra_Table,Tri_Loka_Chakra_TableAdmin)
admin.site.register( Tri_Nadi_Chakra_Table,Tri_Nadi_Chakra_TableAdmin)
admin.site.register( Nakshatra_Tattva_Chakra_Table,Nakshatra_Tattva_Chakra_TableAdmin)
admin.site.register( Tattva_Relationship_Table,Tattva_Relationship_TableAdmin)
admin.site.register( Pushkar_Nakshatra_Table,Pushkar_Nakshatra_TableAdmin)
admin.site.register( Panchak_Nakshatra_Table,Panchak_Nakshatra_TableAdmin)
admin.site.register( Pushkar_Navamsa_Table,Pushkar_Navamsa_TableAdmin)
admin.site.register(Pushkar_Bhaga_Table,Pushkar_Bhaga_TableAdmin)
admin.site.register(Pushkar_Bhaga_Table_Purva_Kalamrit_c_s_patel_Table,Pushkar_Bhaga_Table_Purva_Kalamrit_c_s_patel_TableAdmin)
admin.site.register(Gandanta_Nakshatra_Table,Gandanta_Nakshatra_TableAdmin)
#32-c
admin.site.register(Divisional_Charts_Group_Table, Divisional_Charts_Group_TableAdmin)
admin.site.register(Rashi_Chart_D1_Table,Rashi_Chart_D1_TableAdmin)
admin.site.register(UMA_SHAMBHU_Hora_D2_US_Table, UMA_SHAMBHU_Hora_D2_US_TableAdmin)
admin.site.register(PARASHARI_HORA_D2_PH_Table, PARASHARI_HORA_D2_PH_TableAdmin)
admin.site.register(JAGANNATH_Hora_D2_JH_Table, JAGANNATH_Hora_D2_JH_TableAdmin)
admin.site.register(KASHI_NATH_Hora_D2_KN_Table, KASHI_NATH_Hora_D2_KN_TableAdmin)
admin.site.register(BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G1_Table, BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G1_TableAdmin)
admin.site.register(BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G2_Table, BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G2_TableAdmin)
admin.site.register(SAMA_SAPTAK_Hora_D2_SS_Table, SAMA_SAPTAK_Hora_D2_SS_TableAdmin)
admin.site.register(MANDUKA_Hora_D2_MH_Table, MANDUKA_Hora_D2_MH_TableAdmin)
admin.site.register(GOLA_Hora_D2_GH_Table, GOLA_Hora_D2_GH_TableAdmin)
admin.site.register(BodyMap_MaleChart_Table, BodyMap_MaleChart_TableAdmin)
admin.site.register(BodyMap_FemaleChart_Table, BodyMap_FemaleChart_TableAdmin)
admin.site.register(LABH_MANDOOK_Hora_Table, LABH_MANDOOK_Hora_TableAdmin)
admin.site.register(SAM_MUKHA_RASHI_Table, SAM_MUKHA_RASHI_TableAdmin)
admin.site.register(SAM_MUKHA_Hora_D2_SM_Table, SAM_MUKHA_Hora_D2_SM_TableAdmin)
admin.site.register(SOM_NATH_Hora_D2_SN_Table, SOM_NATH_Hora_D2_SN_TableAdmin)
admin.site.register(PARIVRIITTI_DWAYA_Hora_D2_PD_Table, PARIVRIITTI_DWAYA_Hora_D2_PD_TableAdmin)
admin.site.register(PRASHARI_DREKKANA_D3_PD_Table, PRASHARI_DREKKANA_D3_PD_TableAdmin)
admin.site.register(PARIVITRII_TRAYA_DREKKANA_D3_PT_Table, PARIVITRII_TRAYA_DREKKANA_D3_PT_TableAdmin)
admin.site.register(JAGANNATH_DREKKANA_D3_JD_Table, JAGANNATH_DREKKANA_D3_JD_TableAdmin)
admin.site.register(SOMNATH_M_DREKKANA_D3_SMD_Table, SOMNATH_M_DREKKANA_D3_SMD_TableAdmin)
admin.site.register(PARASHARI_CHATURTHAMSA_OR_TURYA_D4_PC_Table, PARASHARI_CHATURTHAMSA_OR_TURYA_D4_PC_TableAdmin)
admin.site.register(VEDAAMSA_D4_V_Table, VEDAAMSA_D4_V_TableAdmin)
admin.site.register(PARIVRITTI_PANCHAMSHA_D5_PP_Table, PARIVRITTI_PANCHAMSHA_D5_PP_TableaAdmin)
admin.site.register(TAJIK_PANCHAMSHA_D5_TP_Table, TAJIK_PANCHAMSHA_D5_TP_TableAdmin)
admin.site.register(KAULUKA_SHASTAMSA_D6_KS_Table, KAULUKA_SHASTAMSA_D6_KS_TableAdmin)
admin.site.register(PARIVRITTI_SHASHTAMSA_D6_PS_Table, PARIVRITTI_SHASHTAMSA_D6_PS_TableAdmin)
admin.site.register(SAPTAMSHA_D7_Table, SAPTAMSHA_D7_TableAdmin)
admin.site.register(TAJIK_ASHTAMAMSHA_D8_TA_Table, TAJIK_ASHTAMAMSHA_D8_TA_TableAdmin)
admin.site.register(PARASHARI_NAVAMSHA_D9_PN_Table, PARASHARI_NAVAMSHA_D9_PN_TableAdmin)
admin.site.register(SOMNATH_NAVAMSHA_D9_SN_Table, SOMNATH_NAVAMSHA_D9_SN_TableAdmin)
admin.site.register(PADA_NAVAMSHA_D9_PN_Table, PADA_NAVAMSHA_D9_PN_TableAdmin)
admin.site.register(NADI_NAVAMSHA_D9_NN_Table, NADI_NAVAMSHA_D9_NN_TableAdmin)
admin.site.register(DASHAMANSHA_D10_Table, DASHAMANSHA_D10_TableAdmin)
admin.site.register(PARASHARI_RUDRAMSA_D11_PR_Table, PARASHARI_RUDRAMSA_D11_PR_TableAdmin)
admin.site.register(IYER_LABHAMSA_D11_IL_Table, IYER_LABHAMSA_D11_IL_TableAdmin)
admin.site.register(LABHAMSA_D11_Table, LABHAMSA_D11_TableAdmin)
admin.site.register(DVADASHAMSA_D12_Table, DVADASHAMSA_D12_TableAdmin)
admin.site.register(PARASHARI_SODASHAMSA_D16_PS_Table, PARASHARI_SODASHAMSA_D16_PS_TableAdmin)
admin.site.register(IYER_SODASHAMSA_D16_IS_Table, IYER_SODASHAMSA_D16_IS_TableAdmin)
admin.site.register(VIMSAMSHA_D20_Table, VIMSAMSHA_D20_TableAdmin)
admin.site.register(PARASHAR_SIDDHAAMSHA_D24_PSI_Table, PARASHAR_SIDDHAAMSHA_D24_PSI_TableAdmin)
admin.site.register(PARA_VIDHYA_SIDDHAMSHA_D24_PVSI_Table, PARA_VIDHYA_SIDDHAMSHA_D24_PVSI_TableAdmin)
admin.site.register(BHAMSHA_D27_Table, BHAMSHA_D27_TableAdmin)
admin.site.register(PARASHARI_TATTVAMSA_D30_PT_Table, PARASHARI_TATTVAMSA_D30_PT_TableAdmin)
admin.site.register(VENKETSHWAR_TRIMSHAMSA_D30_VT_Table, VENKETSHWAR_TRIMSHAMSA_D30_VT_TableAdmin)
admin.site.register(Khadvedamsa_D40_Table, Khadvedamsa_D40_TableAdmin)
admin.site.register(AKSHAVEDAMSA_D45_Table, AKSHAVEDAMSA_D45_TableAdmin)
admin.site.register(Sastiamsa_D60_Table, Sastiamsa_D60_TableAdmin)
admin.site.register(NavaNavamsha_D81_Table, NavaNavamsha_D81_TableAdmin)
admin.site.register(Ashtottaramsa_D108_Table, Ashtottaramsa_D108_TableAdmin)
admin.site.register(Dwadasamsa_Dwadasamsa_D144_Table, Dwadasamsa_Dwadasamsa_D144_TableAdmin)
#33
admin.site.register(Vaiseshikamsaas_varga_Table, Vaiseshikamsaas_varga_TableAdmin)
admin.site.register(PANCHANG_OVERLORDS_Table, PANCHANG_OVERLORDS_TableAdmin)
admin.site.register(Hora_Table, Hora_TableAdmin)

# admin.site.register(Navatara_Lagna_Table, Navatara_Lagna_TableAdmin)
# admin.site.register(Navatara_Moon_Fixed_Table, Navatara_Moon_Fixed_TableAdmin)
# admin.site.register(Special_Nakshtra_Scheme_Table, Special_Nakshtra_Scheme_TableAdmin)

admin.site.register(Nakshatra_element_works_Table, Nakshatra_element_works_TableAdmin)
admin.site.register(Navratra_Pattern_Table, Navratra_Pattern_TableAdmin)
admin.site.register(Special_Navratra_Pattern_Table, Special_Navratra_Pattern_TableAdmin)
admin.site.register(Nakshatra_sight_Table, Nakshatra_sight_TableAdmin)
admin.site.register(ANDHAADI_NAKSHTRA_Table, ANDHAADI_NAKSHTRA_TableAdmin)
admin.site.register(movability_qualities_nakshatra_Table, movability_qualities_nakshatra_TableAdmin)
admin.site.register(SAPTA_RISHI_BIRTH_SOURCE_Table, SAPTA_RISHI_BIRTH_SOURCE_TableAdmin)
admin.site.register(Natural_Sapt_Rishi_Nakshtra_Table, Natural_Sapt_Rishi_Nakshtra_TableAdmin)
admin.site.register(Characterstic_of_planets_Table, Characterstic_of_planets_TableAdmin)
admin.site.register(Characterstics_of_Signs_Table, Characterstics_of_Signs_TableAdmin)
admin.site.register(Characterstics_of_Houses_Table, Characterstics_of_Houses_TableAdmin)
admin.site.register(Karaka_of_Houses_Table, Karaka_of_Houses_TableAdmin)
admin.site.register(Materialistic_things_differentiation_Table, Materialistic_things_differentiation_TableAdmin)
admin.site.register(Direction_of_planet_dikpala_Table, Direction_of_planet_dikpala_TableAdmin)
admin.site.register(Direction_of_planet_sign_Table, Direction_of_planet_sign_TableAdmin)
admin.site.register(Digbala_of_planet_Table, Digbala_of_planet_TableAdmin)
admin.site.register(Kundalini_chakra_Table, Kundalini_chakra_TableAdmin)
admin.site.register(Combination_of_rising_planets_sings_Table, Combination_of_rising_planets_sings_TableAdmin)
admin.site.register(Gharba_karak_Table, Gharba_karak_TableAdmin)
admin.site.register(Pachaakadi_Sambandha_Table, Pachaakadi_Sambandha_TableAdmin)
admin.site.register(Pachaakadi_Sambandha_B_Table, Pachaakadi_Sambandha_B_TableAdmin)
admin.site.register(Vaar_Chakra_using_7_planets_Table, Vaar_Chakra_using_7_planets_TableAdmin)
admin.site.register(Vaar_Chakra_using_9_planets_Table, Vaar_Chakra_using_9_planets_TableAdmin)
admin.site.register(Houses_from_Pranpada_Lagna_Table, Houses_from_Pranpada_Lagna_TableAdmin)
admin.site.register(Life_cycle_of_creature_Table, Life_cycle_of_creature_TableAdmin)
admin.site.register(Charakarak_bhava_Table, Charakarak_bhava_TableAdmin)
admin.site.register(Form_sun_god_Table, Form_sun_god_TableAdmin)
admin.site.register(Primary_argala_Table, Primary_argala_TableAdmin)
admin.site.register(Secondary_argala_Table, Secondary_argala_TableAdmin)
admin.site.register(Arudha_lagna_determination_Table, Arudha_lagna_determination_TableAdmin)
admin.site.register(Arudha_nomenclature_meaning_Table, Arudha_nomenclature_meaning_TableAdmin)
admin.site.register(Vriddhas_as_per_sahmita_Table, vriddhas_as_per_sahmita_TableAdmin)
admin.site.register(Tattvas_of_nakshatra_Table, tattvas_of_nakshatra_TableAdmin)

admin.site.register(Houses_gunas_Table, Houses_gunas_TableAdmin)
admin.site.register(Devta_guna_arudha_strength_Table, Devta_guna_arudha_strength_TableAdmin)
admin.site.register(Pancha_prana_tattva_graha_Table, Pancha_prana_tattva_graha_TableAdmin)
admin.site.register(Sub_prana_Table, Sub_prana_TableAdmin)
admin.site.register(Rasi_graha_varna_Table, Rasi_graha_varna_TableAdmin)
admin.site.register(Loka_pala_Table, Loka_pala_TableAdmin)
admin.site.register(Upa_graha_list_Table, Upa_graha_list_TableAdmin)
admin.site.register(Special_points_list_Table, Special_points_list_TableAdmin)
admin.site.register(Initiation_chart_list_Table, Initiation_chart_list_TableAdmin)
admin.site.register(Name_of_main_topics_Table, Name_of_main_topics_TableAdmin)
admin.site.register(Bhava_arudha_list_Table, Bhava_arudha_list_TableAdmin)
admin.site.register(Graha_arudha_list_Table, Graha_arudha_list_TableAdmin)
admin.site.register(Nakshatra_Table_For_Vimshottari_Dasa_Table, Nakshatra_Table_For_Vimshottari_Dasa_TableAdmin)
admin.site.register(Vimshottari_Dasa_Planetary_Sequence_Table, Vimshottari_Dasa_Planetary_Sequence_TableAdmin)
admin.site.register(Time_Zone_Rest_Of_The_World_Table, Time_Zone_Rest_Of_The_World_TableAdmin)
admin.site.register(Us_Time_Zones_By_State_Table, Us_Time_Zones_By_State_TableAdmin)
admin.site.register(Russia_Time_Zones_By_City_Table, Russia_Time_Zones_By_City_TableAdmin)
admin.site.register(Canada_Time_Zones_By_Province_Territory_Table, Canada_Time_Zones_By_Province_Territory_TableAdmin)
admin.site.register(Dst_Us_Correction_Timing_Table, Dst_Us_Correction_Timing_TableAdmin)
admin.site.register(Dst_Russia_Correction_Timing_Table, Dst_Russia_Correction_Timing_TableAdmin)
admin.site.register(Dst_Canada_Correction_Timing_Table, Dst_Canada_Correction_Timing_TableAdmin)
admin.site.register(Karana_Table, Karana_TableAdmin)
admin.site.register(Natal_First_Time_Table, Natal_First_Time_TableAdmin)
admin.site.register(User_Registration_Table, User_Registration_TableAdmin)   
admin.site.register(User_Setting_Table, User_Setting_TableAdmin)
admin.site.register(Ashtottari_Dasa_Table, Ashtottari_Dasa_TableAdmin)