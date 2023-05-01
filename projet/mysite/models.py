from django.db import models



# Create your models here.
class Donneur(models.Model):
    nom = models.CharField(max_length=20, verbose_name='الاسم')
    tel = models.IntegerField(verbose_name='الهاتف')
    password = models.CharField(max_length=10, verbose_name='كلمةالسر')
    groupeSanguin = models.CharField(max_length=10,  choices=(('لا اعرف', 'لا اعرف'),
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('A+', 'A+')), verbose_name='زمرةالدم')
    date_Dernier_Don = models.DateField(verbose_name='تاريخ اخر تبرع')
    gender = models.CharField(max_length=10, choices=((' 1', 'ذكر'), ('2', 'أنثى')), verbose_name='الجنس')
    wilaya = models.CharField(max_length=30, choices=((' الحوض الشرقي', 'الحوض الشرقي'),
        ('الحوض الغربي', 'الحوض الغربي'),
        ('لعصابة', 'لعصابة'),
        ('كوركول', 'كوركول'),
        ('لبراكنة', 'لبراكنة'),
        ('ترارزة', 'ترارزة'),
        ('أدرار', 'أدرار'),
        ('انواذيبو', 'انواذيبو'),
        ('تكانت', 'تكانت'),
        ('كيديماغا', 'كيديماغا'),
        ('تيرس زمور', 'تيرس زمور'),
        ('إنشيري', 'إنشيري'),
        ('انواكشوط', 'انواكشوط')), verbose_name='الولاية')
    def __str__(self):
        return self.nom
    
    class Meta:
       verbose_name = 'متبرع'
       verbose_name_plural = 'المتبرعون'
    



class Hopital(models.Model):
    nom = models.CharField(max_length=20, verbose_name='الاسم')
    password = models.CharField(max_length=10, verbose_name='كلمة السر')
    def __str__(self):
        return self.nom
    
    class Meta:
       verbose_name = 'مستشفى'
       verbose_name_plural = 'المستشفيات'
    



class Rendez_vous(models.Model):
    donneur_id = models.ForeignKey(Donneur, on_delete=models.CASCADE, verbose_name='المتبرع')
    date = models.DateField(verbose_name='التاريخ')
    time = models.TimeField(verbose_name='الوقت')
    lieu = models.CharField(max_length=15, verbose_name='المكان')
    def __str__(self):
        #return f"{self.date} - ({self.donneur_id.nom})"
        return f"{self.donneur_id.nom}"
    
    class Meta:
       verbose_name = 'ميعاد'
       verbose_name_plural = 'المواعيد'
    

class Login(models.Model):
    username = models.CharField(max_length=20, verbose_name=' اسم المستخدم')
    password = models.CharField(max_length=20, verbose_name=' كلمة السر')
    def __str__(self):
        return self.username
    
    class Meta:
       verbose_name = 'اتصال'
       verbose_name_plural = 'اتصالات'


class GroupSanguin(models.Model):
    name = models.CharField(max_length=10, verbose_name='الاسم',  choices=(('o-', 'o-'),
        ('o+', 'o+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('A+', 'A+')))
    def __str__(self):
        return self.name
    
    class Meta:
       verbose_name = 'زمرة الدم'
       verbose_name_plural = 'زمر الدم'






