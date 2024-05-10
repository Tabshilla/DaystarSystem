from django.db import models

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name


    

class Sitter(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    RELIGION_CHOICES = (
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Other', 'Other'),
    )
    EDUCATION_LEVEL_CHOICES = (
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('University', 'University'),
    )
    S_name = models.CharField(max_length=200,null=True,blank=True)
    Gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    location = models.CharField(max_length=200, default="Kabalaga")
    next_of_kin = models.CharField(max_length=200)
    recommenders_name = models.CharField(max_length=200)
    religion = models.CharField(max_length=100, choices=RELIGION_CHOICES, blank=True)
    NIN = models.CharField(max_length=30, unique=True)
    education_level = models.CharField(max_length=200, choices=EDUCATION_LEVEL_CHOICES)
    sitter_number = models.CharField(max_length=200, unique=True)
    contact = models.IntegerField(null= True)
    def __str__(self):
        return self.S_name
    
class Baby(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
    B_name = models.CharField(max_length=200,null=True,blank=True)
    c_stay = models.ForeignKey(Categorystay,on_delete = models.CASCADE,null=True,blank = True)
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField(null=True,blank=True,default=0)
    fathers_name = models.CharField(max_length= 255, null=True,blank=True)
    mothers_name = models.CharField(max_length= 255,null=True,blank=True)
    location = models.CharField(max_length= 255)
    mothers_phone = models.IntegerField(null= True)
    fathers_phone = models.IntegerField(null= True)
    brought_by = models.CharField(max_length=200, null=True, blank=True)
    timeIn = models.DateTimeField(null=True,blank=True)
    timeOut = models.DateTimeField(null=True,blank=True)
    baby_number = models.PositiveIntegerField()
    assign = models.ForeignKey(Sitter,on_delete=models.CASCADE, null= True, blank=True)
    

    def __str__(self):
        return self.B_name
    
class Payment(models.Model):
    S_name = models.ForeignKey(Sitter, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=0, help_text='Amount in Ugandan Shillings (UGX)')

    # Define constants for payment types
    HALF_DAY = 'half_day'
    FULL_DAY = 'full_day'
    PAYMENT_CHOICES = [
        (HALF_DAY, 'Half Day Payment (10,000 UGX)'),
        (FULL_DAY, 'Full Day Payment (15,000 UGX)'),
    ]
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    date_of_payment = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.S_name} - {self.get_payment_type_display()}"

    
