from django.db import models
from datetime import datetime, date

class Event(models.Model):



    PANELS=(
        ('AS', 'Amerisolar'),
        ('JAS', 'JA Solar'),
        ('EXE', 'EXE SOLAR')
    )
    BATERY=(
        ('FoxESS', 'FoxESS'),
        ('BYD', 'BYD Battery-Box'),
        ('EXE SOLAR', 'EXE SOLAR')
    )
    INVERTOR=(
        ('GoodWe', 'GoodWe'),
        ('FoxESS', 'FoxESS'),
    )
    OPTIMIZER=(
        ('EXE SOLAR', 'EXE SOLAR'), #todo
        ('FoxESS', 'FoxESS'),

    )
    CERPADLO =(
        ('EXE SOLAR', 'EXE SOLAR'), #todo
 # Maybe there will be more
    )
    yearss=(
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('25', '25'),
        ('30', '30'),

    )
    #name and surnames
    name = models.CharField('Jmeno a Prijmeni zamestance', max_length=30)
    telephone = models.CharField('Telefonni cislo(zamestanec)', max_length=30)
    client_name = models.CharField('Jmeno a prijmeni klientu ', max_length=30)
    adresa_o = models.CharField('Adresa Obchodnika', max_length=60, null=False, default=0)
    date = models.DateField('Date', null=False, default=date.today())
    #panels
    panel = models.CharField(max_length=30, choices = PANELS, null=False)
    panel_vykon = models.IntegerField('Výkon Panely',  default=0, null=False)
    zaruka_panel = models.CharField(max_length=30, choices=yearss, null=False)
    zaruka_panel_vykon = models.CharField(max_length=30, choices=yearss, null=False)

    #baterie
    baterie =models.CharField(max_length=30, choices = BATERY, null=True, blank=True)
    typ_systemu = models.CharField(max_length=30,null=True, blank=True)
    baterie_kapacita = models.IntegerField('Kapacita Baterie',  default=0, null=True)
    baterie_vykon = models.IntegerField('Vykon Baterii', default=0, null=True)
    baterie_zaruka = models.CharField(max_length=30, choices=yearss, null=False)
    baterie_zaruka_vykon = models.CharField(max_length=30, choices=yearss, null=False)
    #Invertor
    invertor =models.CharField(max_length=30, choices = INVERTOR, null=False)
    invertor_vykon = models.IntegerField('Vykon Invertoru', null=False)
    invertor_zaruka = models.CharField(max_length=30, choices=yearss, null=False)
    invertor_zaruka_vykon = models.CharField(max_length=30, choices=yearss, null=False)


    optimizer = models.CharField(max_length=30, choices = OPTIMIZER, null = False)
    optimizer_vykon = models.IntegerField('Vykon Iptimizeru', null=False)
    optimizer_zaruka = models.CharField(max_length=30, choices=yearss, null=False)
    optimizer_zaruka_vykon = models.CharField(max_length=30, choices=yearss, null=False)



#cerpadlo
    cerpadlo = models.CharField(max_length=30, choices= CERPADLO, null=False, blank=True)
    cerpadlo_vykon = models.IntegerField('Vykon cerpadla', null=False)
    cerpadlo_zaruka = models.CharField(max_length=30, choices=yearss, null=False)
    cerpadlo_zaruka_vykon = models.CharField(max_length=30, choices=yearss, null=False)

    #zivotnost
    zivotnost_bat_pan_inv_cer = models.IntegerField( null=False)










    year = models.IntegerField('Roční spotřeba elektřiny',  default=0, null=False)
    many_years = models.IntegerField('Projekce nákladů na energii(25let)',  default=0, null=False)
    naklady = models.IntegerField('Náklady na instalace', default=0, null=False)
    dotace = models.IntegerField('Výše státní dotace', default=0, null=False)
    celkova_cena_dph = models.PositiveIntegerField("Celkova Cena vcetne DPH", default=0, null=False)
    celkove_uspory = models.PositiveIntegerField("Celkova výše úspory", default=0, null=False)
    adress = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=30, null=False)
    email_obchodnika = models.EmailField(max_length=30, null=False)
    phone = models.CharField(max_length=30, null=False)
    kredit = models.IntegerField('Platba po dobu 10let', default=0, null=False)
    vyrobce_pan=models.IntegerField('VÝROBCE A MODEL PANELU', default=0, null=False)
    vyrobce_bat=models.IntegerField('VÝROBCE A MODEL BATERIE', default=0, null=False)
    vyrobce_str=models.IntegerField('VÝROBCE A MODEL STŘÍDAČE', default=0, null=False)
    vyrobce_opt=models.IntegerField('VÝROBCE A MODEL OPTIMALIZÁTORU', default=0, null=False)
    foto_pan=models.IntegerField('Fotovoltaicka elekrarna o vykonu ', default=0, null=False)
    foto_bat=models.IntegerField('Domaci baterieove ulziste o Kapacite ', default=0, null=False)
    Poznamka=models.TextField('', blank=True)

    def __str__(self):
        return self.name + ' ' + self.client_name

