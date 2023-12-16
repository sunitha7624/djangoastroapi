from django.db import models

# Create your models here.

class Biodata(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    dateOfBirth = models.DateField(null=False)
    
            

class Tithi(models.Model):
    tithi = models.CharField(max_length=20, db_column='Tithi Code', blank=True)
    tithiName = models.CharField(max_length=40 ,db_column='Name of Tithi', blank=True)
    paksha = models.CharField(max_length=40, blank=True)
    englishName = models.CharField(max_length=20, db_column='English Name' ,blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)

    class Meta:
        verbose_name = '25. Tithi Table'
        verbose_name_plural = '25. Tithi Table'

class Tithi_Graha_Lordship(models.Model):
    tithi = models.CharField(max_length=20, db_column='Tithi Code', blank=True)
    tithi_name = models.CharField(max_length=30, db_column='Tithi Name', blank=True)
    planetary_lordship = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name = '26. Tithi Graha Lordship Table'
        verbose_name_plural = '26. Tithi Graha Lordship Table'

class Tithi_Group_Tattva_Lordship(models.Model):
    tithi = models.CharField(max_length=20, db_column='Tithi Code', blank=True)
    tithi_name = models.CharField(max_length=30, db_column='Tithi Name', blank=True)
    tithi_type = models.CharField(max_length=20, db_column='Tithi Type(Group)', blank=True)
    tithi_element = models.CharField(max_length=20, blank=True)
    element_lords = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name = '27. Tithi Group & Tattva lordship Table'
        verbose_name_plural = '27. Tithi Group & Tattva lordship Table'

class Vara_Lords(models.Model):
    day = models.CharField(max_length=30, blank=True)
    day_lord = models.CharField(max_length=30, blank=True)
    element_lord = models.CharField(max_length=30, blank=True)
    aaditya = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name = '29. Vara Lords Table'
        verbose_name_plural = '29. Vara Lords Table'

class Rivers_Dieties(models.Model):
    sign = models.CharField(max_length=10, blank=True)
    river_sanskrit_name = models.CharField(max_length=20, blank=True)
    river_modern_name = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=20, blank=True)
    aaditya = models.CharField(max_length=40, blank=True)
    aaditya_name = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name = '30. Rivers and Deities Table'
        verbose_name_plural = '30. Rivers and Deities Table'

class Gandanta_Rashi(models.Model):
    serial_no = models.IntegerField(default=0, blank=True)
    gandanta_name = models.CharField(max_length=10, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='Extent From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='Extent To (SS-DD-MM-SS)', blank=True)

    class Meta:
        verbose_name = '31. Gandanta Rashi Table'
        verbose_name_plural = '31. Gandanta Rashi Table'

class Divisional_Charts_Cycle(models.Model):
    level_of_conciuosness = models.CharField(max_length=10, blank=True)
    cycle_harmonic = models.CharField(max_length=30, blank=True)
    divisional_chart_range = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = '32.1: Divisional Charts Cycle Table Code 32-A'
        verbose_name_plural = '32.1: Divisional Charts Cycle Table Code 32-A'

class Divisional_Charts_Name(models.Model):
    short_name = models.CharField(max_length=10, blank=True)
    divisional_chart_name = models.CharField(max_length=30, blank=True)
    sub_division_chart_name = models.CharField(max_length=20, blank=True)
    glyph = models.CharField(max_length=10, blank=True)
    table = models.CharField(max_length=5, blank=True)

    class Meta:
        verbose_name = '32.2: Divisional Charts Names Table Code 32-B'
        verbose_name_plural = '32.2: Divisional Charts Names Table Code 32-B'
    
class Divisional_Charts_Groupings(models.Model):
    S_no = models.IntegerField(default=0, blank=True)
    name_of_group = models.CharField(max_length=20, blank=True)
    charts_in_group = models.CharField(max_length=5, blank=True)

class Rasi_Names_And_Symbols(models.Model):
    sign_name_english = models.CharField(max_length=30, blank=True)
    short_name_english= models.CharField(max_length=30, blank=True)
    sign_name_hindi = models.CharField(max_length=30, blank=True)
    short_name_hindi = models.CharField(max_length=30, blank=True)
    sign_glyph = models.CharField(max_length=30, blank=True)
    numeric_value = models.CharField(max_length=30, blank=True)
    lord = models.CharField(max_length=30, blank=True)
    lord_glyph = models.CharField(max_length=30, blank=True)
    lord_name = models.CharField(max_length=30, blank=True)
    chara_karak =models.CharField(max_length=30, blank=True)
    



    class Meta:
        verbose_name = ' 1. Rasi Names & Symbols Table'
        verbose_name_plural = ' 1. Rasi Names & Symbols Table'
    
class rasi_extent_in_zodiac_table(models.Model):
    rashi=models.CharField(max_length=30, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='Extent From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='Extent To (SS-DD-MM-SS)', blank=True)
    NUMERIC_VALUE_DENOTING_Rasi=models.IntegerField(default=0, db_column='Numeric Value denoting Rasi', blank=True)

    class Meta:
        verbose_name = ' 2. Rasi Extent in zodiac Table'
        verbose_name_plural = ' 2. Rasi Extent in zodiac Table'

class nakshatra_under_names_28_scheme_table(models.Model):
    nakshatra_no = models.IntegerField(default=0)
    nakshatra_name_english = models.CharField(max_length=30, blank=True)
    short_name_english = models.CharField(max_length=30, blank=True)
    nakshatra_name_hindi = models.CharField(max_length=30, blank=True)
    short_name_hindi = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = ' 6. Nakshatra names under 28 scheme Table'
        verbose_name_plural = ' 6. Nakshatra names under 28 scheme Table'

class planets_Names_and_symbols_table(models.Model):
    planets_name_english = models.CharField(max_length=30, blank=True)
    short_name_english = models.CharField(max_length=30, blank=True)
    planets_name_hindi = models.CharField(max_length=30, blank=True)
    short_name_hindi = models.CharField(max_length=30, blank=True)
    planet_gyph = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = ' 3. Planets Names & symbols Table'
        verbose_name_plural = ' 3. Planets Names & symbols Table'

class Nakshatra_Names_under_27_scheme_Table(models.Model) :
    Nakshatra_no = models.IntegerField(default=0, blank=True)
    Nakshatra_name_english = models.CharField(max_length=30, blank=True)
    short_name_english = models.CharField(max_length=30, blank=True)
    Nakshatra_name_hindi = models.CharField(max_length=30, blank=True)
    short_name_hindi = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = ' 4. Nakshatra Names under 27 scheme Table'
        verbose_name_plural = ' 4. Nakshatra Names under 27 scheme Table'

class Nakshatra_Extent_27_in_terms_of_Degree_table(models.Model) :
    nakshatra_no = models.IntegerField(default=0, blank=True)
    Nakshatra_name_symbol = models.CharField(max_length=30, db_column='Nakshatra Name', blank=True)
    Nakshatra_lord = models.CharField(max_length=30, db_column='Nakshatra Lord', blank=True)
    Nakshatra_diety = models.CharField(max_length=30,db_column='Nakshatra Diety', blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='Extent From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='Extent To (SS-DD-MM-SS)', blank=True)

    class Meta:
        verbose_name = ' 5. Nakshatra Extent(27) in terms of Degree Table'
        verbose_name_plural = ' 5. Nakshatra Extent(27) in terms of Degree Table'

class Nakshatra_Extent_28_in_terms_of_Degree_table(models.Model):
    nakshatra_no = models.IntegerField(default=0, blank=True)
    Nakshatra_name_symbol = models.CharField(max_length=30, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='Extent From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='Extent To (SS-DD-MM-SS)', blank=True)

    class Meta:
        verbose_name = ' 7. Nakshatra Extent(28) in terms of Degree Table'
        verbose_name_plural = ' 7. Nakshatra Extent(28) in terms of Degree Table'

class Nakshatra_Pada_Table_under_27_nakshatra_scheme(models.Model):
    nakshatra_no = models.IntegerField(default=0, blank=True)
    name_of_nashapada = models.CharField(max_length=30, db_column='Nakshatra Name',blank=True)
    pada = models.CharField(max_length=30, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='Extent From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='Extent To (SS-DD-MM-SS)', blank=True)

    class Meta:
        verbose_name = ' 8. Nakshatra Pada Table under 27 nakshatra scheme '
        verbose_name_plural = ' 8. Nakshatra Pada Table under 27 nakshatra scheme '

class Nakshatra_Lord_For_Dasa_Table(models.Model):
    s_no = models.IntegerField(default=0, verbose_name='SERIAL No.',blank=True)
    class_dasa = models.CharField(max_length=30,verbose_name='CLASS OF DASA', blank=True)
    type_dasa = models.CharField(max_length=30,verbose_name='TYPE OF DASA', blank=True)
    lord_dasa = models.CharField(max_length=30,verbose_name='LORD OF DASA', blank=True)
    name_of_nakshatra = models.CharField(max_length=30, verbose_name='NAME OF NAKSHTRA', blank=True)
    from_extent = models.CharField(max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='Extent From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='Extent To (SS-DD-MM-SS)', blank=True)
    lord_nakshtra = models.CharField(max_length=30, db_column='LORD OF NAKSHTRA', verbose_name='LORD OF NAKSHTRA', blank=True)
    period_dasa = models.CharField(max_length=30, db_column='PERIOD OF DASA (YY-MM-DD)', verbose_name='PERIOD OF DASA (YY-MM-DD)', blank=True)

    class Meta:
        verbose_name = ' 9. Nakshatra Lord(For Dasa) Table'
        verbose_name_plural = ' 9. Nakshatra Lord(For Dasa) Table'

class Nakshatra_Deity_Devta_for_REMEDIER(models.Model):
    nakshatra_no = models.IntegerField(default=0, blank=True)
    nakshatra_name = models.CharField(default = '', max_length=30, blank=True)
    deity_as_per_harihar = models.CharField(max_length=30, db_column='Deity as per Harihar Mazumdar', verbose_name='Deity as per Harihar Mazumdar', blank=True)
    deity_as_per_atharva = models.CharField(max_length=30, db_column='Deity as per Atharva Veda', verbose_name='Deity as per Atharva Veda', blank=True)
    rsi_as_per_atharva = models.CharField(max_length=30, db_column='Rsi as per Atharva Veda', verbose_name='Rsi as per Atharva Veda', blank=True)
    diety_as_per_varahmihir = models.CharField(max_length=30, db_column='Deity as per Varahmihir', verbose_name='Deity as per Varahmihir', blank=True)    
    diety_as_per_lagadha = models.CharField(max_length=30, db_column='Deity as per Lagadha', verbose_name='Deity as per Lagadha', blank=True)    

    class Meta:
        verbose_name = '10. Nakshatra Deity (Devta) for REMEDIES Table'
        verbose_name_plural = '10. Nakshatra Deity (Devta) for REMEDIES Table'

class Nakshatra_Pada_Rasi_Gyan_Table(models.Model):
    sign_no = models.IntegerField(default=0, blank=True)
    sign_name = models.CharField(max_length=30, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='Extent From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='Extent To (SS-DD-MM-SS)', blank=True)
    first_nakshatra_pada= models.CharField(default = '', max_length = 30, db_column='First Nakshatra / Pada', verbose_name='First Nakshtra', blank=True)
    first_no_pada = models.CharField(default = '',max_length = 30, db_column='(First) No of padas', verbose_name='No of Pada(s)', blank=True)
    second_nakshatra_pada = models.CharField(default = '', max_length = 30, db_column='Second Nakshatra / Pada', verbose_name='Second Nakshtra', blank=True)
    second_no_pada = models.CharField(default = '',max_length = 30, db_column='(Second) No of padas', verbose_name='No of Pada(s)', blank=True)
    third_nakshatra_pada = models.CharField(default = '', max_length = 30, db_column='Third Nakshatra / Pada', verbose_name='Third Nakshtra', blank=True)
    third_no_pada = models.CharField(default = '',max_length = 30, db_column='(Third) No of padas', verbose_name='No of Pada(s)', blank=True)
    total_padas_in_each_rasi = models.CharField(max_length=30, verbose_name='Total Padas in each Rasi', blank=True)

    class Meta:
        verbose_name = '11. Nakshatra Pada Rasi Gyan Table'
        verbose_name_plural = '11. Nakshatra Pada Rasi Gyan Table'

class Rasi_Ayan_and_Tattva_Table(models.Model):
    sign_no = models.IntegerField(default=0, blank=True)
    sign_name = models.CharField(max_length=30, blank=True)
    ayan = models.CharField(max_length=30, blank=True)
    element = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = '12. Rasi Ayan & Tattva Table'
        verbose_name_plural = '12. Rasi Ayan & Tattva Table'
    
class Sapt_Lok_Mandal_Table(models.Model):
    plane_loka = models.CharField(max_length=30, db_column='PLANE (LOKA)', blank=True)
    signifactor = models.CharField(max_length=30, blank=True)
    chakra_in_body = models.CharField(max_length=30, blank=True)
    meaning = models.CharField(max_length=30, blank=True)
    devta = models.CharField(max_length=30, blank=True)
    bija = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = '13. Sapt Lok Mandal Table'
        verbose_name_plural = '13. Sapt Lok Mandal Table'

class Tri_Loka_Chakra_Table(models.Model):
    loka = models.CharField(max_length=30, blank=True)
    constallation_no_1 = models.IntegerField(default=0, db_column='1st Constellation No', verbose_name='1st Constellation No:',blank=True)
    constallation_1 = models.CharField(max_length=30, db_column='1st Constellation Name', verbose_name='1st Constellation Name',blank=True)
    constallation_no_2 = models.IntegerField(default=0, db_column='2nd Constellation No', verbose_name='2nd Constellation No',blank=True)
    constallation_2 = models.CharField(max_length=30, db_column='2nd Constellation Name', verbose_name='2nd Constellation Name',blank=True)
    constallation_no_3 = models.IntegerField(default=0, db_column='3rd Constellation No', verbose_name='3rd Constellation No',blank=True)
    constallation_3 = models.CharField(max_length=30, db_column='3rd Constellation Name', verbose_name='3rd Constellation Name',blank=True)
    constallation_no_4 = models.IntegerField(default=0, db_column='4th Constellation No', verbose_name='4th Constellation No',blank=True)
    constallation_4 = models.CharField(max_length=30, db_column='4th Constellation Name', verbose_name='4th Constellation Name',blank=True)
    constallation_no_5 = models.IntegerField(default=0, db_column='5th Constellation No', verbose_name='5th Constellation No',blank=True)
    constallation_5 = models.CharField(max_length=30, db_column='5th Constellation Name', verbose_name='5th Constellation Name',blank=True)
    constallation_no_6 = models.IntegerField(default=0, db_column='6th Constellation No',verbose_name='6th Constellation No', blank=True)
    constallation_6 = models.CharField(max_length=30, db_column='6th Constellation Name', verbose_name='6th Constellation Name',blank=True)
    constallation_no_7 = models.IntegerField(default=0, db_column='7th Constellation No', verbose_name='7th Constellation No',blank=True)
    constallation_7 = models.CharField(max_length=30, db_column='7th Constellation Name',verbose_name='7th Constellation Name', blank=True)
    constallation_no_8 = models.IntegerField(default=0, db_column='8th Constellation No', verbose_name='8th Constellation No',blank=True)
    constallation_8 = models.CharField(max_length=30, db_column='8th Constellation Name', verbose_name='8th Constellation Name',blank=True)
    constallation_no_9 = models.IntegerField(default=0, db_column='9th Constellation No', verbose_name='9th Constellation No',blank=True)
    constallation_9 = models.CharField(max_length=30, db_column='9th Constellation Name', verbose_name='9th Constellation Name',blank=True)

    class Meta:
        verbose_name = '14. Tri-Loka Chakra Table'
        verbose_name_plural = '14.Tri-Loka Chakra Table'

class Savya_Apsavya_Nakshatra_Chakra_Table(models.Model):
    group = models.IntegerField(default=0, verbose_name='GROUP',blank=True)
    motion = models.CharField(max_length=30, verbose_name='MOTION',blank=True)
    constallation_no_1 = models.IntegerField(default=0, db_column='First Constellation No', verbose_name='CONSTELLATION No', blank=True)
    constallation_1 = models.CharField(max_length=30, db_column='First Constellation Name', verbose_name='1ST CONSTELATION NAME',blank=True)
    constallation_no_2 = models.IntegerField(default=0, db_column='Second Constellation No',verbose_name='CONSTELLATION No',  blank=True)
    constallation_2 = models.CharField(max_length=30, db_column='Second Constellation Name',verbose_name='2ND CONSTELATION NAME', blank=True)
    constallation_no_3 = models.IntegerField(default=0, db_column='Third Constellation No',verbose_name='CONSTELLATION No',  blank=True)
    constallation_3 = models.CharField(max_length=30, db_column='Third Constellation Name',verbose_name='3RD CONSTELATION NAME', blank=True)

    class Meta:
        verbose_name = '15. Savya Apsavya Nakshatra Chakra Table'
        verbose_name_plural = '15.  Savya Apsavya Nakshatra Chakra Table'

class Tri_Nadi_Chakra_Table(models.Model):
    nadi = models.CharField(max_length=30, db_column='NADI', verbose_name='NADI',blank=True)
    Srota = models.CharField(max_length=30, db_column='Srota', verbose_name='Srota',blank=True)
    naadi = models.CharField(max_length=30, db_column='Naadi', verbose_name='Naadi',blank=True)
    flow = models.CharField(max_length=30, db_column='Flow', verbose_name='Flow',blank=True)
    devta = models.CharField(max_length=30, db_column='Devta', verbose_name='Devta',blank=True)
    purpose = models.CharField(max_length=30, db_column='Purpose', verbose_name='Purpose',blank=True)
    trimurti = models.CharField(max_length=30, db_column='Trimurti', verbose_name='Trimurti',blank=True)
    humour = models.CharField(max_length=30, db_column='Humour', verbose_name='Humour',blank=True)
    nakshatra_dir_1 = models.CharField(max_length=30, db_column='1st Nakshatra Direction', verbose_name='1st Nakshatra Direction',blank=True)
    nakshatra_no_1 = models.CharField(max_length=30, db_column='1st Nakshatra No', verbose_name='1st Nakshatra No',blank=True)
    nakshatra_name_1 = models.CharField(max_length=30, db_column='1st Nakshatra Name', verbose_name='1st Nakshatra Name',blank=True)
    nakshatra_dir_2 = models.CharField(max_length=30, db_column='2nd Nakshatra Direction', verbose_name='2nd Nakshatra Direction',blank=True)
    nakshatra_no_2 = models.CharField(max_length=30, db_column='2nd Nakshatra No', verbose_name='2nd Nakshatra No',blank=True)
    nakshatra_name_2 = models.CharField(max_length=30, db_column='2nd Nakshatra Name', verbose_name='2nd Nakshatra Name',blank=True)
    nakshatra_dir_3 = models.CharField(max_length=30, db_column='3rd Nakshatra Direction', verbose_name='3rd Nakshatra Direction',blank=True)
    nakshatra_no_3 = models.CharField(max_length=30, db_column='3rd Nakshatra No', verbose_name='3rd Nakshatra No',blank=True)
    nakshatra_name_3 = models.CharField(max_length=30, db_column='3rd Nakshatra Name', verbose_name='3rd Nakshatra Name',blank=True)
    nakshatra_dir_4 = models.CharField(max_length=30, db_column='4th Nakshatra Direction', verbose_name='4th Nakshatra Direction',blank=True)
    nakshatra_no_4 = models.CharField(max_length=30, db_column='4th Nakshatra No', verbose_name='4th Nakshatra No',blank=True)
    nakshatra_name_4 = models.CharField(max_length=30, db_column='4th Nakshatra Name', verbose_name='4th Nakshatra Name',blank=True)
    nakshatra_dir_5 = models.CharField(max_length=30, db_column='5th Nakshatra Direction', verbose_name='5th Nakshatra Direction',blank=True)
    nakshatra_no_5 = models.CharField(max_length=30, db_column='5th Nakshatra No', verbose_name='5th Nakshatra No',blank=True)
    nakshatra_name_5 = models.CharField(max_length=30, db_column='5th Nakshatra Name', verbose_name='5th Nakshatra Name',blank=True)
    nakshatra_dir_6 = models.CharField(max_length=30, db_column='6th Nakshatra Direction', verbose_name='6th Nakshatra Direction',blank=True)
    nakshatra_no_6 = models.CharField(max_length=30, db_column='6th Nakshatra No', verbose_name='6th Nakshatra No',blank=True)
    nakshatra_name_6 = models.CharField(max_length=30, db_column='6th Nakshatra Name', verbose_name='6th Nakshatra Name',blank=True)
    nakshatra_dir_7 = models.CharField(max_length=30, db_column='7th Nakshatra Direction', verbose_name='7th Nakshatra Direction',blank=True)
    nakshatra_no_7 = models.CharField(max_length=30, db_column='7th Nakshatra No', verbose_name='7th Nakshatra No',blank=True)
    nakshatra_name_7 = models.CharField(max_length=30, db_column='7th Nakshatra Name', verbose_name='7th Nakshatra Name',blank=True)
    nakshatra_dir_8 = models.CharField(max_length=30, db_column='8th Nakshatra Direction', verbose_name='8th Nakshatra Direction',blank=True)
    nakshatra_no_8 = models.CharField(max_length=30, db_column='8th Nakshatra No', verbose_name='8th Nakshatra No',blank=True)
    nakshatra_name_8 = models.CharField(max_length=30, db_column='8th Nakshatra Name', verbose_name='8th Nakshatra Name',blank=True)
    nakshatra_dir_9 = models.CharField(max_length=30, db_column='9th Nakshatra Direction', verbose_name='9th Nakshatra Direction',blank=True)
    nakshatra_no_9 = models.CharField(max_length=30, db_column='9th Nakshatra No', verbose_name='9th Nakshatra No',blank=True)
    nakshatra_name_9 = models.CharField(max_length=30, db_column='9th Nakshatra Name', verbose_name='9th Nakshatra Name',blank=True)

    class Meta:
        verbose_name = '16. Tri Nadi Chakra Table'
        verbose_name_plural = '16. Tri Nadi Chakra Table'

class Nakshatra_Tattva_Chakra_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No',blank=True)
    element_tattva = models.CharField(max_length=30, db_column='ELEMENT/ TATTVA', verbose_name='ELEMENT/ TATTVA', blank=True)
    earth_prithvi = models.CharField(max_length=30, db_column='EARTH(PRITHVI)', verbose_name='EARTH(PRITHVI)',blank=True)
    water_jala = models.CharField(max_length=30, db_column='WATER(JALA)', verbose_name='WATER(JALA)',blank=True)
    fire_agni = models.CharField(max_length=30, db_column='FIRE(AGNI)', verbose_name='FIRE(AGNI)',blank=True)
    air_vaayu = models.CharField(max_length=30, db_column='AIR( VAAYU)', verbose_name='AIR( VAAYU)',blank=True)
    sky_akash = models.CharField(max_length=30, db_column='SKY(AKASH)', verbose_name='SKY(AKASH)',blank=True)
    
    class Meta:
        verbose_name = '17. Nakshatra Tattva Chakra Table'
        verbose_name_plural = '17. Nakshatra Tattva Chakra Table'
        ordering = ['S_No']

class Tattva_Relationship_Table(models.Model):
    serial_no = models.IntegerField(default=0, blank=True)
    ELEMENT_TATTVA = models.CharField(max_length=30, db_column='Element(Tattva)',blank=True)
    friend = models.CharField(max_length=30,blank=True)
    ENMITY = models.CharField(max_length=30, blank=True)
    NEUTRAL = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = '18. Tattva Relationship Table'
        verbose_name_plural = '18. Tattva Relationship Table'

class Pushkar_Nakshatra_Table(models.Model):
    types_of_pushkar_nakshtra = models.CharField(max_length=30, db_column='Type of Pushkar Nakshatra', blank=True)
    no_of_nakshtra = models.CharField(max_length=30, db_column='Number of Nakshatra', blank=True)
    name_of_nakshatra = models.CharField(max_length=30, db_column='Name of Nakshatra', blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    owner_of_nakshtra = models.CharField(max_length=30, blank=True)
    effect = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = '19. Pushkar Nakshatra Table'
        verbose_name_plural = '19. Pushkar Nakshatra Table'

class Panchak_Nakshatra_Table(models.Model):
    special_name = models.CharField(max_length=30, db_column='Special Name of nakshatra', verbose_name='Special Name of nakshatra',blank=True)
    sign_rasi = models.CharField(max_length=30, db_column='Sign', blank=True)
    nakshtra = models.CharField(max_length=30, db_column='Nakshatra Number', verbose_name='Nakshatra No.', blank=True)
    nakshtra_name = models.CharField(max_length=30, db_column='Nakshatra Name', verbose_name='Nakshatra Name', blank=True)
    padas = models.CharField(max_length=30, db_column='pada', blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)

    class Meta:
        verbose_name = '20. Panchak Nakshatra Table'
        verbose_name_plural = '20. Panchak Nakshatra Table'

class Pushkar_Navamsa_Table(models.Model):
    sign = models.CharField(max_length=30, blank=True)
    element_of_sign = models.CharField(max_length=30, db_column='Element Of Sign', verbose_name='Element Of Sign',blank=True)
    CONSTELLATION_No = models.IntegerField(default=0, blank=True)
    constallation = models.CharField(max_length=30, verbose_name='CONSTELLATION Name', blank=True)
    pada = models.CharField(max_length=30, verbose_name='Pada Of Constellation',blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    navamsa_sign = models.CharField(max_length=30, db_column='Navamsa Sign', verbose_name='NAVAMSA SIGN',blank=True)
    sign_no_navamsa = models.CharField(max_length=30, db_column='Sign Number of Navamsa', verbose_name='Sign No. of Navamsa where body/planet is posted', blank=True)

    class Meta:
        verbose_name = '21. Pushkar Navamsa Table'
        verbose_name_plural = '21. Pushkar Navamsa Table'

class Pushkar_Bhaga_Table(models.Model):
    sign = models.CharField(max_length=30, blank=True)
    element_of_sign = models.CharField(max_length=30, blank=True)
    constallation_no = models.IntegerField(default=0, blank=True)
    constallation = models.CharField(max_length=30, blank=True)
    pada = models.CharField(max_length=30, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    exact_extent = models.CharField(default = '', max_length = 30, db_column='Exact (SS-DD-MM-SS)', verbose_name='Exact (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    navamsa_sign = models.CharField(max_length=30, db_column='Navamsa Sign', blank=True)
    sign_no_navamsa = models.CharField(max_length=30, verbose_name='Sign No. of Navamsa where body/planet is posted', blank=True)

    class Meta:
        verbose_name = '22. Pushkar Bhaga Table (JATAK PARIJAT DEFINITION)'
        verbose_name_plural = '22. Pushkar Bhaga Table (JATAK PARIJAT DEFINITION)'

class Pushkar_Bhaga_Table_Purva_Kalamrit_c_s_patel_Table(models.Model):
    sign = models.CharField(max_length=30, blank=True)
    element_of_sign = models.CharField(max_length=30, blank=True)
    constallation_no = models.IntegerField(default=0, blank=True)
    constallation = models.CharField(max_length=30, blank=True)
    pada = models.CharField(max_length=30, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    exact_extent = models.CharField(default = '', max_length = 30, db_column='Exact (SS-DD-MM-SS)', verbose_name='Exact (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    navamsa_sign = models.CharField(max_length=30, db_column='Navamsa Sign', blank=True)
    sign_no_navamsa = models.CharField(max_length=30, verbose_name='Sign No. of Navamsa where body/planet is posted', blank=True)

    class Meta:
        verbose_name = '23. Pushkar Bhaga Table (Purva Kalamrit/c.s.patel)'
        verbose_name_plural = '23. Pushkar Bhaga Table (Purva Kalamrit/c.s.patel)'

class Gandanta_Nakshatra_Table(models.Model):
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    gandanta_name = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = '31. Gandanta Nakshatra Table'
        verbose_name_plural = '31. Gandanta Nakshatra Table'

class Divisional_Charts_Group_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=True)
    name_group = models.CharField(default='', max_length=20, db_column='NAME OF THE GROUP', verbose_name='NAME OF THE GROUP', blank=True)
    divisional_Charts_Groups = models.CharField(default='', max_length=20, db_column='DIVISIONAL CHARTS IN THE GROUP', verbose_name='DIVISIONAL CHARTS IN THE GROUP', blank=True)
    no_divisional_charts = models.CharField(default='', max_length=20, db_column='No OF DIVISIONAL CHARTS', verbose_name='No OF DIVISIONAL CHARTS', blank=True)
    applies_to = models.CharField(default='', max_length=20, db_column='APPLIES To', verbose_name='APPLIES TO', blank=True)

    class Meta:
        verbose_name = '32.3: Divisional Charts Group Table Code 32-C'
        verbose_name_plural = '32.3: Divisional Charts Group Table Code 32-C'

class Rashi_Chart_D1_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    DEVTA = models.CharField(default='', max_length=30, blank=True)

    class Meta:
        verbose_name = '32.4. Table Name: Rasi Chart, Table Code: 32-D'
        verbose_name_plural = '32.4. Table Name: Rasi Chart, Table Code: 32-D'

class UMA_SHAMBHU_Hora_D2_US_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    DEVTA = models.CharField(default='', max_length=30, blank=True)
   

    class Meta:
        verbose_name = '32.5. Table Name: Uma-Shambhu Hora D-2(US) Table Code: 32-E'
        verbose_name_plural = '32.5. Table Name: Uma-Shambhu Hora D-2(US) Table Code: 32-E'

class PARASHARI_HORA_D2_PH_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    DEVTA = models.CharField(default='', max_length=30, blank=True)
   

    class Meta:
        verbose_name = '32.6. Table Name: Parashari Hora D2(PH) Table Code:32-F'
        verbose_name_plural = '32.6. Table Name: Parashari Hora D2(PH) Table Code:32-F'

class JAGANNATH_Hora_D2_JH_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    DEVTA = models.CharField(default='', max_length=30, blank=True)
    class Meta:
        verbose_name = '32.7. Table Name: Jagannath Hora D2(JH) Table Code: 32-G'
        verbose_name_plural = '32.7. Table Name: Jagannath Hora D2(JH) Table Code: 32-G'

class KASHI_NATH_Hora_D2_KN_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    DEVTA = models.CharField(default='', max_length=30, blank=True)
    class Meta:
        verbose_name = '32.8. Table Name: Kashinath Hora D-2(KN) Table Code: 32-H'
        verbose_name_plural = '32.8. Table Name: Kashinath Hora D-2(KN) Table Code: 32-H'


class BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G1_Table(models.Model):
    SIGN = models.CharField(default='', max_length=10, blank=True)
    CATEGORY = models.CharField(default='', verbose_name='CATEGORY', max_length=10, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    hora_lord = models.CharField(default='', verbose_name='HORA LORD', max_length=25, blank=True)

    class Meta:
        verbose_name = '32.9. Table Name: Bifurcation of Zodiac as per Saravali Table Code: 32-G1'
        verbose_name_plural = '32.9. Table Name: Bifurcation of Zodiac as per Saravali Table Code: 32-G1'
    
class BIFURCATION_OF_ZODIAC_AS_PER_SARAVALI_G2_Table(models.Model):
    SECTION = models.CharField(default='', max_length=10, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    from_extent1 = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)-1', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent1 = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)-1', verbose_name='To (SS-DD-MM-SS)', blank=True)
    hora_lord1 = models.CharField(default='', max_length=20, db_column='HORA LORD-1', verbose_name='HORA LORD', blank=True)

    class Meta:
        verbose_name = '32.10. Table Name: Bifurcation of Zodiac as per Saravali Table Code: 32-G2'
        verbose_name_plural = '32.10. Table Name: Bifurcation of Zodiac as per Saravali Table Code: 32-G2'

class SAMA_SAPTAK_Hora_D2_SS_Table(models.Model):
    planet_sign = models.CharField(default='', max_length=20, db_column='IF THE BODY IS IN THE SIGN', verbose_name='IF THE BODY IS IN THE SIGN', blank=True)
    if_in_group = models.CharField(default='', max_length=20, db_column = 'IF THE BODY IS IN THE GROUP', verbose_name='IF THE BODY IS IN THE GROUP', blank=True)
    if_in_section = models.CharField(default='', max_length=20, db_column = 'IF THE BODY IS IN THE CATEGORY', verbose_name='IF THE BODY IS IN THE CATEGORY', blank=True)
    body_placed = models.CharField(default='', max_length=20, db_column = 'THE NUMERIC VALUE WHERE THE PLANET/BODY IS POSTED in SAMA-SAPTAK HORA/JAGANNATH HORA', verbose_name='THE NUMERIC VALUE WHERE THE PLANET/BODY IS POSTED in SAMA-SAPTAK HORA/JAGANNATH HORA', blank=True)

    class Meta:
        verbose_name = '32.11. Table Name: Sama Saptak Hora D-2(SS) Table Code: 32-I'
        verbose_name_plural = '32.11. Table Name: Sama Saptak Hora D-2(SS) Table Code: 32-I'

class MANDUKA_Hora_D2_MH_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)

    class Meta:
        verbose_name = '32.13. Table Name: Manduka Hora D-2(MH) Table Code: 32-J'
        verbose_name_plural = '32.13. Table Name: Manduka Hora D-2(MH) Table Code: 32-J'

class GOLA_Hora_D2_GH_Table(models.Model):
    SECTION = models.CharField(default='', max_length=10, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    if_body_d1 = models.CharField(default='', max_length=20, db_column='D1 Placement', verbose_name='IF BODY IS PLACED IN HOUSES IN D1 CHART', blank=True)
    then_body_gola = models.CharField(default='', max_length=20, db_column='Gola Placement', verbose_name='THEN BODY IS PLACED IN HOUSE IN GOLA HORA', blank=True)
    if_body_d1_1 = models.CharField(default='', max_length=20, db_column='D1 Placement-1', verbose_name='IF BODY IS PLACED IN HOUSES IN D1 CHART', blank=True)
    then_body_gola_1 = models.CharField(default='', max_length=20, db_column='Gola Placement-1', verbose_name='THEN BODY IS PLACED IN HOUSE IN GOLA HORA', blank=True)
    if_body_d1_2 = models.CharField(default='', max_length=20, db_column='D1 Placement-2', verbose_name='IF BODY IS PLACED IN HOUSES IN D1 CHART', blank=True)
    then_body_gola_2 = models.CharField(default='', max_length=20, db_column='Gola Placement-2', verbose_name='THEN BODY IS PLACED IN HOUSE IN GOLA HORA', blank=True)
    if_body_d1_3 = models.CharField(default='', max_length=20, db_column='D1 Placement-3', verbose_name='IF BODY IS PLACED IN HOUSES IN D1 CHART', blank=True)
    then_body_gola_3 = models.CharField(default='', max_length=20, db_column='Gola Placement-3', verbose_name='THEN BODY IS PLACED IN HOUSE IN GOLA HORA', blank=True)
    if_body_d1_4 = models.CharField(default='', max_length=20, db_column='D1 Placement-4', verbose_name='IF BODY IS PLACED IN HOUSES IN D1 CHART', blank=True)
    then_body_gola_4 = models.CharField(default='', max_length=20, db_column='Gola Placement-4', verbose_name='THEN BODY IS PLACED IN HOUSE IN GOLA HORA', blank=True)
    
    class Meta:
        verbose_name = '32.14. Table Name: Gola Hora D-2(GH) Table Code: 32-K'
        verbose_name_plural = '32.14. Table Name: Gola Hora D-2(GH) Table Code: 32-K'

class BodyMap_MaleChart_Table(models.Model):
    malechart_houses = models.CharField(default = '', max_length= 30, db_column='malechart_houses', verbose_name='MALE CHART HOUSES (BELOW)', blank = True)
    righthand_side = models.CharField(default = '', max_length= 30, db_column='RIGHT HAND SIDE', verbose_name='RIGHT HAND SIDE', blank = True)
    malechart = models.CharField(default = '', max_length= 30, db_column='MALE CHART', verbose_name='MALE CHART', blank = True)
    lefthand_houses = models.CharField(default = '', max_length= 30, db_column='LEFT HAND SIDE', verbose_name='LEFT HAND SIDE', blank = True)
    
    class Meta:
        verbose_name = '32.15. Table Name:  Body Map- Male Chart Table Code: 32-K1'
        verbose_name_plural = '32.15. Table Name:  Body Map- Male Chart Table Code: 32-K1'

class BodyMap_FemaleChart_Table(models.Model):
    femalechart_houses = models.CharField(default = '', max_length= 30, db_column='femalechart_houses', verbose_name='FEMALE CHART HOUSES (BELOW)', blank = True)
    righthand_side = models.CharField(default = '', max_length= 30, db_column='RIGHT HAND SIDE', verbose_name='RIGHT HAND SIDE', blank = True)
    femalechart = models.CharField(default = '', max_length= 30, db_column='FEMALE CHART', verbose_name='FEMALE CHART HOUSES (BELOW)', blank = True)
    lefthand_houses = models.CharField(default = '', max_length= 30, db_column='LEFT HAND SIDE', verbose_name='LEFT HAND SIDE', blank = True)
    
    class Meta:
        verbose_name = '32.16. Table Name:  Body Map- Female Chart Table Code: 32-K2'
        verbose_name_plural = '32.16. Table Name:  Body Map- Female Chart Table Code: 32-K2'

class LABH_MANDOOK_Hora_Table(models.Model):
    SECTION = models.CharField(default='', max_length=10, blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    
    class Meta:
        verbose_name = '32.18. Table Name:  Mihir (Labha) Hora/Labh Mandook Hora  Table Code: 32-L'
        verbose_name_plural = '32.18. Table Name:  Mihir (Labha) Hora/Labh Mandook Hora  Table Code: 32-L'

class SAM_MUKHA_RASHI_Table(models.Model):
    RASHI = models.CharField(default='', max_length=30, blank=True)
    SAM_MUKHA_RASHI = models.CharField(default='', max_length=20, db_column='SAM-MUKHA RASHI', verbose_name='SAM-MUKHA RASHI', blank=True)
    
    class Meta:
        verbose_name = '32.19. Table Name: Sam-Mukha Rasi Table Code: 32-M1'
        verbose_name_plural = '32.19. Table Name: Sam-Mukha Rasi Table Code: 32-M1'

class SAM_MUKHA_Hora_D2_SM_Table(models.Model):
    serial_no = models.IntegerField(default=0, verbose_name='Serial No.', blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    hora_lord = models.CharField(default='', max_length=20, db_column='HORA LORD', verbose_name='HORA LORD', blank=True)
    body_placed = models.CharField(default = '', max_length=5, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    from_extent1 = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)-1', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent1 = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)-1', verbose_name='To (SS-DD-MM-SS)', blank=True)
    hora_lord1 = models.CharField(default='', max_length=20, db_column='HORA LORD-1', verbose_name='HORA LORD D', blank=True)
    body_placed1 = models.CharField(default = '', max_length=5, db_column='body_placed-1', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    
    class Meta:
        verbose_name = '32.20. Table Name: Sam-Mukha Hora D-2(SM) Table Code: 32-M2'
        verbose_name_plural = '32.20. Table Name: Sam-Mukha Hora D-2(SM) Table Code: 32-M2'

class SOM_NATH_Hora_D2_SN_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    in_hora = models.CharField(default= '', max_length = 20, db_column='in_hora', verbose_name='IN THE Hora OF', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)

    class Meta:
        verbose_name = '32.21. Table Name: Som-Nath Hora D-2(SN) Table Code: 32-N'
        verbose_name_plural = '32.21. Table Name: Som-Nath Hora D-2(SN) Table Code: 32-N'
        
class PARIVRIITTI_DWAYA_Hora_D2_PD_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    in_hora = models.CharField(default= '', max_length = 20, db_column='in_hora', verbose_name='IN THE Hora OF', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    
    
    class Meta:
        verbose_name = '32.22. Table Name: Parivritti Dwaya Hora D-2(PD) Table Code: 32-O'
        verbose_name_plural = '32.22. Table Name: Parivritti Dwaya Hora D-2(PD) Table Code: 32-O'

class PRASHARI_DREKKANA_D3_PD_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    
    class Meta:
        verbose_name = '32.23. Table Name: Parashari Drekkana D-3(PD) Table Code: 32-P'
        verbose_name_plural = '32.23. Table Name: Parashari Drekkana D-3(PD) Table Code: 32-P'

class PARIVITRII_TRAYA_DREKKANA_D3_PT_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.24. Table Name: Parivritti Traya Drekkana D-3(PT) Table Code: 32-Q'
        verbose_name_plural = '32.24. Table Name: Parivritti Traya Drekkana D-3(PT) Table Code: 32-Q'

class JAGANNATH_DREKKANA_D3_JD_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.25. Table Name: Jagannath Drekkana D-3(JD) Table Code: 32-R'
        verbose_name_plural = '32.25. Table Name: Jagannath Drekkana D-3(JD) Table Code: 32-R'

class SOMNATH_M_DREKKANA_D3_SMD_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.26. Table Name: Somanath M Drekkana D-3(SMD) Table Code: 32-S'
        verbose_name_plural = '32.26. Table Name: Somanath M Drekkana D-3(SMD) Table Code: 32-S'

class PARASHARI_CHATURTHAMSA_OR_TURYA_D4_PC_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
   
    class Meta:
        verbose_name = '32.27. Table Name: Parashari Chaturthamsa or Turyaamsa D-4(PC) Table Code: 32-T'
        verbose_name_plural = '32.27. Table Name: Parashari Chaturthamsa or Turyaamsa D-4(PC) Table Code: 32-T'

class VEDAAMSA_D4_V_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    veda = models.CharField(default='', max_length=20, db_column='VEDA', verbose_name='VEDA', blank=True)
    gayatri = models.CharField(default='', max_length=20, db_column='GAYATRI', verbose_name='GAYATRI', blank=True)
    pancha = models.CharField(default='', max_length=20, db_column='PANCHA', verbose_name='PANCHA', blank=True)
    kumara = models.CharField(default='', max_length=20, db_column='KUMAARA', verbose_name='KUMAARA', blank=True)
    yuga = models.CharField(default='', max_length=20, db_column='YUGA', verbose_name='YUGA', blank=True)
    vidhyaa = models.CharField(default='', max_length=20, db_column='VIDHYAA', verbose_name='VIDHYAA', blank=True)
    
    class Meta:
        verbose_name = '32.28. Table Name: Vedaamsa  D-4(V)Table Code: 32-U'
        verbose_name_plural = '32.28. Table Name: Vedaamsa  D-4(V)Table Code: 32-U'

class PARIVRITTI_PANCHAMSHA_D5_PP_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.29. Table Name:  Parivritti Panchamsha D-5(PP) Table Code: 32-V'
        verbose_name_plural = '32.29. Table Name:  Parivritti Panchamsha D-5(PP) Table Code: 32-V'

class TAJIK_PANCHAMSHA_D5_TP_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.30. Table Name: Tajik Panchamsha D-5(TP) Table Code: 32-W'
        verbose_name_plural = '32.30. Table Name: Tajik Panchamsha D-5(TP) Table Code: 32-W'

class KAULUKA_SHASTAMSA_D6_KS_Table(models.Model):
    S_No = models.IntegerField(default=0, blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.31. Table Name: Kauluka Shastamsa D-6(KS) Table Code: 32-Y'
        verbose_name_plural = '32.31. Table Name: Kauluka Shastamsa D-6(KS) Table Code: 32-Y'
    
class PARIVRITTI_SHASHTAMSA_D6_PS_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='body_placed', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.32. Table Name: Parivritti Shastamsa D-6(PS) Table Code: 32-Z'
        verbose_name_plural = '32.32. Table Name: Parivritti Shastamsa D-6(PS) Table Code: 32-Z'

class SAPTAMSHA_D7_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.33. Table Name: Saptamansha D-7 Table Code: 32-AA'
        verbose_name_plural = '32.33. Table Name: Saptamansha D-7 Table Code: 32-AA'

class TAJIK_ASHTAMAMSHA_D8_TA_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.34. Table Name: Tajik Ashtamansha D-8(TA) Table Code: 32-AB'
        verbose_name_plural = '32.34. Table Name: Tajik Ashtamansha D-8(TA) Table Code: 32-AB'

class PARASHARI_NAVAMSHA_D9_PN_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.35. Table Name: Parashari Navamsha D-9(PN) Table Code: 32-AC'
        verbose_name_plural = '32.35. Table Name: Parashari Navamsha D-9(PN) Table Code: 32-AC'

class SOMNATH_NAVAMSHA_D9_SN_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.36. Table Name: Somnath Navamsha D-9(SN) Table Code: 32-AD'
        verbose_name_plural = '32.36. Table Name: Somnath Navamsha D-9(SN) Table Code: 32-AD'

class PADA_NAVAMSHA_D9_PN_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.37. Table Name: Pada Navamsha D-9(PN) Table Code: 32-AE'
        verbose_name_plural = '32.37. Table Name: Pada Navamsha D-9(PN) Table Code: 32-AE'

class NADI_NAVAMSHA_D9_NN_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.38. Table Name: Nadi Navamsha D-9(NN) Table Code: 32-AF'
        verbose_name_plural = '32.38. Table Name: Nadi Navamsha D-9(NN) Table Code: 32-AF'

class DASHAMANSHA_D10_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.39. Table Name: Dashamasha D-10 Table Code: 32-AG'
        verbose_name_plural = '32.39. Table Name: Dashamasha D-10 Table Code: 32-AG'

class PARASHARI_RUDRAMSA_D11_PR_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.40. Table Name: Parashari Rudramsa D-11(PR) Table Code: 32-AH'
        verbose_name_plural = '32.40. Table Name: Parashari Rudramsa D-11(PR) Table Code: 32-AH'

class IYER_LABHAMSA_D11_IL_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.41. Table Name: Iyer Labhamsha D-11(IL) Table Code: 32-AI'
        verbose_name_plural = '32.41. Table Name: Iyer Labhamsha D-11(IL) Table Code: 32-AI'

class LABHAMSA_D11_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.42. Table Name: Labhamsha D-11 Table Code: 32-AJ'
        verbose_name_plural = '32.42. Table Name: Labhamsha D-11 Table Code: 32-AJ'

class DVADASHAMSA_D12_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.43. Table Name: Dvadasamsha D-12  Table Code: 32-AK'
        verbose_name_plural = '32.43. Table Name: Dvadasamsha D-12  Table Code: 32-AK'

class PARASHARI_SODASHAMSA_D16_PS_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.44. Table Name: Parashari Sodashamsa D-16(PS) Table Code: 32-AL'
        verbose_name_plural = '32.44. Table Name: Parashari Sodashamsa D-16(PS) Table Code: 32-AL'

class IYER_SODASHAMSA_D16_IS_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.45. Table Name: Iyer Sodashamsa  D-16(IS) Table Code:32-AM'
        verbose_name_plural = '32.45. Table Name: Iyer Sodashamsa  D-16(IS) Table Code:32-AM'

class VIMSAMSHA_D20_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.46. Table Name:  Vimsamsha D-20 Table Code: 32-AN'
        verbose_name_plural = '32.46. Table Name:  Vimsamsha D-20 Table Code: 32-AN'

class PARASHAR_SIDDHAAMSHA_D24_PSI_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.47. Table Name:  Parashar Siddhaamsa D-24(PSI) Table Code: 32-AO'
        verbose_name_plural = '32.47. Table Name:  Parashar Siddhaamsa D-24(PSI) Table Code: 32-AO'

class PARA_VIDHYA_SIDDHAMSHA_D24_PVSI_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.48. Table Name: Para Vidhya Siddhaamsa D-24(PVSI) Table Code: 32-AP'
        verbose_name_plural = '32.48. Table Name: Para Vidhya Siddhaamsa D-24(PVSI) Table Code: 32-AP'

class BHAMSHA_D27_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.49. Table Name: Bhamsha D-27 Table Code: 32-AQ'
        verbose_name_plural = '32.49. Table Name: Bhamsha D-27 Table Code: 32-AQ'

class PARASHARI_TATTVAMSA_D30_PT_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    element = models.CharField(default='', max_length=20, db_column='Element', verbose_name='Element', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.50. Table Name: Parashar Trimsamsa/Tattvaamsa D-30(PT) Table Code: 32-AR'
        verbose_name_plural = '32.50. Table Name: Parashar Trimsamsa/Tattvaamsa D-30(PT) Table Code: 32-AR'

class VENKETSHWAR_TRIMSHAMSA_D30_VT_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.51. Table Name: Venketshwar Trimsamsa D30(VT) Table Code: 32-AS'
        verbose_name_plural = '32.51. Table Name: Venketshwar Trimsamsa D30(VT) Table Code: 32-AS'

class Khadvedamsa_D40_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.52. Table Name: Khadvedamsa D-40 Table Code: 32-AT'
        verbose_name_plural = '32.52. Table Name: Khadvedamsa D-40 Table Code: 32-AT'

class AKSHAVEDAMSA_D45_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.53. Table Name: AkshVedamsa D-45 Table Code: 32-AU'
        verbose_name_plural = '32.53. Table Name: AkshVedamsa D-45 Table Code: 32-AU'

class Sastiamsa_D60_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    class Meta:
        verbose_name = '32.54. Table Name: Sastiamsa D-60 Table Code: 32-AV'
        verbose_name_plural = '32.54. Table Name: Sastiamsa D-60 Table Code: 32-AV'

class NavaNavamsha_D81_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    
    
    class Meta:
        verbose_name = '32.55. Table Name: NavaNavamsha D-81 Table Code: 32-AW'
        verbose_name_plural = '32.55. Table Name: NavaNavamsha D-81 Table Code: 32-AW'

class Ashtottaramsa_D108_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.56. Table Name: Ashtottaramsa D-108 Table Code: 32-AX'
        verbose_name_plural = '32.56. Table Name: Ashtottaramsa D-108 Table Code: 32-AX'

class Dwadasamsa_Dwadasamsa_D144_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    body_placed = models.CharField(default= '', max_length=30, db_column='NUMERIC VALUE WHRE BODY IS PLACED', verbose_name='NUMERIC VALUE WHRE BODY IS PLACED', blank=True)
    lord = models.CharField(default='', max_length=20, db_column='LORD', verbose_name='LORD', blank=True)
    diety = models.CharField(default='', max_length=20, db_column='diety', verbose_name='diety', blank=True)
    

    class Meta:
        verbose_name = '32.57. Table Name: Dwadasamsa-Dwadasamsaa D-144 Table Code: 32-AY'
        verbose_name_plural = '32.57. Table Name: Dwadasamsa-Dwadasamsa D-144 Table Code: 32-AY'

class Vaiseshikamsaas_varga_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_group = models.CharField(default='', max_length=25, verbose_name="NAME OF THE GROUP",db_column="NAME OF THE GROUP" ,blank=True)
    chart_exhaltation =  models.CharField(default='', max_length=25, verbose_name="N HOW MANY DIVISIONAL CHARTS IS EXALTATION /OFFICE/HOME IN THE GROUP",db_column="Chart-exhaltation" ,blank=True)
    title_planet = models.CharField(default='', max_length=20, db_column='title-planet', verbose_name='SPECIAL TITLE OF THE PLANET', blank=True)

    class Meta:
        verbose_name = '33. Table Name: Vaiseshikamsaas in Varga Table Code: 33'
        verbose_name_plural = '33. Table Name: Vaiseshikamsaas in Varga Table Code: 33'

class PANCHANG_OVERLORDS_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    unit_time = models.CharField(default='', max_length=20, db_column='unit-time', verbose_name='UNIT OF MEASURE OF TIME', blank=True)
    overlord_unit = models.CharField(default='', max_length=20, db_column='overlord-unit', verbose_name='OVER-LORD OF  THE UNIT (ELEMENTS)', blank=True)
    knowledge = models.CharField(default='', max_length=30, db_column='knowledge', verbose_name='KNOWLEDGE OF THIS LEADS TO', blank=True)

    class Meta:
        verbose_name = '34. Table Name: PANCHANG OVERLORDS Table Code: 34'
        verbose_name_plural = '34. Table Name: PANCHANG OVERLORDS Table Code: 34'

class Hora_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    time_from = models.CharField(default='', max_length=10, db_column='time-from', verbose_name='TIME FROM (HH-MM)', blank=True)
    time_to = models.CharField(default='', max_length=10, db_column='time-to', verbose_name='TIME TO (HH-MM)', blank=True)
    sunday = models.CharField(default='', max_length=20, db_column='SUNDAY', verbose_name='SUNDAY', blank=True)
    monday = models.CharField(default='', max_length=20, db_column='MONDAY', verbose_name='MONDAY', blank=True)
    tuesday = models.CharField(default='', max_length=20, db_column='TUESDAY', verbose_name='TUESDAY', blank=True)
    wednesday = models.CharField(default='', max_length=20, db_column='WEDNESDAY', verbose_name='WEDNESDAY', blank=True)
    thursday = models.CharField(default='', max_length=20, db_column='THURSDAY', verbose_name='THURSDAY', blank=True)
    friday = models.CharField(default='', max_length=20, db_column='FRIDAY', verbose_name='FRIDAY', blank=True)
    saturday = models.CharField(default='', max_length=20, db_column='SATURDAY', verbose_name='SATURDAY', blank=True)
    
    class Meta:
        verbose_name = '35. Table Name: Hora Table (Fixed) Table Code: 35'
        verbose_name_plural = '35. Table Name: Hora Table (Fixed) Table Code: 35'

""" class Navatara_Lagna_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    S_No_Nakshatra = models.IntegerField(default=0, verbose_name='S No OF NAKSHTRA FROM LAGNA',blank=False)
    cycle = models.CharField(default='', max_length=30, db_column='CYCLE', verbose_name='CYCLE', blank=True)
    alphanumeric_notation = models.CharField(default='', max_length=30, db_column='ALPHABETICAL NOTATION', verbose_name='ALPHABETICAL NOTATION', blank=True)
    spl_name_nakshatra = models.CharField(default = '', max_length = 30, db_column='spl name NAKSHTRA', verbose_name='SPECIAL NAME OF NAKSHTRA CALLED', blank=True)

    class Meta:
        verbose_name = '36.1. Table Name: Navatara Table From Lagna (Fixed) Table Code: 36-A'
        verbose_name_plural = '36.1. Table Name: Navatara Table From Lagna (Fixed) Table Code: 36-A' """
        
class Nakshatra_element_works_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_nakshatra = models.CharField(default='', max_length=30, db_column='NAKSHATRA NAME', verbose_name='NAKSHATRA NAME', blank=True)
    element = models.CharField(default='', max_length=30, db_column='ELEMENT', verbose_name='ELEMENT(BHUTA)', blank=True)
    caste = models.CharField(default='', max_length=30, db_column='CASTE', verbose_name='CASTE(JATI)', blank=True)
    works = models.CharField(default='', max_length=30, db_column='WORKS', verbose_name='WORKS(KARMNA)', blank=True)
    genus = models.CharField(default='', max_length=30, db_column='GENUS', verbose_name='GENUS(GANA)', blank=True)
    
    class Meta:
        verbose_name = '36. Table Name: Nakshatra Element(Bhuta), Caste(Jati) Works(Karmana) & (Genus) Gana Table (Table Code: 36)'
        verbose_name_plural = '36. Table Name: Nakshatra Element(Bhuta), Caste(Jati) Works(Karmana) & (Genus) Gana Table (Table Code: 36)'

        
class Navratra_Pattern_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    start_ref_point = models.CharField(default='', max_length=30, db_column='STARTING REFERENCE POINT', verbose_name='STARTING REFERENCE POINT', blank=True)
    no_nakshatra_from_ref = models.CharField(default='', max_length=30, db_column='NUMBER OF NAKSHTRA FROM STARTING REFERENCE POINT', verbose_name='NUMBER OF NAKSHTRA FROM STARTING REFERENCE POINT', blank=True)
    cycle = models.CharField(default='', max_length=30, db_column='CYCLE', verbose_name='CYCLE', blank=True)
    alphanumeric_notation = models.CharField(default='', max_length=30, db_column='ALPHABETICAL NOTATION', verbose_name='ALPHABETICAL NOTATION', blank=True)
    spl_name_nakshatra = models.CharField(default = '', max_length = 30, db_column='spl name NAKSHTRA', verbose_name='SPECIAL NAME OF NAKSHTRA CALLED', blank=True)

    class Meta:
        verbose_name = '37. Table Name: Navtara Pattern Table (Table Code: 37)'
        verbose_name_plural = '37. Table Name: Navtara Pattern Table (Table Code: 37)'

class Special_Navratra_Pattern_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    start_ref_point = models.CharField(default='', max_length=30, db_column='STARTING REFERENCE POINT', verbose_name='STARTING REFERENCE POINT', blank=True)
    no_nakshatra_from_ref = models.CharField(default='', max_length=30, db_column='NUMBER OF NAKSHTRA FROM STARTING REFERENCE POINT', verbose_name='NUMBER OF NAKSHTRA FROM STARTING REFERENCE POINT', blank=True)
    name_spl_tara = models.CharField(default='', max_length=30, db_column='NAME OF SPECIAL TARA', verbose_name='NAME OF SPECIAL TARA', blank=True)
    impact = models.CharField(default='', max_length=30, db_column='IMPACT', verbose_name='IMPACT', blank=True)

    class Meta:
        verbose_name = '38. Table Name: Special Tara Pattern Table (Table Code:38)'
        verbose_name_plural = '38. Table Name: Special Tara Pattern Table (Table Code:38)'


""" class Navatara_Moon_Fixed_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    S_No_Nakshatra = models.IntegerField(default=0, verbose_name='S No OF NAKSHTRA FROM MOON',blank=False)
    cycle = models.CharField(default='', max_length=30, db_column='CYCLE', verbose_name='CYCLE', blank=True)
    alphanumeric_notation = models.CharField(default='', max_length=30, db_column='ALPHABETICAL NOTATION', verbose_name='ALPHABETICAL NOTATION', blank=True)
    spl_name_nakshatra = models.CharField(default = '', max_length = 30, db_column='spl name NAKSHTRA', verbose_name='SPECIAL NAME OF NAKSHTRA CALLED', blank=True)

    class Meta:
        verbose_name = '36.2. Table Name: Navatara Table From Moon (Fixed) Table Code: 36-B'
        verbose_name_plural = '36.2. Table Name: Navatara Table From Moon (Fixed) Table Code: 36-B' """

""" class Special_Nakshtra_Scheme_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    start_ref_point = models.CharField(default='', max_length=30, db_column='STARTING REFERENCE POINT', verbose_name='STARTING REFERENCE POINT', blank=True)
    tara_no_ref_point = models.CharField(default='', max_length=30, db_column='TARA NUMBER FROM REFERENCE POINT', verbose_name='TARA NUMBER FROM REFERENCE POINT', blank=True)
    name_spl_tara = models.CharField(default='', max_length=30, db_column='NAME OF SPECIAL TARA', verbose_name='NAME OF SPECIAL TARA', blank=True)
    impact = models.CharField(default='', max_length=30, db_column='IMPACT', verbose_name='IMPACT', blank=True)

    class Meta:
        verbose_name = '37. Table Name: Special Nakshtra Scheme'
        verbose_name_plural = '37. Table Name: Special Nakshtra Scheme' """

class Nakshatra_sight_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    quality_nakshatra = models.CharField(default='', max_length=30, db_column='QUALITY OF NAKSHTRA', verbose_name='QUALITY OF NAKSHTRA', blank=True)
    name_nakshatra = models.CharField(default='', max_length=30, db_column='NAME OF NAKSHATRA', verbose_name='NAME OF NAKSHATRA', blank=True)
    nakshatra_no = models.CharField(default='', max_length=30, db_column='NAKSHTRA NUMBER', verbose_name='NAKSHTRA NUMBER', blank=True)
    direction_dristi = models.CharField(default='', max_length=30, db_column='DIRECTION OF DRISTI', verbose_name='DIRECTION OF DRISTI', blank=True)
    guna = models.CharField(default='', max_length=30, db_column='GUNA', verbose_name='GUNA', blank=True)
    impact = models.CharField(default='', max_length=30, db_column='IMPACT', verbose_name='IMPACT', blank=True)

    class Meta:
        verbose_name = '39. Table Name: NAKSHTRA SIGHT TABLE (Table Code:39)'
        verbose_name_plural = '39. Table Name: NAKSHTRA SIGHT TABLE (Table Code:39)'

class ANDHAADI_NAKSHTRA_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    quality_nakshatra = models.CharField(default='', max_length=30, db_column='QUALITY OF NAKSHTRA', verbose_name='QUALITY OF NAKSHTRA', blank=True)
    name_nakshatra = models.CharField(default='', max_length=30, db_column='NAME OF NAKSHATRA', verbose_name='NAME OF NAKSHATRA', blank=True)
    nakshatra_no = models.CharField(default='', max_length=30, db_column='NAKSHTRA NUMBER', verbose_name='NAKSHTRA NUMBER', blank=True)
    vision_quality = models.CharField(default='', max_length=30, db_column='VISION QUALITY', verbose_name='VISION QUALITY', blank=True)
    impact = models.CharField(default='', max_length=30, db_column='IMPACT', verbose_name='IMPACT', blank=True)

    class Meta:
        verbose_name = '40. Table Name: ANDHAADI NAKSHTRA TABLE (Table Code:40)'
        verbose_name_plural = '40. Table Name: ANDHAADI NAKSHTRA TABLE (Table Code:40)'

class movability_qualities_nakshatra_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    class_nakshatra = models.CharField(default='', max_length=30, db_column='CLASS OF NAKSHATRA', verbose_name='CLASS OF NAKSHATRA', blank=True)
    name_nakshatra = models.CharField(default='', max_length=30, db_column='NAME OF NAKSHATRA', verbose_name='NAME OF NAKSHATRA', blank=True)
    quality_nakshatra = models.CharField(default='', max_length=30, db_column='QUALITY OF NAKSHTRA', verbose_name='QUALITY OF NAKSHTRA', blank=True)
    attributing_planets = models.CharField(default='', max_length=30, db_column='ATTRIBUTING PLANET(S)', verbose_name='ATTRIBUTING PLANET(S)', blank=True)
    suit_activity_nature = models.CharField(default='', max_length=151, db_column='SUITABLE FOR ACTIVITIES LIKE (NATURE) ', verbose_name='SUITABLE FOR ACTIVITIES LIKE (NATURE) ', blank=True)
    nakshatra_energy = models.CharField(default='', max_length=151, db_column='NAKSHTRA HAS ENERGY SIMILAR TO', verbose_name='NAKSHTRA HAS ENERGY SIMILAR TO', blank=True)
    suit_activities1 = models.CharField(default='', max_length=151, db_column='SUITABLE FOR ACTIVITIES 1', verbose_name='SUITABLE FOR ACTIVITIES 1', blank=True)
    suit_activities2 = models.CharField(default='', max_length=151, db_column='SUITABLE FOR ACTIVITIES 2', verbose_name='SUITABLE FOR ACTIVITIES 2', blank=True)
    suit_activities3 = models.CharField(default='', max_length=151, db_column='SUITABLE FOR ACTIVITIES 3', verbose_name='SUITABLE FOR ACTIVITIES 3', blank=True)
    suit_activities4 = models.CharField(default='', max_length=151, db_column='SUITABLE FOR ACTIVITIES 4', verbose_name='SUITABLE FOR ACTIVITIES 4', blank=True)
    suit_activities5 = models.CharField(default='', max_length=151, db_column='SUITABLE FOR ACTIVITIES 5', verbose_name='SUITABLE FOR ACTIVITIES 5', blank=True)
    suit_activities6 = models.CharField(default='', max_length=151, db_column='SUITABLE FOR ACTIVITIES 6', verbose_name='SUITABLE FOR ACTIVITIES 6', blank=True)
    suit_activities7 = models.CharField(default='', max_length=151, db_column='SUITABLE FOR ACTIVITIES 7', verbose_name='SUITABLE FOR ACTIVITIES 7', blank=True)
       
    class Meta:
        verbose_name = '41. Table Name: Moveability & Other Qualities of Nakshatra Table (Table Code:41)'
        verbose_name_plural = '41. Table Name: Moveability & Other Qualities of Nakshatra Table (Table Code:41)'

class SAPTA_RISHI_BIRTH_SOURCE_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    saptarsi = models.CharField(default='', max_length=30, db_column='SAPTARSI', verbose_name='SAPTARSI (PURUSA)', blank=True)
    born_from = models.CharField(default='', max_length=30, db_column='BORN FROM', verbose_name='BORN FROM', blank=True)
    kaaraka_father_of = models.CharField(default='', max_length=30, db_column='KAARAKA', verbose_name='KAARAKA(FATHER OF)', blank=True)
    indication = models.CharField(default='', max_length=30, db_column='INDICATION', verbose_name='INDICATION', blank=True)

    class Meta:
        verbose_name = '42. Table Name: Sapta Rishi Birth Source Table (Table Code:42)'
        verbose_name_plural = '42. Table Name: Sapta Rishi Birth Source Table (Table Code:42)'


class Natural_Sapt_Rishi_Nakshtra_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    saptarsi = models.CharField(default='', max_length=30, db_column='SAPTARSI', verbose_name='SAPTARSI (PURUSA)', blank=True)
    nakshatra_no = models.CharField(default='', max_length=30, db_column='NAKSHTRA NUMBER', verbose_name='NAKSHTRA NUMBER', blank=True)
    name_nakshatra = models.CharField(default='', max_length=30, db_column='NAME OF NAKSHATRA', verbose_name='NAME OF NAKSHATRA', blank=True)
    nakshatra_no1 = models.CharField(default='', max_length=30, db_column='NAKSHTRA NUMBER-1', verbose_name='NAKSHTRA NUMBER', blank=True)
    name_nakshatra1 = models.CharField(default='', max_length=30, db_column='NAME OF NAKSHATRA-1', verbose_name='NAME OF NAKSHATRA', blank=True)
    nakshatra_no2 = models.CharField(default='', max_length=30, db_column='NAKSHTRA NUMBER-2', verbose_name='NAKSHTRA NUMBER', blank=True)
    name_nakshatra2 = models.CharField(default='', max_length=30, db_column='NAME OF NAKSHATRA-2', verbose_name='NAME OF NAKSHATRA', blank=True)
    nakshatra_no3 = models.CharField(default='', max_length=30, db_column='NAKSHTRA NUMBER-3', verbose_name='NAKSHTRA NUMBER', blank=True)
    name_nakshatra3 = models.CharField(default='', max_length=30, db_column='NAME OF NAKSHATRA-3', verbose_name='NAME OF NAKSHATRA', blank=True)

    class Meta:
        verbose_name = '43. Table Name: Natural Sapta Rishi Nakshatra Table(28 Scheme) (Table Code:43)'
        verbose_name_plural = '43. Table Name: Natural Sapta Rishi Nakshatra Table(28 Scheme) (Table Code:43)'

class Characterstic_of_planets_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    as_per_writer = models.CharField(default='', max_length=30, db_column='As per writer', verbose_name='AS PER RISHI/EXPONENT/ WRITER/ASTROLOGER', blank=True)
    planets = models.CharField(default='', max_length=30, db_column='PLANETS', verbose_name='PLANETS', blank=True)
    synonym1 = models.CharField(default='', max_length=30, db_column='SYNONYM 1', verbose_name='SYNONYM 1', blank=True)
    synonym2 = models.CharField(default='', max_length=30, db_column='SYNONYM 2', verbose_name='SYNONYM 2', blank=True)
    synonym3 = models.CharField(default='', max_length=30, db_column='SYNONYM 3', verbose_name='SYNONYM 3', blank=True)
    synonym4 = models.CharField(default='', max_length=30, db_column='SYNONYM 4', verbose_name='SYNONYM 4', blank=True)
    synonym5 = models.CharField(default='', max_length=30, db_column='SYNONYM 5', verbose_name='SYNONYM 5', blank=True)
    castes = models.CharField(default='', max_length=30, db_column='CASTES', verbose_name='CASTES', blank=True)
    description = models.CharField(default='', max_length=160, db_column='DESCRIPTION', verbose_name='DESCRIPTION', blank=True)
    statust = models.CharField(default='', max_length=30, db_column='STATUS-t', verbose_name='STATUS', blank=True)
    guna = models.CharField(default='', max_length=30, db_column='GUNA', verbose_name='GUNA', blank=True)
    shad_ripu = models.CharField(default='', max_length=30, db_column='SHAD-RIPU', verbose_name='SHAD-RIPU', blank=True)
    makaar = models.CharField(default='', max_length=30, db_column='MAKAAR', verbose_name='MAKAAR', blank=True)
    karak1 = models.CharField(default='', max_length=30, db_column='KARAK 1', verbose_name='KARAK 1', blank=True)
    karak2 = models.CharField(default='', max_length=30, db_column='KARAK 2', verbose_name='KARAK 2', blank=True)
    karak3 = models.CharField(default='', max_length=30, db_column='KARAK 3', verbose_name='KARAK 3', blank=True)
    karak4 = models.CharField(default='', max_length=30, db_column='KARAK 4', verbose_name='KARAK 4', blank=True)
    naisargika_karak = models.CharField(default='', max_length=160, db_column='NAISARGIKA KARAK', verbose_name='NAISARGIKA KARAK', blank=True)
    chara_karak = models.CharField(default='', max_length=30, db_column='CHARA KARAK', verbose_name='CHARA KARAK', blank=True)
    sthir_karak_rel = models.CharField(default='', max_length=30, db_column='STHIR KARAK -RELATIVES', verbose_name='STHIR KARAK -RELATIVES', blank=True)
    fierce_saumya = models.CharField(default='', max_length=30, db_column='Fierce-Saumya', verbose_name='FIERCE-KRURA/GENTLE-SAUMYA', blank=True)
    tara_planets = models.CharField(default='', max_length=30, db_column='PRAKASA/TARA PLANETS', verbose_name='PRAKASA/TARA PLANETS', blank=True)
    governance = models.CharField(default='', max_length=30, db_column='GOVERNANCE', verbose_name='GOVERNANCE', blank=True)
    graha_vahan = models.CharField(default='', max_length=30, db_column='GRAHA VAHAN', verbose_name='GRAHA VAHAN', blank=True)
    robes = models.CharField(default='', max_length=30, db_column='ROBES', verbose_name='ROBES', blank=True)
    gender = models.CharField(default='', max_length=30, db_column='GENDER', verbose_name='GENDER', blank=True)
    age_group = models.CharField(default='', max_length=30, db_column='AGE GROUP', verbose_name='AGE GROUP', blank=True)
    planet_cabinet = models.CharField(default='', max_length=30, db_column='PLANET CABINET', verbose_name='PLANET CABINET', blank=True)
    pancha_mahabhuta = models.CharField(default='', max_length=30, db_column='PANCHA MAHABHUTA', verbose_name='PANCHA MAHABHUTA', blank=True)
    trees = models.CharField(default='', max_length=30, db_column='TREES', verbose_name='TREES', blank=True)
    tastes = models.CharField(default='', max_length=30, db_column='TASTES', verbose_name='TASTES', blank=True)
    gotra = models.CharField(default='', max_length=30, db_column='GOTRA', verbose_name='GOTRA', blank=True)
    birth_place_planet = models.CharField(default='', max_length=30, db_column='BIRTH PLACE OF PLANETS', verbose_name='BIRTH PLACE OF PLANETS', blank=True)
    abode_place_planet = models.CharField(default='', max_length=30, db_column='ABODES OF THE PLANETS', verbose_name='ABODES OF THE PLANETS', blank=True)
    place_freq_planet1 = models.CharField(default='', max_length=160, db_column='PLACES FREQUENTED BY PLANETS 1', verbose_name='PLACES FREQUENTED BY PLANETS 1', blank=True)
    place_freq_planet2 = models.CharField(default='', max_length=160, db_column='PLACES FREQUENTED BY PLANETS 2', verbose_name='PLACES FREQUENTED BY PLANETS 2', blank=True)
    place_freq_planet3 = models.CharField(default='', max_length=160, db_column='PLACES FREQUENTED BY PLANETS 3', verbose_name='PLACES FREQUENTED BY PLANETS 3', blank=True)
    place_freq_planet4 = models.CharField(default='', max_length=160, db_column='PLACES FREQUENTED BY PLANETS 4', verbose_name='PLACES FREQUENTED BY PLANETS 4', blank=True)
    place_freq_planet5 = models.CharField(default='', max_length=160, db_column='PLACES FREQUENTED BY PLANETS 5', verbose_name='PLACES FREQUENTED BY PLANETS 5', blank=True)
    place_freq_planet6 = models.CharField(default='', max_length=160, db_column='PLACES FREQUENTED BY PLANETS 6', verbose_name='PLACES FREQUENTED BY PLANETS 6', blank=True)
    lokas = models.CharField(default='', max_length=30, db_column='LOKAS', verbose_name='LOKA(AS PER KALP-VRIKSHA)', blank=True)
    lokas1 = models.CharField(default='', max_length=30, db_column='LOKAS-1', verbose_name='LOKA (AS PER BRAHAJJATAKA)', blank=True)
    rising_udaya = models.CharField(default='', max_length=30, db_column='RISING - UDAYA', verbose_name='RISING (UDAYA)', blank=True)
    # legs = models.CharField(default='', max_length=30, db_column='LEGS', verbose_name=' LEGS(PADAS)', blank=True)
    form = models.CharField(default='', max_length=30, db_column='form', verbose_name='FORM(SVARUPA-AKRITI)', blank=True)
    working_style_planets = models.CharField(default='', max_length=30, db_column='WORKING STYLES OF PLANETS', verbose_name='WORKING STYLES OF PLANETS', blank=True)
    element = models.CharField(default='', max_length=30, db_column='ELEMENT', verbose_name='ELEMENT', blank=True)
    tattva_hindi = models.CharField(default='', max_length=30, db_column='TATTVA-HINDI', verbose_name='TATTVA (HINDI)', blank=True)
    colour_english = models.CharField(default='', max_length=30, db_column='COLOUR (ENGLISH)', verbose_name='COLOUR (ENGLISH)', blank=True)
    rang_hindi = models.CharField(default='', max_length=30, db_column='RANG-HINDI', verbose_name='RANG (HINDI)', blank=True)
    complexion = models.CharField(default='', max_length=30, db_column='COMPLEXION', verbose_name='COMPLEXION', blank=True)
    length_planet = models.CharField(default='', max_length=30, db_column='LENGTH AS PER PLANET', verbose_name='LENGTH AS PER PLANET', blank=True)
    sapt_dhatu = models.CharField(default='', max_length=30, db_column='SAPT DHATU', verbose_name='SAPT DHATU', blank=True)
    related_to = models.CharField(default='', max_length=30, db_column='RELATED TO', verbose_name='RELATED TO', blank=True)
    provides = models.CharField(default='', max_length=30, db_column='PROVIDES', verbose_name='PROVIDES', blank=True)
    tridhatu = models.CharField(default='', max_length=160, db_column='TRIDHATU', verbose_name='TRIDHATU', blank=True)
    taste_1 = models.CharField(default='', max_length=30, db_column='TASTE-1', verbose_name='TASTE', blank=True)
    rasa = models.CharField(default='', max_length=30, db_column='RASA-HINDI', verbose_name='RASA(HINDI)', blank=True)
    kaal = models.CharField(default='', max_length=30, db_column='KAAL', verbose_name='KAAL', blank=True)
    time_duration = models.CharField(default='', max_length=30, db_column='TIME DURATION', verbose_name='TIME DURATION', blank=True)
    direction_dig_chakra = models.CharField(default='', max_length=30, db_column='DIRECTION IN DIG CHAKRA', verbose_name='DIRECTION IN DIG CHAKRA', blank=True)
    devta_dig_chakra = models.CharField(default='', max_length=30, db_column='DEVTA OF DIG CHAKRA', verbose_name='DEVTA OF DIG CHAKRA', blank=True)
    direction_kaal_chakra = models.CharField(default='', max_length=30, db_column='DIRECTION IN KAAL CHAKRA', verbose_name='DIRECTION IN KAAL CHAKRA', blank=True)
    devta_kaal_chakra = models.CharField(default='', max_length=30, db_column='DEVTA OF KAAL CHAKRA', verbose_name='DEVTA OF KAAL CHAKRA', blank=True)
    dig_bala_from_lagna = models.CharField(default='', max_length=30, db_column='DIG BALA FROM LAGNA', verbose_name='DIG BALA FROM LAGNA/ARUDHA', blank=True)
    friends = models.CharField(default='', max_length=30, db_column='FRIENDS', verbose_name='FRIENDS (Parashar /Jaimini)', blank=True)
    neutrals = models.CharField(default='', max_length=30, db_column='NEUTRALS', verbose_name='NEUTRALS (Parashar /Jaimini)', blank=True)
    enemies = models.CharField(default='', max_length=30, db_column='ENEMIES', verbose_name='ENEMIES (Parashar /Jaimini)', blank=True)
    friendly_sign = models.CharField(default='', max_length=30, db_column='FRIENDLY SIGN', verbose_name='FRIENDLY SIGN', blank=True)
    neutral_sign = models.CharField(default='', max_length=30, db_column='NEUTRAL SIGN', verbose_name='NEUTRAL SIGN', blank=True)
    enemy_sign = models.CharField(default='', max_length=30, db_column='ENEMY’S SIGN', verbose_name='ENEMY’S SIGN', blank=True)
    status0 = models.CharField(default='', max_length=30, db_column='STATUS-0', verbose_name='STATUS', blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    special_remark = models.CharField(default = '',max_length = 30, db_column='SPECIAL REMARK', verbose_name='SPECIAL REMARK', blank=True)
    status1 = models.CharField(default='', max_length=30, db_column='STATUS-1', verbose_name='STATUS', blank=True)
    from_extent1 = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)-1', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent1 = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)-1', verbose_name='To (SS-DD-MM-SS)', blank=True)
    status2 = models.CharField(default='', max_length=30, db_column='STATUS-2', verbose_name='STATUS', blank=True)
    from_extent2 = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)-2', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent2 = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)-2', verbose_name='To (SS-DD-MM-SS)', blank=True)
    status3 = models.CharField(default='', max_length=30, db_column='STATUS-3', verbose_name='STATUS', blank=True)
    from_extent3 = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)-3', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent3 = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)-3', verbose_name='To (SS-DD-MM-SS)', blank=True)
    adi_devta_parashar = models.CharField(default='', max_length=30, db_column='ADI-DEVTA AS PER PARASHAR', verbose_name='ADI-DEVTA AS PER PARASHAR', blank=True)
    aadi_devta_jaimini = models.CharField(default='', max_length=30, db_column='AADI DEVTA AS PER JAIMINI', verbose_name='AADI DEVTA AS PER JAIMINI', blank=True)
    pratyadhi_devta_parashar = models.CharField(default='', max_length=30, db_column='PRATYADHI DEVTA AS PER PARASHAR', verbose_name='PRATYADHI DEVTA AS PER PARASHAR', blank=True)
    pratyadhi_devta_jaimini = models.CharField(default='', max_length=30, db_column='PRATYADHI DEVTA AS PER JAIMINI', verbose_name='PRATYADHI DEVTA AS PER JAIMINI', blank=True)
    vishi_avtaar = models.CharField(default='', max_length=30, db_column='VISHNU AVTAAR', verbose_name='VISHNU AVTAAR', blank=True)
    rishi = models.CharField(default='', max_length=30, db_column='RISHI', verbose_name='RISHI', blank=True)
    maha_vidhya = models.CharField(default='', max_length=30, db_column='MAHA-VIDHYA', verbose_name='MAHA-VIDHYA', blank=True)
    tattva_devta = models.CharField(default='', max_length=30, db_column='TATTVA DEVTA', verbose_name='TATTVA DEVTA', blank=True)
    mks1 = models.CharField(default='', max_length=30, db_column='MARAN KARAK STHAN 1(MKS1)FROM LAGNA/ ARUDHA/ BHAVA', verbose_name='MARAN KARAK STHAN 1(MKS1)FROM LAGNA/ ARUDHA/ BHAVA', blank=True)
    mks2 = models.CharField(default='', max_length=30, db_column='MARAN KARAK STHAN 2(MKS2)FROM LAGNA/ ARUDHA/ BHAVA', verbose_name='MARAN KARAK STHAN 2(MKS2)FROM LAGNA/ ARUDHA/ BHAVA', blank=True)
    jks1 = models.CharField(default='', max_length=30, db_column='JEEV KARAK STHAN 1(JKS1)FROM LAGNA/ ARUDHA/ BHAVA', verbose_name='JEEV KARAK STHAN 1(JKS1)FROM LAGNA/ ARUDHA/ BHAVA', blank=True)
    jks2 = models.CharField(default='', max_length=30, db_column='JEEV KARAK STHAN 2(JKS2)FROM LAGNA/ ARUDHA/ BHAVA', verbose_name='JEEV KARAK STHAN 2(JKS2)FROM LAGNA/ ARUDHA/ BHAVA', blank=True)
    varna_of_plaets = models.CharField(default='', max_length=30, db_column='VARNA OF PLANETS', verbose_name='VARNA OF PLANETS', blank=True)
    dhat_jeeva = models.CharField(default='', max_length=30, db_column='DHATU/MOOLA/JEEVA', verbose_name='DHATU/MOOLA/JEEVA', blank=True)
    sense_organs = models.CharField(default='', max_length=30, db_column='SENSE ORGANS', verbose_name='SENSE ORGANS', blank=True)
    sense = models.CharField(default='', max_length=30, db_column='SENSE', verbose_name='SENSE', blank=True)
    tattva = models.CharField(default='', max_length=30, db_column='TATTVA', verbose_name='TATTVA', blank=True)
    grains = models.CharField(default='', max_length=30, db_column='GRAINS', verbose_name='GRAINS', blank=True)
    metals = models.CharField(default='', max_length=30, db_column='METALS', verbose_name='METALS', blank=True)
    body_mark = models.CharField(default='', max_length=30, db_column='BODY MARK IN', verbose_name='BODY MARK IN', blank=True)
    side_mark = models.CharField(default='', max_length=30, db_column='SIDE HAVING A MARK', verbose_name='SIDE HAVING A MARK', blank=True)
    dry_wet = models.CharField(default='', max_length=30, db_column='DRY/WET', verbose_name='DRY/WET', blank=True)
    direction_sight = models.CharField(default='', max_length=30, db_column='DIRECTION OF SIGHT', verbose_name='DIRECTION OF SIGHT', blank=True)
    significant_karkatvas = models.CharField(default='', max_length=30, db_column='SIGNIFICANT KARKATVAS', verbose_name='SIGNIFICANT KARKATVAS', blank=True)
    rising = models.CharField(default='', max_length=30, db_column='RISING', verbose_name='RISING', blank=True)
    udaya = models.CharField(default='', max_length=30, db_column='UDAYA-HINDI', verbose_name='UDAYA (HINDI)', blank=True)
    
    class Meta:
        verbose_name = '44. Table Name: Characteristics of Planets Table (Table Code:44)'
        verbose_name_plural = '44. Table Name: Characteristics of Planets Table (Table Code:44)'

class Characterstics_of_Signs_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    as_per_writer = models.CharField(default='', max_length=30, db_column='As per writer', verbose_name='AS PER RISHI/EXPONENT/ WRITER/ASTROLOGER', blank=True)
    sign_rasi = models.CharField(default='',max_length=30, db_column='SIGN', verbose_name='SIGN/RASI',blank=True)
    synonym_rasi1 = models.CharField(default='', max_length=30, db_column='SYNONYMS OF SIGN/RASI 1', verbose_name='SYNONYMS OF SIGN/RASI 1', blank=True)
    synonym_rasi2 = models.CharField(default='', max_length=30, db_column='SYNONYMS OF SIGN/RASI 2', verbose_name='SYNONYMS OF SIGN/RASI 2', blank=True)
    symbol_rasi = models.CharField(default='', max_length=30, db_column='SYMBOL OF SIGN/RASI', verbose_name='SYMBOL OF SIGN/RASI', blank=True)
    ghatak_moon = models.CharField(default='', max_length=30, db_column='GHATAK MOON', verbose_name='GHATAK MOON', blank=True)
    ghatak_tithi_group =  models.CharField(default='', max_length=30, db_column='GHATAK TITHI GROUP', verbose_name='GHATAK TITHI GROUP', blank=True)
    ghatak_tithi =  models.CharField(default='', max_length=30, db_column='GHATAK TITHI', verbose_name='GHATAK TITHI', blank=True)
    ghatak_day = models.CharField(default='', max_length=30, db_column='GHATAK DAY', verbose_name='GHATAK DAY', blank=True)
    ghatak_nakshatra = models.CharField(default='', max_length=30, db_column='GHATAK NAKSHATRA', verbose_name='GHATAK NAKSHATRA', blank=True)
    ghatak_lagna = models.CharField(default='', max_length=30, db_column='GHATAK LAGNA (SAME SEX)', verbose_name='GHATAK LAGNA (SAME SEX)', blank=True)
    day_night =  models.CharField(default='', max_length=30, db_column='DAY/NIGHT', verbose_name='DAY/NIGHT', blank=True)
    rising = models.CharField(default='', max_length=30, db_column='RISING', verbose_name='RISING', blank=True)
    udaya = models.CharField(default='', max_length=30, db_column='UDAYA-HINDI', verbose_name='UDAYA (HINDI)', blank=True)
    mobility = models.CharField(default='', max_length=30, db_column='MOBILITY', verbose_name='MOBILITY', blank=True)
    hindi =  models.CharField(default='', max_length=30, db_column='HINDI', verbose_name='HINDI', blank=True)
    guna = models.CharField(default='', max_length=30, db_column='GUNA', verbose_name='CHARACTER/GUNA(HINDI', blank=True)
    direction = models.CharField(default='', max_length=30, db_column='DIRECTION', verbose_name='DIRECTION', blank=True)
    disha = models.CharField(default='', max_length=30, db_column='DISHA (HINDI)', verbose_name='DISHA (HINDI)', blank=True)
    element = models.CharField(default='', max_length=20, db_column='Element', verbose_name='Element', blank=True)
    tattva_hindi = models.CharField(default='', max_length=30, db_column='TATTVA-HINDI', verbose_name='TATTVA (HINDI)', blank=True)
    era = models.CharField(default='', max_length=20, db_column='ERA (YUGA)', verbose_name='ERA (YUGA)', blank=True)
    order_yuga = models.CharField(default='', max_length=30, db_column='ORDER OF YUGA', verbose_name='ORDER OF YUGA', blank=True)
    colour = models.CharField(default='', max_length=30, db_column='v', verbose_name='COLOUR', blank=True)
    rang = models.CharField(default='', max_length=30, db_column='RANG (HINDI)', verbose_name='RANG (HINDI)', blank=True)
    complexion = models.CharField(default='', max_length=30, db_column='COMPLEXION', verbose_name='COMPLEXION', blank=True)
    rangat = models.CharField(default='', max_length=30, db_column='(RANGAT) HINDI', verbose_name='(RANGAT) HINDI', blank=True)
    lenght_ascension = models.CharField(default='', max_length=30, db_column='LENGTH OF ASCENSION', verbose_name='LENGTH OF ASCENSION', blank=True)
    lambai = models.CharField(default='', max_length=30, db_column='LAMBAI (HINDI)', verbose_name='LAMBAI (HINDI)', blank=True)
    ayana = models.CharField(default='', max_length=30, db_column='AYANA', verbose_name='AYANA', blank=True)
    gender_signs_general = models.CharField(default='', max_length=30, db_column='GENDER OF THE SIGNS (RELATED TO GENERAL)', verbose_name='GENDER OF THE SIGNS (RELATED TO GENERAL)', blank=True)
    gender_signs_progeny = models.CharField(default='', max_length=30, db_column='GENDER OF THE SIGNS (RELATED TO PROGENY)', verbose_name='GENDER OF THE SIGNS (RELATED TO PROGENY)', blank=True)
    castes = models.CharField(default='', max_length=30, db_column='CASTES', verbose_name='CASTES', blank=True)
    description1 = models.CharField(default='', max_length=161, db_column='DESCRIPTION-1', verbose_name='DESCRIPTION', blank=True)
    description2 = models.CharField(default='', max_length=161, db_column='DESCRIPTION-2', verbose_name='DESCRIPTION', blank=True)
    description3 = models.CharField(default='', max_length=161, db_column='DESCRIPTION-3', verbose_name='DESCRIPTION', blank=True)
    description4 = models.CharField(default='', max_length=161, db_column='DESCRIPTION-4', verbose_name='DESCRIPTION', blank=True)
    description5 = models.CharField(default='', max_length=161, db_column='DESCRIPTION-5', verbose_name='DESCRIPTION', blank=True)
    description6 = models.CharField(default='', max_length=161, db_column='DESCRIPTION-6', verbose_name='DESCRIPTION', blank=True)
    description7 = models.CharField(default='', max_length=161, db_column='DESCRIPTION-7', verbose_name='DESCRIPTION', blank=True)
    planetary_flaws = models.CharField(default='', max_length=30, db_column='PLANETARY FLAWS', verbose_name='PLANETARY FLAWS', blank=True)
    dwelling_signs = models.CharField(default='', max_length=30, db_column='DWELLING OF SIGNS', verbose_name='DWELLING OF SIGNS', blank=True)
    jyotiriling = models.CharField(default='', max_length=30, db_column='JYOTIRLING', verbose_name='JYOTIRLING', blank=True)
    resiging_signs = models.CharField(default='', max_length=160, db_column='RESIDING OF SIGNS', verbose_name='RESIDING OF SIGNS', blank=True)
    sign_based_on_no_feet_pada = models.CharField(default='', max_length=160, db_column='SIGNS BASED ON NUMBER OF FEET-PADA', verbose_name='SIGNS BASED ON NUMBER OF FEET-PADA', blank=True)
    classification_signs = models.CharField(default='', max_length=30, db_column='CLASSIFACTION OF SIGN', verbose_name='CLASSIFACTION OF SIGN', blank=True)
    basis_classification = models.CharField(default='', max_length=151, db_column='BASIS OF CLASSIFICATION', verbose_name='BASIS OF CLASSIFICATION', blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    sign_based_on_no_feet_pada1 = models.CharField(default='', max_length=160, db_column='SIGNS BASED ON NUMBER OF FEET-PADA-1', verbose_name='SIGNS BASED ON NUMBER OF FEET-PADA', blank=True)
    classification_signs1 = models.CharField(default='', max_length=30, db_column='CLASSIFACTION OF SIGN-1', verbose_name='CLASSIFACTION OF SIGN', blank=True)
    basis_classification1 = models.CharField(default='', max_length=151, db_column='BASIS OF CLASSIFICATION-1', verbose_name='BASIS OF CLASSIFICATION', blank=True)
    from_extent1 = models.CharField(default = '', max_length = 30, db_column='From (SS-DD-MM-SS)-1', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent1 = models.CharField(default = '',max_length = 30, db_column='To (SS-DD-MM-SS)-1', verbose_name='To (SS-DD-MM-SS)', blank=True)
    # animal_kingdom_signs = models.CharField(default='', max_length=30, db_column='ANIMAL KINGDOM OF SIGNS', verbose_name='ANIMAL KINGDOM OF SIGNS', blank=True)
    door = models.CharField(default='', max_length=30, db_column='DOOR', verbose_name='DOOR', blank=True)
    jeeva = models.CharField(default='', max_length=30, db_column='DHATU/MOOLA/JEEVA', verbose_name='DHATU/MOOLA/JEEVA', blank=True)
    solar_lunar_half = models.CharField(default='', max_length=30, db_column='SOLAR OR LUNAR HALF', verbose_name='SOLAR OR LUNAR HALF', blank=True)
    barren_fruitful_sings = models.CharField(default='', max_length=30, db_column='BARREN OR FRUITFUL SIGNS', verbose_name='BARREN OR FRUITFUL SIGNS', blank=True)
    seasons = models.CharField(default='', max_length=30, db_column='SEASONS', verbose_name='SEASONS', blank=True)
    ritu_hidi = models.CharField(default='', max_length=30, db_column='RITU(HINDI)', verbose_name='RITU(HINDI)', blank=True)
    lord_of_season = models.CharField(default='', max_length=30, db_column='LORD OF SEASON (RITU)', verbose_name='LORD OF SEASON (RITU)', blank=True)
    rasi_dristi_sign1 = models.CharField(default='', max_length=30, db_column='RASI DRISTI ON SIGN 1', verbose_name='RASI DRISTI ON SIGN 1', blank=True)
    # name_dristi_1 = models.CharField(default='', max_length=30, db_column='NAME OF DRISTI-1', verbose_name='NAME OF DRISTI', blank=True)
    rasi_dristi_sign2 = models.CharField(default='', max_length=30, db_column='RASI DRISTI ON SIGN 2', verbose_name='RASI DRISTI ON SIGN 2', blank=True)
    # name_dristi_2 = models.CharField(default='', max_length=30, db_column='NAME OF DRISTI-2', verbose_name='NAME OF DRISTI', blank=True)
    rasi_dristi_sign3 = models.CharField(default='', max_length=30, db_column='RASI DRISTI ON SIGN 3', verbose_name='RASI DRISTI ON SIGN 3', blank=True)
    # name_dristi_3 = models.CharField(default='', max_length=30, db_column='NAME OF DRISTI-3', verbose_name='NAME OF DRISTI', blank=True)
    abimukha_rasi = models.CharField(default='', max_length=30, db_column='ABHIMUKHA RASI', verbose_name='ABHIMUKHA RASI', blank=True)
    samukha_rasi = models.CharField(default='', max_length=30, db_column='SAMUKHA RASI', verbose_name='SAMUKHA RASI', blank=True)
    badhaka_rashi = models.CharField(default='', max_length=30, db_column='BADHAKA RASHI', verbose_name='BADHAKA RASHI', blank=True)
    badhkesh = models.CharField(default='', max_length=30, db_column='BADHKESH', verbose_name='BADHKESH', blank=True)
    built = models.CharField(default='', max_length=30, db_column='BUILT', verbose_name='BUILT', blank=True)
    content_water_sign = models.CharField(default='', max_length=30, db_column='CONTENT OF WATER IN SIGN', verbose_name='CONTENT OF WATER IN SIGN', blank=True)
    rasi_tattva = models.CharField(default='', max_length=30, db_column='RASI TATTVA', verbose_name='RASI TATTVA', blank=True)
    blind_sign = models.CharField(default='', max_length=30, db_column='BLIND/DUMB/LAME SIGN', verbose_name='BLIND/DUMB/LAME SIGN', blank=True)
    during_time = models.CharField(default='', max_length=30, db_column='DURING TIME', verbose_name='DURING TIME', blank=True)

    
    class Meta:
        verbose_name = '45. CHARECTERISTICS OF SIGN (TABLE CODE: 45)'
        verbose_name_plural = '45. CHARECTERISTICS OF SIGN (TABLE CODE: 45)'

    

class Characterstics_of_Houses_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    as_per_writer = models.CharField(default='', max_length=30, db_column='As per writer', verbose_name='AS PER RISHI/EXPONENT/ WRITER/ASTROLOGER', blank=True)
    ref_code = models.CharField(default='', max_length=30, db_column='REFERENCE CODE', verbose_name='REFERENCE CODE', blank=True)
    house_no = models.CharField(default='', max_length=30, db_column='HOUSE No', verbose_name='HOUSE No', blank=True)
    synonym1 = models.CharField(default='', max_length=30, db_column='SYNONYM 1', verbose_name='SYNONYM 1', blank=True)
    synonym2 = models.CharField(default='', max_length=30, db_column='SYNONYM 2', verbose_name='SYNONYM 2', blank=True)
    synonym3 = models.CharField(default='', max_length=30, db_column='SYNONYM 3', verbose_name='SYNONYM 3', blank=True)
    synonym4 = models.CharField(default='', max_length=30, db_column='SYNONYM 4', verbose_name='SYNONYM 4', blank=True)
    classification1 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 1 (THE KENDRA)', verbose_name='CLASSIFICATION 1 (THE KENDRA)', blank=True)
    classification2 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 2 (THE TRIKONA)', verbose_name='CLASSIFICATION 2 (THE TRIKONA)', blank=True)
    classification3 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 3 (THE DUSTHANA)', verbose_name='CLASSIFICATION 3 (THE DUSTHANA)', blank=True)
    classification4 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 4 (THE CHATURASRA)', verbose_name='CLASSIFICATION 4 (THE CHATURASRA)', blank=True)
    classification5 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 5 (THE UPACHAYA)', verbose_name='CLASSIFICATION 5 (THE UPACHAYA)', blank=True)
    classification6 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 6 (THE TRISADAYA)', verbose_name='CLASSIFICATION 6 (THE TRISADAYA)', blank=True)
    classification7 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 7 (THE MARAKA)', verbose_name='CLASSIFICATION 7 (THE MARAKA)', blank=True)
    classification8 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 8', verbose_name='CLASSIFICATION 8', blank=True)
    classification9 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 9 (KALPURUSA DIVISION)', verbose_name='CLASSIFICATION 9 (KALPURUSA DIVISION)', blank=True)
    classification10 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 10 (VISIBILITY DIVISION)', verbose_name='CLASSIFICATION 10 (VISIBILITY DIVISION)', blank=True)
    classification11 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 11 (ORIENTAL/OCCIDENTAL DIVISION)', verbose_name='CLASSIFICATION 11 (ORIENTAL/OCCIDENTAL DIVISION)', blank=True)
    classification12 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 12', verbose_name='CLASSIFICATION 12', blank=True)
    classification13 = models.CharField(default='', max_length=30, db_column='CLASSIFICATION 13 (THE LINASTHANA)', verbose_name='CLASSIFICATION 13 (THE LINASTHANA)', blank=True)

    class Meta:
        verbose_name = '46. Table Name: Characteristics of Houses Table (Table Code:46)'
        verbose_name_plural = '46. Table Name: Characteristics of Houses Table (Table Code:46)'

class Karaka_of_Houses_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    house_no = models.CharField(default='', max_length=30, db_column='HOUSE No', verbose_name='HOUSE No', blank=True)
    as_per_writer = models.CharField(default='', max_length=30, db_column='As per writer', verbose_name='AS PER RISHI/EXPONENT/ WRITER/ASTROLOGER', blank=True)
    ref_code = models.CharField(default='', max_length=30, db_column='REFERENCE CODE', verbose_name='REFERENCE CODE', blank=True)
    karakkatva1 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-1', verbose_name='KARAKATTVA OF 1', blank=True)
    karakkatva2 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-2', verbose_name='KARAKATTVA OF 2', blank=True)
    karakkatva3 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-3', verbose_name='KARAKATTVA OF 3', blank=True)
    karakkatva4 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-4', verbose_name='KARAKATTVA OF 4', blank=True)
    karakkatva5 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-5', verbose_name='KARAKATTVA OF 5', blank=True)
    karakkatva6 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-6', verbose_name='KARAKATTVA OF 6', blank=True)
    karakkatva7 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-7', verbose_name='KARAKATTVA OF 7', blank=True)
    karakkatva8 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-8', verbose_name='KARAKATTVA OF 8', blank=True)
    karakkatva9 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-9', verbose_name='KARAKATTVA OF 9', blank=True)
    karakkatva10 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-10', verbose_name='KARAKATTVA OF 10', blank=True)
    karakkatva11 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-11', verbose_name='KARAKATTVA OF 11', blank=True)
    karakkatva12 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-12', verbose_name='KARAKATTVA OF 12', blank=True)
    karakkatva13 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-13', verbose_name='KARAKATTVA OF 13', blank=True)
    karakkatva14 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-14', verbose_name='KARAKATTVA OF 14', blank=True)
    karakkatva15 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-15', verbose_name='KARAKATTVA OF 15', blank=True)
    karakkatva16 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-16', verbose_name='KARAKATTVA OF 16', blank=True)
    karakkatva17 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-17', verbose_name='KARAKATTVA OF 17', blank=True)
    karakkatva18 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-18', verbose_name='KARAKATTVA OF 18', blank=True)
    karakkatva19 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-19', verbose_name='KARAKATTVA OF 19', blank=True)
    karakkatva20 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-20', verbose_name='KARAKATTVA OF 20', blank=True)
    karakkatva21 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-21', verbose_name='KARAKATTVA OF 21', blank=True)
    karakkatva22 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-22', verbose_name='KARAKATTVA OF 22', blank=True)
    karakkatva23 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-23', verbose_name='KARAKATTVA OF 23', blank=True)
    karakkatva24 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-24', verbose_name='KARAKATTVA OF 24', blank=True)
    karakkatva25 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-25', verbose_name='KARAKATTVA OF 25', blank=True)
    karakkatva26 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-26', verbose_name='KARAKATTVA OF 26', blank=True)
    karakkatva27 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-27', verbose_name='KARAKATTVA OF 27', blank=True)
    karakkatva28 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-28', verbose_name='KARAKATTVA OF 28', blank=True)
    karakkatva29 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-29', verbose_name='KARAKATTVA OF 29', blank=True)
    karakkatva30 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-30', verbose_name='KARAKATTVA OF 30', blank=True)
    karakkatva31 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-31', verbose_name='KARAKATTVA OF 31', blank=True)
    karakkatva32 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-32', verbose_name='KARAKATTVA OF 32', blank=True)
    karakkatva33 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-33', verbose_name='KARAKATTVA OF 33', blank=True)
    karakkatva34 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-34', verbose_name='KARAKATTVA OF 34', blank=True)
    karakkatva35 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-35', verbose_name='KARAKATTVA OF 35', blank=True)
    karakkatva36 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-36', verbose_name='KARAKATTVA OF 36', blank=True)
    karakkatva37 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-37', verbose_name='KARAKATTVA OF 37', blank=True)
    karakkatva38 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-38', verbose_name='KARAKATTVA OF 38', blank=True)
    karakkatva39 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-39', verbose_name='KARAKATTVA OF 39', blank=True)
    karakkatva40 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-40', verbose_name='KARAKATTVA OF 40', blank=True)
    karakkatva41 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-41', verbose_name='KARAKATTVA OF 41', blank=True)
    karakkatva42 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-42', verbose_name='KARAKATTVA OF 42', blank=True)
    karakkatva43 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-43', verbose_name='KARAKATTVA OF 43', blank=True)
    karakkatva44 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-44', verbose_name='KARAKATTVA OF 44', blank=True)
    karakkatva45 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-45', verbose_name='KARAKATTVA OF 45', blank=True)
    karakkatva46 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-46', verbose_name='KARAKATTVA OF 56', blank=True)
    karakkatva47 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-47', verbose_name='KARAKATTVA OF 47', blank=True)
    karakkatva48 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-48', verbose_name='KARAKATTVA OF 48', blank=True)
    karakkatva49 = models.CharField(default='', max_length=30, db_column='KARAKATTVA OF-49', verbose_name='KARAKATTVA OF 49', blank=True)
    

    class Meta:
        verbose_name = '47. Table Name: Karaka Of Houses Table (Table Code:47)'
        verbose_name_plural = '47. Table Name: Karaka Of Houses Table (Table Code:47)'

class Materialistic_things_differentiation_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    planet_class = models.CharField(default='', max_length=30, db_column='PLANET CLASS', verbose_name='PLANET CLASS', blank=True)
    planet_in_signed = models.CharField(default='', max_length=30, db_column='PLANET IN SIGN OWNED BY PLANET CLASS', verbose_name='PLANET IN SIGN OWNED BY PLANET CLASS', blank=True)
    planet_in_dreskana = models.CharField(default='', max_length=30, db_column='PLANET IN DRESKANA OWNED BY PLANET CLASS', verbose_name='PLANET IN DRESKANA OWNED BY PLANET CLASS', blank=True)
    planet_in_navamsa = models.CharField(default='', max_length=30, db_column='PLANET IN NAVAMSA OWNED BY PLANET CLASS', verbose_name='PLANET IN NAVAMSA OWNED BY PLANET CLASS', blank=True)
    planet_accepted = models.CharField(default='', max_length=30, db_column='PLANET ASPECTED BY PLANET CLASS', verbose_name='PLANET ASPECTED BY PLANET CLASS', blank=True)
    result = models.CharField(default='', max_length=161, db_column='RESULT', verbose_name='RESULT', blank=True)

    class Meta:
        verbose_name = '48. Table Name: Materialistic Things Differentiation (Dhatu/Moola/Jeeva) Table (Table Code:48)'
        verbose_name_plural = '48. Table Name: Materialistic Things Differentiation (Dhatu/Moola/Jeeva) Table (Table Code:48)'

class Direction_of_planet_dikpala_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    planet = models.CharField(default='', max_length=30, db_column='PLANET', verbose_name='PLANET', blank=True)
    direction = models.CharField(default='', max_length=30, db_column='DIRECTION', verbose_name='DIRECTION', blank=True)
    dikpala = models.CharField(default='', max_length=30, db_column='DIKPALA', verbose_name='DIKPALA', blank=True)
    tattva = models.CharField(default='', max_length=30, db_column='TATTVA', verbose_name='TATTVA', blank=True)
    welding = models.CharField(default='', max_length=30, db_column='WIELDING', verbose_name='WIELDING', blank=True)
    cosort = models.CharField(default='', max_length=30, db_column='CONSORT', verbose_name='CONSORT', blank=True)

    class Meta:
        verbose_name = '49. Table Name: Direction of Planets, Dikpala etc Table (Table Code:49)'
        verbose_name_plural = '49. Table Name: Direction of Planets, Dikpala etc Table (Table Code:49)'

class Direction_of_planet_sign_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    planet = models.CharField(default='', max_length=30, db_column='PLANET', verbose_name='PLANET', blank=True)
    direction = models.CharField(default='', max_length=30, db_column='DIRECTION', verbose_name='DIRECTION', blank=True)
    sign1 = models.CharField(default='', max_length=160, db_column='SIGNS 1', verbose_name='SIGNS 1', blank=True)
    sign2 = models.CharField(default='', max_length=160, db_column='SIGNS 2', verbose_name='SIGNS 2', blank=True)
    bhava = models.CharField(default='', max_length=30, db_column='BHAVA', verbose_name='BHAVA', blank=True)

    class Meta:
        verbose_name = '50. Table Name: Direction of Planets, Signs etc Table (Table Code:50)'
        verbose_name_plural = '50. Table Name: Direction of Planets, Signs etc Table (Table Code:50)'

class Digbala_of_planet_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    direction = models.CharField(default='', max_length=30, db_column='DIRECTION', verbose_name='DIRECTION', blank=True)
    planet = models.CharField(default='', max_length=30, db_column='PLANET', verbose_name='Dikbali PLANET', blank=True)
    tattva = models.CharField(default='', max_length=30, db_column='TATTVA', verbose_name='TATTVA', blank=True)
    governer = models.CharField(default='', max_length=30, db_column='GOVERNER', verbose_name='GOVERNER', blank=True)
    assoc_signs = models.CharField(default='', max_length=160, db_column='ASSOCIATED SIGNS', verbose_name='ASSOCIATED SIGNS', blank=True)
    dikpala = models.CharField(default='', max_length=30, db_column='DIKPALA', verbose_name='DIKPALA', blank=True)
    bhava = models.CharField(default='', max_length=30, db_column='BHAVA', verbose_name='BHAVA', blank=True)

    class Meta:
        verbose_name = '51. Table Name: DigBala of Planets Table (Table Code:51)'
        verbose_name_plural = '51. Table Name: DigBala of Planets Table (Table Code:51)'

class Kundalini_chakra_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    kundalini_chakra = models.CharField(default='', max_length=30, db_column='KUNDALINI CHAKRA', verbose_name='KUNDALINI CHAKRA', blank=True)
    meaning = models.CharField(default='', max_length=30, db_column='MEANING', verbose_name='MEANING', blank=True)
    padma = models.CharField(default='', max_length=30, db_column='PADMA', verbose_name='PADMA', blank=True)
    colour = models.CharField(default='', max_length=30, db_column='v', verbose_name='COLOUR', blank=True)
    bijakshra = models.CharField(default='', max_length=30, db_column='BIJAKSHRA', verbose_name='BIJAKSHRA', blank=True)
    bhuta = models.CharField(default='', max_length=30, db_column='BHUTA', verbose_name='BHUTA', blank=True)
    karaka1 = models.CharField(default='', max_length=30, db_column='KARAKA 1', verbose_name='KARAKA 1', blank=True)
    karaka2 = models.CharField(default='', max_length=30, db_column='KARAKA 2', verbose_name='KARAKA 2', blank=True)

    class Meta:
        verbose_name = '52. Table Name: Kundalini Chakra Table (Table Code:52)'
        verbose_name_plural = '52. Table Name: Kundalini Chakra Table (Table Code:52)'

class Combination_of_rising_planets_sings_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    kind_graha = models.CharField(default='', max_length=30, db_column='KIND OF GRAHA', verbose_name='KIND OF GRAHA', blank=True)
    name_graha = models.CharField(default='', max_length=30, db_column='NAME OF GRAHA ', verbose_name='NAME OF GRAHA ', blank=True)
    kind_rashi = models.CharField(default='', max_length=30, db_column='KIND OF RASHI', verbose_name='KIND OF RASHI', blank=True)
    name_rashi = models.CharField(default='', max_length=30, db_column='NAME OF RASHI', verbose_name='NAME OF RASHI', blank=True)
    result = models.CharField(default='', max_length=160, db_column='RESULT', verbose_name='RESULT', blank=True)

    class Meta:
        verbose_name = '53. Table Name: Combination (On the Basis)of Rising pattern of Planets and Signs Table (Table Code:53)'
        verbose_name_plural = '53. Table Name: Combination (On the Basis)of Rising pattern of Planets and Signs Table (Table Code:53)'

class Gharba_karak_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    rank_of_pregnancy = models.CharField(default='', max_length=30, db_column='RANK OF PREGNANCY', verbose_name='RANK OF PREGNANCY', blank=True)
    significator_planet = models.CharField(default='', max_length=30, db_column='SIGNIFICATOR PLANET (KARAK)', verbose_name='SIGNIFICATOR PLANET (KARAK)', blank=True)

    class Meta:
        verbose_name = '54. Table Name: Garbha Karak Table (Table Code:54)'
        verbose_name_plural = '54. Table Name: Garbha Karak Table (Table Code:54)'

class Pachaakadi_Sambandha_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    pachakaadi_sambhandh = models.CharField(default='', max_length=30, db_column='PACHAKAADI SAMBANDH', verbose_name='PACHAKAADI SAMBANDH', blank=True)
    from_sun = models.CharField(default='', max_length=30, db_column='FROM SUN', verbose_name='FROM SUN', blank=True)
    from_moon = models.CharField(default='', max_length=30, db_column='FROM MOON', verbose_name='FROM MOON', blank=True)
    from_mars = models.CharField(default='', max_length=30, db_column='FROM MARS', verbose_name='FROM MARS', blank=True)
    from_mercury = models.CharField(default='', max_length=30, db_column='FROM MERCURY', verbose_name='FROM MERCURY', blank=True)
    from_jupiter = models.CharField(default='', max_length=30, db_column='FROM JUPITER', verbose_name='FROM JUPITER', blank=True)
    from_venus = models.CharField(default='', max_length=30, db_column='FROM VENUS', verbose_name='FROM VENUS', blank=True)
    from_saturn = models.CharField(default='', max_length=30, db_column='FROM SATURN', verbose_name='FROM SATURN', blank=True)

    class Meta:
        verbose_name = '55. Table Name: Pachaakadi Sambandha (Graha to Graha) Table (Table Code:55-A)'
        verbose_name_plural = '55. Table Name: Pachaakadi Sambandha (Graha to Graha) Table (Table Code:55-A)'
        
class Pachaakadi_Sambandha_B_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    pachakaadi_sambhandh = models.CharField(default='', max_length=30, db_column='PACHAKAADI SAMBANDH', verbose_name='PACHAKAADI SAMBANDH', blank=True)
    from_sun = models.CharField(default='', max_length=30, db_column='FROM SUN', verbose_name='FROM SUN', blank=True)
    from_moon = models.CharField(default='', max_length=30, db_column='FROM MOON', verbose_name='FROM MOON', blank=True)
    from_mars = models.CharField(default='', max_length=30, db_column='FROM MARS', verbose_name='FROM MARS', blank=True)
    from_mercury = models.CharField(default='', max_length=30, db_column='FROM MERCURY', verbose_name='FROM MERCURY', blank=True)
    from_jupiter = models.CharField(default='', max_length=30, db_column='FROM JUPITER', verbose_name='FROM JUPITER', blank=True)
    from_venus = models.CharField(default='', max_length=30, db_column='FROM VENUS', verbose_name='FROM VENUS', blank=True)
    from_saturn = models.CharField(default='', max_length=30, db_column='FROM SATURN', verbose_name='FROM SATURN', blank=True)

    class Meta:
        verbose_name = '56. Table Name: Pachaakadi Sambandha (Graha to Bhava) Table (Table Code:55-B)'
        verbose_name_plural = '56. Table Name: Pachaakadi Sambandha (Graha to Bhava) Table (Table Code:55-B)'

class Vaar_Chakra_using_7_planets_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    sequence = models.CharField(default='', max_length=20, db_column='SEQUENCE', verbose_name='SEQUENCE (IN VAAR CHAKRA)', blank=True)
    sunday = models.CharField(default='', max_length=20, db_column='SUNDAY', verbose_name='SUNDAY', blank=True)
    monday = models.CharField(default='', max_length=20, db_column='MONDAY', verbose_name='MONDAY', blank=True)
    tuesday = models.CharField(default='', max_length=20, db_column='TUESDAY', verbose_name='TUESDAY', blank=True)
    wednesday = models.CharField(default='', max_length=20, db_column='WEDNESDAY', verbose_name='WEDNESDAY', blank=True)
    thursday = models.CharField(default='', max_length=20, db_column='THURSDAY', verbose_name='THURSDAY', blank=True)
    friday = models.CharField(default='', max_length=20, db_column='FRIDAY', verbose_name='FRIDAY', blank=True)
    saturday = models.CharField(default='', max_length=20, db_column='SATURDAY', verbose_name='SATURDAY', blank=True)

    class Meta:
        verbose_name = '57. Table Name: Vaar Chakra Table (Using 7 planets) Table (Table Code:56-A)'
        verbose_name_plural = '57. Table Name: Vaar Chakra Table (Using 7 planets) Table (Table Code:56-A)'

class Vaar_Chakra_using_9_planets_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    sequence = models.CharField(default='', max_length=20, db_column='SEQUENCE', verbose_name='SEQUENCE (IN VAAR CHAKRA)', blank=True)
    sunday = models.CharField(default='', max_length=20, db_column='SUNDAY', verbose_name='SUNDAY', blank=True)
    monday = models.CharField(default='', max_length=20, db_column='MONDAY', verbose_name='MONDAY', blank=True)
    tuesday = models.CharField(default='', max_length=20, db_column='TUESDAY', verbose_name='TUESDAY', blank=True)
    wednesday = models.CharField(default='', max_length=20, db_column='WEDNESDAY', verbose_name='WEDNESDAY', blank=True)
    thursday = models.CharField(default='', max_length=20, db_column='THURSDAY', verbose_name='THURSDAY', blank=True)
    friday = models.CharField(default='', max_length=20, db_column='FRIDAY', verbose_name='FRIDAY', blank=True)
    saturday = models.CharField(default='', max_length=20, db_column='SATURDAY', verbose_name='SATURDAY', blank=True)

    class Meta:
        verbose_name = '58. Table Name: Vaar Chakra Table (Using 9 planets) Table (Table Code:56-B)'
        verbose_name_plural = '58. Table Name: Vaar Chakra Table (Using 9 planets) Table (Table Code:56-B)'

class Houses_from_Pranpada_Lagna_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    houses_from_pranpada = models.CharField(default='', max_length=20, db_column='HOUSES FROM PRANPADA (PP) LAGNA', verbose_name='HOUSES FROM PRANPADA (PP) LAGNA', blank=True)
    panch_prana = models.CharField(default='', max_length=20, db_column='PANCH PRANA', verbose_name='PANCH PRANA', blank=True)
    tattva = models.CharField(default='', max_length=30, db_column='TATTVA', verbose_name='TATTVA', blank=True)
    graha = models.CharField(default='', max_length=20, db_column='GRAHA', verbose_name='GRAHA', blank=True)
    controls = models.CharField(default='', max_length=20, db_column='CONTROLS', verbose_name='CONTROLS', blank=True)
    graha1 = models.CharField(default='', max_length=20, db_column='GRAHA-1', verbose_name='GRAHA', blank=True)
    karaka = models.CharField(default='', max_length=20, db_column='KARAKA', verbose_name='KARAKA', blank=True)
    
    class Meta:
        verbose_name = '59. Table Name: Houses from Pranpada Lagna Table (Table Code:57)'
        verbose_name_plural = '59. Table Name: Houses from Pranpada Lagna Table (Table Code:57)'

class Life_cycle_of_creature_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    creature_group = models.CharField(default='', max_length=20, db_column='CREATURE GROUP', verbose_name='CREATURE GROUP', blank=True)
    full_life =  models.CharField(default='', max_length=20, db_column='FULL LIFE (YEARS)', verbose_name='FULL LIFE (YEARS)', blank=True)
    mutiplier = models.CharField(default='', max_length=20, db_column='MULTIPLIER', verbose_name='MULTIPLIER', blank=True)
    max_dasa_per_rasi = models.CharField(default='', max_length=20, db_column='MAXIMUM DASA PER RASI (YEARS)', verbose_name='MAXIMUM DASA PER RASI (YEARS)', blank=True)
    rasi = models.CharField(default='', max_length=20, db_column='YEARS/RASI', verbose_name='YEARS/RASI', blank=True)
    total_rasis = models.CharField(default='', max_length=20, db_column='TOTAL RASIS', verbose_name='TOTAL RASIS', blank=True)
    total_dasa = models.CharField(default='', max_length=20, db_column='TOTAL DASA IN ALL RASIS(YEARS)', verbose_name='TOTAL DASA IN ALL RASIS(YEARS)', blank=True)

    class Meta:
        verbose_name = '60. Table Name: Life Cycle for Creatures Table (Table Code:58)'
        verbose_name_plural = '60. Table Name: Life Cycle for Creatures Table (Table Code:58)'

class Charakarak_bhava_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    houses = models.CharField(default='', max_length=20, db_column='HOUSES', verbose_name='HOUSES', blank=True)
    as_per_parashar = models.CharField(default='', max_length=20, db_column='AS PER PARASHAR', verbose_name='AS PER PARASHAR', blank=True)
    as_per_parampara1 = models.CharField(default='', max_length=20, db_column='AS PER ACHYUTANAND PARAMPARA 1', verbose_name='AS PER ACHYUTANAND PARAMPARA 1', blank=True)
    as_per_parampara2 = models.CharField(default='', max_length=20, db_column='AS PER ACHYUTANAND PARAMPARA 2', verbose_name='AS PER ACHYUTANAND PARAMPARA 2', blank=True)
    as_per_parampara3 = models.CharField(default='', max_length=20, db_column='AS PER ACHYUTANAND PARAMPARA 3', verbose_name='AS PER ACHYUTANAND PARAMPARA 3', blank=True)

    class Meta:
        verbose_name = '61. Table Name: CharaKarak & Bhava Table (Table Code:59)'
        verbose_name_plural = '61. Table Name: CharaKarak & Bhava Table (Table Code:59)'

class Form_sun_god_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    if_lagna_loris =  models.CharField(default='', max_length=20, db_column='IF LAGNA LORS IS', verbose_name='IF LAGNA LORS IS', blank=True)
    form_sun_god = models.CharField(default='', max_length=20, db_column='FORM OF SUN GOD (ADITYA HRDAYA )', verbose_name='FORM OF SUN GOD (ADITYA HRDAYA )', blank=True)

    class Meta:
        verbose_name = '62. Table Name: Form of Sun God(Aditya Hrdya) Table (Table Code:60)'
        verbose_name_plural = '62. Table Name: Form of Sun God(Aditya Hrdya) Table (Table Code:60)'

class Primary_argala_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_primary_intervention = models.CharField(default='', max_length=20, db_column='NAME OF PRIMARY INTERVENTION', verbose_name='NAME OF PRIMARY INTERVENTION (PRADHAN ARAGALA KA NAAM)', blank=True)
    planets_houses_special = models.CharField(default='', max_length=20, db_column='PLANETS IN THE HOUSE No FROM ANY SPECIAL POINT/ PLANETS/SIGN', verbose_name='PLANETS IN THE HOUSE No FROM ANY SPECIAL POINT/ PLANETS/SIGN', blank=True)
    planets_houses_special_obsc = models.CharField(default='', max_length=20, db_column='PLANETS IN THE HOUSE No FROM ANY SPECIAL POINT/PLANETS/SIGN OBSTRUCTION(VIRODH ARAGALA)', verbose_name='PLANETS IN THE HOUSE No FROM ANY SPECIAL POINT/PLANETS/SIGN OBSTRUCTION(VIRODH ARAGALA)', blank=True)
    
    class Meta:
        verbose_name = '63. Table Name: Primary Argala -Virodh Table (Table Code:61)'
        verbose_name_plural = '63. Table Name: Primary Argala -Virodh Table (Table Code:61)'
    
class Secondary_argala_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_secondary_intervention = models.CharField(default='', max_length=20, db_column='NAME OF SECONDARY INTERVENTION', verbose_name='NAME OF SECONDARY INTERVENTION(PRADHAN ARAGALA KA NAAM)', blank=True)
    planets_houses_special = models.CharField(default='', max_length=20, db_column='PLANETS IN THE HOUSE No FROM ANY SPECIAL POINT/ PLANETS/SIGN', verbose_name='PLANETS IN THE HOUSE No FROM ANY SPECIAL POINT/ PLANETS/SIGN', blank=True)
    planets_houses_special_obsc = models.CharField(default='', max_length=20, db_column='LANETS IN THE HOUSE No FROM ANY SPECIAL POINT/PLANETS/SIGN OBSTRUCTION (VIRODH ARAGALA)', verbose_name='LANETS IN THE HOUSE No FROM ANY SPECIAL POINT/PLANETS/SIGN OBSTRUCTION (VIRODH ARAGALA)', blank=True)
    
    class Meta:
        verbose_name = '64. Table Name: Secondary Argala-Virodh Table (Table Code:62)'
        verbose_name_plural = '64. Table Name: Secondary Argala-Virodh Table (Table Code:62)'

class Arudha_lagna_determination_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    lord_house1 = models.CharField(default='', max_length=20, db_column='LORD OF 1ST HOUSE IN', verbose_name='LORD OF 1ST HOUSE IN', blank=True)
    a1_in = models.CharField(default='', max_length=20, db_column='A1 IN', verbose_name='A1 IN', blank=True)
    lord_house2 = models.CharField(default='', max_length=20, db_column='LORD OF 2ND HOUSE IN', verbose_name='LORD OF 2ND HOUSE IN', blank=True)
    a2_in = models.CharField(default='', max_length=20, db_column='A2 IN', verbose_name='A2 IN', blank=True)
    lord_house3 = models.CharField(default='', max_length=20, db_column='LORD OF 3RD HOUSE IN', verbose_name='LORD OF 3RD HOUSE IN', blank=True)
    a3_in = models.CharField(default='', max_length=20, db_column='A3 IN', verbose_name='A3 IN', blank=True)
    lord_house4 = models.CharField(default='', max_length=20, db_column='LORD OF 4th HOUSE IN', verbose_name='LORD OF 4th HOUSE IN', blank=True)
    a4_in = models.CharField(default='', max_length=20, db_column='A4 IN', verbose_name='A4 IN', blank=True)
    lord_house5 = models.CharField(default='', max_length=20, db_column='LORD OF 5th HOUSE IN', verbose_name='LORD OF 5th HOUSE IN', blank=True)
    a5_in = models.CharField(default='', max_length=20, db_column='A5 IN', verbose_name='A5 IN', blank=True)
    lord_house6 = models.CharField(default='', max_length=20, db_column='LORD OF 6th HOUSE IN', verbose_name='LORD OF 6th HOUSE IN', blank=True)
    a6_in = models.CharField(default='', max_length=20, db_column='A6 IN', verbose_name='A6 IN', blank=True)    
    lord_house7 = models.CharField(default='', max_length=20, db_column='LORD OF 7th HOUSE IN', verbose_name='LORD OF 7th HOUSE IN', blank=True)
    a7_in = models.CharField(default='', max_length=20, db_column='A7 IN', verbose_name='A7 IN', blank=True)    
    lord_house8 = models.CharField(default='', max_length=20, db_column='LORD OF 8th HOUSE IN', verbose_name='LORD OF 8th HOUSE IN', blank=True)
    a8_in = models.CharField(default='', max_length=20, db_column='A8 IN', verbose_name='A8 IN', blank=True)    
    lord_house9 = models.CharField(default='', max_length=20, db_column='LORD OF 9th HOUSE IN', verbose_name='LORD OF 9th HOUSE IN', blank=True)
    a9_in = models.CharField(default='', max_length=20, db_column='A9 IN', verbose_name='A9 IN', blank=True) 
    lord_house10 = models.CharField(default='', max_length=20, db_column='LORD OF 10th HOUSE IN', verbose_name='LORD OF 10th HOUSE IN', blank=True)
    a10_in = models.CharField(default='', max_length=20, db_column='A10 IN', verbose_name='A10 IN', blank=True) 
    lord_house11 = models.CharField(default='', max_length=20, db_column='LORD OF 11th HOUSE IN', verbose_name='LORD OF 11th HOUSE IN', blank=True)
    a11_in = models.CharField(default='', max_length=20, db_column='A11 IN', verbose_name='A11 IN', blank=True) 
    lord_house12 = models.CharField(default='', max_length=20, db_column='LORD OF 12th HOUSE IN', verbose_name='LORD OF 12th HOUSE IN', blank=True)
    a12_in = models.CharField(default='', max_length=20, db_column='A12 IN', verbose_name='A12 IN', blank=True) 

    class Meta:
        verbose_name = '65. Table Name: Arudha Lagna Determination Table (Table Code:63)'
        verbose_name_plural = '65. Table Name: Arudha Lagna Determination Table (Table Code:63)'

class Arudha_nomenclature_meaning_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_arudha = models.CharField(default='', max_length=20, db_column='NAME OF ARUDHA', verbose_name='NAME OF ARUDHA', blank=True)
    abbrev = models.CharField(default='', max_length=20, db_column='ABBREVATION', verbose_name='ABBREVATION', blank=True)
    meaning = models.CharField(default='', max_length=20, db_column='MEANING', verbose_name='MEANING', blank=True)

    class Meta:
        verbose_name = '66. Table Name: Arudha Nomenclature & Meaning Table (Table Code:64)'
        verbose_name_plural = '66. Table Name: Arudha Nomenclature & Meaning Table (Table Code:64)'

class Vriddhas_as_per_sahmita_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_samhita = models.CharField(default='', max_length=20, db_column='SAMHITA NAME', verbose_name='SAMHITA NAME', blank=True)
    seq_no = models.CharField(default='', max_length=20, db_column='SEQUENCE/SERIAL No', verbose_name='SEQUENCE/SERIAL No', blank=True)
    name_vriddha = models.CharField(default='', max_length=20, db_column='NAME OF VRIDDHA/RISHI', verbose_name='NAME OF VRIDDHA/RISHI', blank=True)
    
    class Meta:
        verbose_name = '67. Table Name: Vriddhas As Per Various Samhita Table (Table Code:65)'
        verbose_name_plural = '67. Table Name: Vriddhas As Per Various Samhita Table (Table Code:65)'

class Tattvas_of_nakshatra_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    paksha = models.CharField(default='', max_length=20, db_column='PAKSHA', verbose_name='PAKSHA', blank=True)
    disha = models.CharField(default='', max_length=20, db_column='DISHA', verbose_name='DISHA', blank=True)
    tattva = models.CharField(default='', max_length=20, db_column='TATTVA', verbose_name='TATTVA', blank=True)
    name_nakshatra = models.CharField(default='', max_length=20, db_column='NAME OF NAKSHTRA', verbose_name='NAME OF NAKSHTRA', blank=True)

    class Meta:
        verbose_name = '68. Table Name: Tattvas of Nakshatras Table (Table Code:66)'
        verbose_name_plural = '68. Table Name: Tattvas of Nakshatras Table (Table Code:66)'

class Houses_gunas_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    houses_from_arudha_lagna = models.CharField(default='', max_length=20, db_column='HOUSE(S) FROM ARUDHA LAGNA', verbose_name='HOUSE(S) FROM ARUDHA LAGNA', blank=True)
    seq_no = models.CharField(default='', max_length=20, db_column='SEQUENCE/SERIAL No', verbose_name='SEQUENCE/SERIAL No', blank=True)
    aum_alphabets = models.CharField(default='', max_length=20, db_column='AUM ALPHABETS', verbose_name='AUM ALPHABETS', blank=True)
    pos_signification = models.CharField(default='', max_length=20, db_column='POSITIVE SIGNIFICATION (STRONG)', verbose_name='POSITIVE SIGNIFICATION (STRONG)', blank=True)
    neg_signification = models.CharField(default='', max_length=20, db_column='NEGATIVE SIGNIFICATION (WEAK)', verbose_name='NEGATIVE SIGNIFICATION (WEAK)', blank=True)
    neut_signification =  models.CharField(default='', max_length=20, db_column='NEUTRAL SIGNIFICATION (AVERAGE)', verbose_name='NEUTRAL SIGNIFICATION (AVERAGE)', blank=True)
    
    class Meta:
        verbose_name = '69. Table Name: Houses & Guna Table (Table Code:67)'
        verbose_name_plural = '69. Table Name: Houses & Guna Table (Table Code:67))'
    
class Devta_guna_arudha_strength_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    guna = models.CharField(default='', max_length=30, db_column='GUNA', verbose_name='GUNA', blank=True)
    devta = models.CharField(default='', max_length=30, db_column='Devta', verbose_name='Devta',blank=True)
    strength = models.CharField(default='',max_length=30, db_column='Strength', verbose_name='Strength',blank=True)
    planets = models.CharField(default='', max_length=30, db_column='PLANETS', verbose_name='PLANETS', blank=True)
    
    class Meta:
        verbose_name = '70. Table Name: Devta, Guna Arudha Strength Table (Table Code:68)'
        verbose_name_plural = '70. Table Name: Devta, Guna Arudha Strength Table (Table Code:68)'
    
class Pancha_prana_tattva_graha_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    panch_prana = models.CharField(default='', max_length=30, db_column='PANCH PRANA', verbose_name='PANCH PRANA', blank=True)
    tattva = models.CharField(default='', max_length=30, db_column='TATTVA', verbose_name='TATTVA', blank=True)
    planet = models.CharField(default='', max_length=30, db_column='PLANET', verbose_name='PLANET', blank=True)
    cheif_organs = models.CharField(default='', max_length=30, db_column='CHIEF ORGANS-ORGANS', verbose_name='CHIEF ORGANS-ORGANS', blank=True)
    controls = models.CharField(default='', max_length=30, db_column='CONTROLS', verbose_name='CONTROLS', blank=True)
    
    class Meta:
        verbose_name = '71. Table Name: Pancha Prana, Tattva & Graha Table (Table Code:69)'
        verbose_name_plural = '71. Table Name: Pancha Prana, Tattva & Graha Table (Table Code:69)'

class Sub_prana_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    panch_prana = models.CharField(default='', max_length=30, db_column='PANCH PRANA', verbose_name='PANCH PRANA', blank=True)
    tattva = models.CharField(default='', max_length=30, db_column='TATTVA', verbose_name='TATTVA', blank=True)
    sub_prana = models.CharField(default='', max_length=30, db_column='SUB-PRANA', verbose_name='SUB-PRANA', blank=True)
    planet =  models.CharField(default='', max_length=30, db_column='PLANET', verbose_name='PLANET', blank=True)
    controls = models.CharField(default='', max_length=30, db_column='CONTROLS', verbose_name='CONTROLS', blank=True)
    
    class Meta:
        verbose_name = '72. Table Name: Sub Prana Table (Table Code:70)'
        verbose_name_plural = '72. Table Name: Sub Prana Table (Table Code:70)'

class Rasi_graha_varna_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    varna = models.CharField(default='', max_length=30, db_column='VARNA', verbose_name='VARNA', blank=True)
    tattva = models.CharField(default='', max_length=30, db_column='TATTVA', verbose_name='TATTVA', blank=True)
    rasi = models.CharField(default='', max_length=30, db_column='RASI', verbose_name='RASI', blank=True)
    graha1 = models.CharField(default='', max_length=30, db_column='GRAHA-1', verbose_name='GRAHA-1', blank=True)
    graha2 = models.CharField(default='', max_length=30, db_column='GRAHA-2', verbose_name='GRAHA-2', blank=True)
    
    class Meta:
        verbose_name = '73. Table Name: Rasi Graha Varna Table (Table Code:71))'
        verbose_name_plural = '73. Table Name: Rasi Graha Varna Table (Table Code:71)'

class Loka_pala_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    houses_from_ascendant = models.CharField(default='', max_length=30, db_column='HOUSE FROM ASCENDANT', verbose_name='HOUSE FROM ASCENDANT', blank=True)
    direction = models.CharField(default='', max_length=30, db_column='DIRECTION', verbose_name='DIRECTION', blank=True)
    planets_as_lords = models.CharField(default='', max_length=30, db_column='PLANETS AS LORD', verbose_name='PLANETS AS LORD', blank=True)
    lord = models.CharField(default='', max_length=30, db_column='LORD', verbose_name='LORD', blank=True)
    
    class Meta:
        verbose_name = '74. Table Name: Loka Pala Table (Table Code:72)'
        verbose_name_plural = '74. Table Name: Loka Pala Table (Table Code:72)'

class Upa_graha_list_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    upagraha = models.CharField(default='', max_length=30, db_column='UPAGHRAHA', verbose_name='UPAGHRAHA', blank=True)
    
    class Meta:
        verbose_name = '75. Table Name: Upa-Graha List Table (Table Code:73)'
        verbose_name_plural = '75. Table Name: Upa-Graha List Table (Table Code:73)'

class Special_points_list_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    special_points = models.CharField(default='', max_length=30, db_column='SPECIAL POINT(S)', verbose_name='SPECIAL POINT(S)', blank=True)
    abbrev_english = models.CharField(default='', max_length=30, db_column='ABBREVATION IN ENGLISH', verbose_name='ABBREVATION IN ENGLISH', blank=True)
    abbrev_hindi = models.CharField(default='', max_length=30, db_column='ABBREVATION IN HINDI', verbose_name='ABBREVATION IN HINDI', blank=True)
    category = models.CharField(default='', max_length=30, db_column='CATEGORY', verbose_name='CATEGORY', blank=True)
    source = models.CharField(default='', max_length=30, db_column='SOURCE', verbose_name='SOURCE', blank=True)
    
    class Meta:
        verbose_name = '76. Table Name: Special Point List Table (Table Code:74)'
        verbose_name_plural = '76. Table Name: Special Point List Table (Table Code:74)'

class Initiation_chart_list_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_divisional_chart =  models.CharField(default='', max_length=30, db_column='NAME OF DIVISIONAL CHART', verbose_name='NAME OF DIVISIONAL CHART', blank=True)
    code = models.CharField(default='', max_length=30, db_column='CODE', verbose_name='CODE', blank=True)
    sub_category_divisional_chart = models.CharField(default='', max_length=30, db_column='SUB CATEGORY OF DIVISIONAL CHART', verbose_name='SUB CATEGORY OF DIVISIONAL CHART', blank=True)
    table_code = models.CharField(default='', max_length=30, db_column='TABLE CODE', verbose_name='TABLE CODE', blank=True)
    sub_Sub_category_Sub_category_divisional_chart = models.CharField(default='', max_length=30, db_column='SUB-SUB CATEGORY OF SUB CATEGORY OF DIVISIONAL CHART', verbose_name='SUB-SUB CATEGORY OF SUB CATEGORY OF DIVISIONAL CHART', blank=True)
    table_code = models.CharField(default='', max_length=30, db_column='TABLE CODE', verbose_name='TABLE CODE', blank=True)
    link_to = models.CharField(default='', max_length=30, db_column='LINK TO', verbose_name='LINK TO', blank=True)

    class Meta:
        verbose_name = '77. Table Name: Initiating Chart List Table (Table Code:75)'
        verbose_name_plural = '77. Table Name: Initiating Chart List Table (Table Code:75)'

class Name_of_main_topics_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_of_topics = models.CharField(default='', max_length=30, db_column='CODE', verbose_name='CODE', blank=True)
    abbrev_english = models.CharField(default='', max_length=30, db_column='ABBREVATION IN ENGLISH', verbose_name='ABBREVATION IN ENGLISH', blank=True)
    abbrev_hindi = models.CharField(default='', max_length=30, db_column='ABBREVATION IN HINDI', verbose_name='ABBREVATION IN HINDI', blank=True)
    no_Of_sub_topics = models.CharField(default='', max_length=30, db_column='NO OF SUB TOPICS', verbose_name='NO OF SUB TOPICS', blank=True)
    table_no_Of_Sub_topics = models.CharField(default='', max_length=30, db_column='TABLE No OF SUB-TOPICS', verbose_name='TABLE No OF SUB-TOPICS', blank=True)
    usage_in_model = models.CharField(default='', max_length=30, db_column='USAGE IN MODEL', verbose_name='USAGE IN MODEL', blank=True)

    class Meta:
        verbose_name = '78. Table Name: Name of Main Topics Table (Table Code:76)'
        verbose_name_plural = '78. Table Name: Name of Main Topics Table (Table Code:76)'

class Bhava_arudha_list_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_bhava_arudha = models.CharField(default='', max_length=30, db_column='NAME OF BHAVA ARUDHA', verbose_name='NAME OF BHAVA ARUDHA', blank=True)
    speial_name_arudha = models.CharField(default='', max_length=30, db_column='SPECIAL NAME OF ARUDHA', verbose_name='SPECIAL NAME OF ARUDHA', blank=True)
    abbrev1 = models.CharField(default='', max_length=30, db_column='ABBREVATION 1', verbose_name='ABBREVATION 1', blank=True)
    abbrev2 = models.CharField(default='', max_length=30, db_column='ABBREVATION 2', verbose_name='ABBREVATION 2', blank=True)
    link_func = models.CharField(default='', max_length=30, db_column='LINK TO FUNCTION', verbose_name='LINK TO FUNCTION', blank=True)

    class Meta:
        verbose_name = '79. Table Name: Bhava Arudha List Table (Table Code:77)'
        verbose_name_plural = '79. Table Name: Bhava Arudha List Table (Table Code:77)'

class Graha_arudha_list_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_graha = models.CharField(default='', max_length=30, db_column='NAME OF GRAHA', verbose_name='NAME OF GRAHA', blank=True)
    for_sign = models.CharField(default='', max_length=30, db_column='FOR SIGN', verbose_name='FOR SIGN', blank=True)
    abbrev = models.CharField(default='', max_length=30, db_column='ABBREVATION', verbose_name='ABBREVATION', blank=True)
    link_func = models.CharField(default='', max_length=30, db_column='LINK TO FUNCTION', verbose_name='LINK TO FUNCTION', blank=True)

    class Meta:
        verbose_name = '80. Table Name: Graha Arudha List Table (Table Code:78)'
        verbose_name_plural = '80. Table Name: Graha Arudha List Table (Table Code:78)'

class Nakshatra_Table_For_Vimshottari_Dasa_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    name_nakshatra = models.CharField(default='', max_length=30, db_column='NAME OF NAKSHATRA', verbose_name='NAME OF NAKSHATRA', blank=True)
    from_extent = models.CharField(default = '', max_length = 30, db_column='Extent From (SS-DD-MM-SS)', verbose_name='From (SS-DD-MM-SS)', blank=True)
    to_extent = models.CharField(default = '',max_length = 30, db_column='Extent To (SS-DD-MM-SS)', verbose_name='To (SS-DD-MM-SS)', blank=True)
    lord_nakshtra = models.CharField(default = '',max_length=30, db_column='LORD OF NAKSHTRA', verbose_name='LORD OF NAKSHTRA', blank=True)
    dasa_lord = models.CharField(default = '',max_length=30,db_column='DASA LORD',verbose_name='DASA LORD', blank=True)
    period_dasa = models.CharField(max_length=30, db_column='PERIOD OF DASA (YY-MM-DD-HH-MM-SS)', verbose_name='PERIOD OF DASA (YY-MM-DD-HH-MM-SS)', blank=True)

    class Meta:
        verbose_name = '81. Table Name: Nakshatra Table For Vimshottari Dasa Table (Table Code:79-A)'
        verbose_name_plural = '81. Table Name: Nakshatra Table For Vimshottari Dasa Table (Table Code:79-A)'

class Vimshottari_Dasa_Planetary_Sequence_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.',blank=False)
    starting_dasa_planet = models.CharField(default='', max_length=30, db_column='STARTING DASA OF PLANET', verbose_name='STARTING DASA OF PLANET', blank=True)
    vimshottary_dasa_planet1 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 1ST PLANET', verbose_name='VIMSHOTTARY DASA OF 1ST PLANET', blank=True)
    vimshottary_dasa_planet2 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 2ND PLANET', verbose_name='VIMSHOTTARY DASA OF 2ND PLANET', blank=True)
    vimshottary_dasa_planet3 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 3RD PLANET', verbose_name='VIMSHOTTARY DASA OF 3RD PLANET', blank=True)
    vimshottary_dasa_planet4 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 4TH PLANET', verbose_name='VIMSHOTTARY DASA OF 4TH PLANET', blank=True)
    vimshottary_dasa_planet5 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 5TH PLANET', verbose_name='VIMSHOTTARY DASA OF 5TH PLANET', blank=True)
    vimshottary_dasa_planet6 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 6TH PLANET', verbose_name='VIMSHOTTARY DASA OF 6TH PLANET', blank=True)
    vimshottary_dasa_planet7 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 7TH PLANET', verbose_name='VIMSHOTTARY DASA OF 7TH PLANET', blank=True)
    vimshottary_dasa_planet8 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 8TH PLANET', verbose_name='VIMSHOTTARY DASA OF 8TH PLANET', blank=True)
    vimshottary_dasa_planet9 = models.CharField(default='', max_length=30, db_column='VIMSHOTTARY DASA OF 9TH PLANET', verbose_name='VIMSHOTTARY DASA OF 9TH PLANET', blank=True)

    class Meta:
        verbose_name = '82. Table Name: Vimshottari Dasa Planetary Sequence Table (Table Code:79-B)'
        verbose_name_plural = '82. Table Name: Vimshottari Dasa Planetary Sequence Table (Table Code:79-B)'
 
class Time_Zone_Rest_Of_The_World_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    country_or_territory= models.CharField(default='',null=True, max_length=100, db_column='COUNTRY OR TERRITORY', verbose_name='COUNTRY OR TERRITORY')
    normal_time_zone_correction = models.CharField(default='',null=True, max_length=100, db_column='NORMAL TIME ZONE CORRECTION', verbose_name='NORMAL TIME ZONE CORRECTION' )
    dst_time_zone_correction = models.CharField(default='',null=True, max_length=100, db_column='DST TIME ZONE CORRECTION ', verbose_name='DST TIME ZONE CORRECTION ' )
    dst_time_start_date_time = models.CharField(default='', null=True,max_length=100, db_column='DST TIME START(DATE/TIME)', verbose_name='DST TIME START(DATE/TIME)' )
    dst_time_end_date_time = models.CharField(default='',null=True, max_length=100, db_column='DST TIME END(DATE/TIME)', verbose_name='DST TIME END(DATE/TIME)' )
    

    class Meta:
        verbose_name = '83. Table Name: Time Zone Rest Of The World Table (Table Code:80)'
        verbose_name_plural = '83. Table Name:Time Zone Rest Of The World Table (Table Code:80)'
 
class Us_Time_Zones_By_State_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    state_of_us_abbrevation = models.CharField(default='', max_length=100, db_column='STATE OF US (ABBREVAION )', verbose_name='STATE OF US (ABBREVAION )')
    larget_city = models.CharField(default='', max_length=100, db_column='LARGET CITY', verbose_name='LARGET CITY')
    us_normal_time_zone_correction = models.CharField(default='', max_length=100, db_column='NORMAL TIME ZONE CORRECTION', verbose_name='NORMAL TIME ZONE CORRECTION')
    us_dst_time_zone_correction = models.CharField(default='', max_length=100, db_column='DST TIME ZONE CORRECTION ', verbose_name='DST TIME ZONE CORRECTION ')
   
    class Meta:
        verbose_name = '84. Table Name: US Time Zones By State Table (Table Code:81)'
        verbose_name_plural = '84. Table Name:US Time Zones By State Table (Table Code:81)' 

class Russia_Time_Zones_By_City_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    city_or_regional_capital = models.CharField(default='', max_length=100, db_column='CITY OR REGIONAL CAPITAL', verbose_name='CITY OR REGIONAL CAPITAL')
    region = models.CharField(default='', max_length=100, db_column='REGION', verbose_name='REGION')
    russia_normal_time_zone_correction = models.CharField(default='', max_length=100, db_column='NORMAL TIME ZONE CORRECTION', verbose_name='NORMAL TIME ZONE CORRECTION')
    russia_dst_time_zone_correction_form_moscow_time = models.CharField(default='', max_length=100, db_column='DST TIME ZONE CORRECTION FROM MOSCOW TIME  ', verbose_name='DST TIME ZONE CORRECTION FROM MOSCOW TIME  ')
    
    

    class Meta:
        verbose_name = '85. Table Name: Russia Time Zones By City Table (Table Code:82)'
        verbose_name_plural = '85. Table Name:Russia Time Zones By City Table (Table Code:82)'         
      
class  Canada_Time_Zones_By_Province_Territory_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    province_territory = models.CharField(default='', max_length=100, db_column='PROVINCE/TERRITORY', verbose_name='PROVINCE/TERRITORY')
    larget_city = models.CharField(default='', max_length=100, db_column='LARGET CITY', verbose_name='LARGET CITY')
    canada_normal_time_zone_correction = models.CharField(default='', max_length=100, db_column='NORMAL TIME ZONE CORRECTION', verbose_name='NORMAL TIME ZONE CORRECTION')
    canada_dst_time_zone_correction_form_moscow_time = models.CharField(default='', max_length=100, db_column='DST TIME ZONE CORRECTION', verbose_name='DST TIME ZONE CORRECTION')
    
    

    class Meta:
        verbose_name = '86. Table Name: Canada Time Zones By Province Territory Table (Table Code:83)'
        verbose_name_plural = '86. Table Name: Canada Time Zones By Province territory Table (Table Code:83)'
        
class  Dst_Us_Correction_Timing_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    beginning_of_dst  = models.CharField(default='', max_length=100, db_column='BEGINNING OF DST ', verbose_name='BEGINNING OF DST ')
    beginning_time_of_dst = models.CharField(default='', max_length=100, db_column='BEGINNING TIME OF DST', verbose_name='BEGINNING TIME OF DST')
    end_of_dst = models.CharField(default='', max_length=100, db_column='END OF DST', verbose_name='END OF DST')
    ending_time_of_dst = models.CharField(default='', max_length=100, db_column='ENDING TIME OF DST', verbose_name='ENDING TIME OF DST')
    year_year = models.CharField(default='', max_length=50, db_column='YEAR-YEAR', verbose_name='YEAR-YEAR')
    

    class Meta:
        verbose_name = '87. Table Name: Dst Us Correction Time Table (Table Code:84)'
        verbose_name_plural = '87. Table Name:  Dst Us Correction Time Table (Table Code:84)'        
        
class  Dst_Russia_Correction_Timing_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    beginning_of_dst  = models.CharField(default='', max_length=100, db_column='BEGINNING OF DST ', verbose_name='BEGINNING OF DST ')
    beginning_time_of_dst = models.CharField(default='', max_length=100, db_column='BEGINNING TIME OF DST', verbose_name='BEGINNING TIME OF DST')
    end_of_dst = models.CharField(default='', max_length=100, db_column='END OF DST', verbose_name='END OF DST')
    ending_time_of_dst = models.CharField(default='', max_length=100, db_column='ENDING TIME OF DST', verbose_name='ENDING TIME OF DST')
    year_year = models.CharField(default='', max_length=50, db_column='YEAR-YEAR', verbose_name='YEAR-YEAR')
    

    class Meta:
        verbose_name = '88. Table Name: Dst Russia Correction Time Table (Table Code:85)'
        verbose_name_plural = '88. Table Name:  Dst Russia Correction Time Table (Table Code:85)'   
        
class  Dst_Canada_Correction_Timing_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    beginning_of_dst  = models.CharField(default='', max_length=100, db_column='BEGINNING OF DST ', verbose_name='BEGINNING OF DST ')
    beginning_time_of_dst = models.CharField(default='', max_length=100, db_column='BEGINNING TIME OF DST', verbose_name='BEGINNING TIME OF DST')
    end_of_dst = models.CharField(default='', max_length=100, db_column='END OF DST', verbose_name='END OF DST')
    ending_time_of_dst = models.CharField(default='', max_length=100, db_column='ENDING TIME OF DST', verbose_name='ENDING TIME OF DST')
    year_year = models.CharField(default='', max_length=50, db_column='YEAR-YEAR', verbose_name='YEAR-YEAR')
    

    class Meta:
        verbose_name = '89. Table Name: Dst Canada Correction Time Table (Table Code:89)'
        verbose_name_plural = '89. Table Name:  Dst Canada Correction Time Table (Table Code:89)' 
        
class Karana_Table(models.Model):
    s_no = models.IntegerField(default=0, verbose_name='Serial No.')
    name_of_karana = models.CharField(max_length=30, db_column='name_of_karana', blank=True)
    quality = models.CharField(max_length=30, db_column='quality', blank=True)
    lord = models.CharField(max_length=30, db_column='lord',blank=True)
    from_extent = models.CharField(default='', max_length=30, db_column='from_extent',  blank=True)
    to_extent = models.CharField(default='', max_length=30, db_column='to_extent', blank=True)

    class Meta:
        verbose_name = '90. Table Name: Name Of Karana Degree Table (Table Code:90)'
        verbose_name_plural = '90. Table Name: Name Of Karana Degree Table (Table Code:90)'        
        
class  Natal_First_Time_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    name  = models.CharField(default='', max_length=100, db_column='Name ', verbose_name='Name')
    gender = models.CharField(default='', max_length=100, db_column='gender', verbose_name='gender')
    father_name = models.CharField(default='', max_length=100, db_column='father name', verbose_name='father name')
    mother_name = models.CharField(default='', max_length=100, db_column='mother name', verbose_name='mother name')
    dob = models.CharField(default='', max_length=50, db_column='dob', verbose_name='dob')
    time  = models.CharField(default='', max_length=100, db_column='time ', verbose_name='time')
    location_search_input_lord = models.CharField(default='', max_length=200, db_column='location-search-input', verbose_name='location-search-input')
    timezone = models.CharField(default='', max_length=100, db_column='Time Zone', verbose_name='Time Zone')
    dst = models.CharField(default='', max_length=100, db_column='DST', verbose_name='DST')
    date1 = models.CharField(default='', max_length=100, db_column='BTR Date and Time', verbose_name='BTR Date and Time')
    currentaddress = models.CharField(default='', max_length=200, db_column='BTR Place', verbose_name='BTR Place')
    

    class Meta:
        verbose_name = '100. Table Name: Natal First Time Table (Table Code:100)'
        verbose_name_plural = '100. Table Name:  Natal First Time Table (Table Code:100)'
        
class  User_Registration_Table(models.Model):
   
    name  = models.CharField(default='', max_length=100, db_column='name ', verbose_name='name')
    city = models.CharField(default='', max_length=100, db_column='city', verbose_name='city')
    mobile_number = models.CharField(default='', max_length=100, db_column='mobile number', verbose_name='mobile_number')
    Email = models.CharField(default='', max_length=100, db_column='Email', verbose_name='Email')
    Password = models.CharField(default='', max_length=50, db_column='password', verbose_name='password')
    Forgot_password  = models.CharField(default='', max_length=100, db_column='forgot password ', verbose_name='forgot password')
    Reset_password = models.CharField(default='', max_length=200, db_column='reset password', verbose_name='reset password')
   
    class Meta:
        verbose_name = '100. Table Name: User_Registration_Table (Table Code:101)'
        verbose_name_plural = '100. Table Name:  User_Registration_Table (Table Code:101)'
        
        
class  User_Setting_Table(models.Model):
   
    graphtype = models.CharField(default='', max_length=100, db_column='graphtype', verbose_name='graphtype')
    language = models.CharField(default='', max_length=100, db_column='language', verbose_name='language')
    color  = models.CharField(default='', max_length=100, db_column='color', verbose_name='color')
    font_size= models.CharField(default='', max_length=200, db_column='font-size', verbose_name='font-size')
    bgColor  = models.CharField(default='', max_length=100, db_column='bgColor', verbose_name='bgColor')
    chartColor  = models.CharField(default='', max_length=100, db_column='chartColor', verbose_name='chartColor')
    glyphColor  = models.CharField(default='', max_length=100, db_column='glyphColor', verbose_name='glyphColor')
   
    class Meta:
        verbose_name = '100. Table Name: User_Setting_Table (Table Code:101)'
        verbose_name_plural = '100. Table Name:  User_Setting_Table (Table Code:101)'                   
       
class Ashtottari_Dasa_Table(models.Model):
    Nakshatra_name = models.CharField(max_length=100, db_column='Nakshatra Name', blank=True)
    from_extent = models.CharField(default='', max_length=30, db_column='from_extent',  blank=True)
    to_extent = models.CharField(default='', max_length=30, db_column='to_extent', blank=True)
    ending_point = models.CharField(max_length=30,verbose_name='ENDING POINT DASA', blank=True)
    lord_dasa = models.CharField(max_length=30,verbose_name='LORD OF DASA', blank=True)
    period_dasa = models.CharField(max_length=30, db_column='PERIOD OF DASA (YY-MM-DD)', verbose_name='PERIOD OF DASA (YY-MM-DD)', blank=True)
    class Meta:
        verbose_name = '101. Ashtottari  Deity (Devta) for REMEDIES Table'
        verbose_name_plural = '101. Ashtottari  Deity (Devta) for REMEDIES Table'        
        
                