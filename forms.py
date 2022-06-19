from django import forms
from django.forms import ModelForm
from .models import Event


#create Event form
class Event_form(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'telephone', 'adresa_o', 'email_obchodnika', 'client_name', 'date', 'panel', 'panel_vykon', 'zaruka_panel', 'zaruka_panel_vykon', 'baterie', 'typ_systemu', 'baterie_kapacita', 'baterie_vykon', 'baterie_zaruka', 'baterie_zaruka_vykon', 'invertor', 'invertor_vykon', 'invertor_zaruka', 'invertor_zaruka_vykon', 'optimizer', 'optimizer_vykon', 'optimizer_zaruka', 'optimizer_zaruka_vykon', 'cerpadlo', 'cerpadlo_vykon', 'cerpadlo_zaruka', 'cerpadlo_zaruka_vykon', 'zivotnost_bat_pan_inv_cer', 'year', 'many_years', 'foto_pan', 'foto_bat', 'naklady', 'dotace', 'celkova_cena_dph', 'celkove_uspory', 'kredit', 'vyrobce_pan', 'vyrobce_bat', 'vyrobce_str', 'vyrobce_opt', 'adress', 'email', 'phone', 'Poznamka')
      #  widgets = {
      #  'name': forms.TextInput(attrs={'class':'form-control'}),
      #  'client_name': forms.TextInput(attrs={'class':'form-control'}),
      #  'date': forms.TextInput(attrs={'class':'form-control'}),
       # 'panel': forms.TextInput(attrs={'class':'form-control'}),
       # 'baterie': forms.TextInput(attrs={'class':'form-select'}),
       # 'invertor': forms.TextInput(attrs={'class':'form-control'}),
       # 'year': forms.TextInput(attrs={'class':'form-control'}),
      #  'many_years': forms.TextInput(attrs={'class':'form-control'}),
       # 'panel_vykon': forms.TextInput(attrs={'class':'form-control'}),
       # 'baterie_kapacita': forms.TextInput(attrs={'class':'form-control'}),
       # 'naklady': forms.TextInput(attrs={'class':'form-control'}),
       # 'dotace': forms.TextInput(attrs={'class':'form-control'}),
       # 'celkova_cena_dph': forms.TextInput(attrs={'class':'form-control'}),
       # 'celkove_uspory': forms.TextInput(attrs={'class':'form-control'}),
        #'adress': forms.TextInput(attrs={'class':'form-control'}),
       # 'email': forms.TextInput(attrs={'class':'form-control'}),
        #'phone': forms.TextInput(attrs={'class':'form-control'}),
        #'description': forms.TextInput(attrs={'class':'form-control'}),


       # }
