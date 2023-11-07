from django import forms
from .models import Setting

class settingForm(forms.ModelForm):
    class Meta:
         model = Setting 
         fields = ('setting','description','sh_desc','lastuser')    ##ถ้าไม่เอาall สามารถกำหนดตามชื่อได้ ('fullname','a','b')
         labels = {
              'setting':'รหัสการฝัง',
              'description': 'คำอธิบายการฝัง',
              'sh_desc' : 'ตัวย่อการฝัง',
               'lastuser' : 'ชื่อผู้ใช้' 

         }

    def __init__(self, *args, **kwargs):
         super(settingForm,self).__init__(*args,**kwargs)
         self.fields['setting'].required = True
         self.fields['description'].required = True
         self.fields['sh_desc'].required = False