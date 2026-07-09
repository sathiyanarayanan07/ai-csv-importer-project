from django.db import models

# Create your models here.

class Upload(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
class CRMLead(models.Model):


    STATUS_CHOICES = [
        ("GOOD_LEAD_FOLLOW_UP", "GOOD_LEAD_FOLLOW_UP"),
        ("DID_NOT_CONNECT", "DID_NOT_CONNECT"),
        ("BAD_LEAD", "BAD_LEAD"),
        ("SALE_DONE", "SALE_DONE"),
    ]

    DATA_SOURCE_CHOICES = [
        ("leads_on_demand", "leads_on_demand"),
        ("meridian_tower", "meridian_tower"),
        ("eden_park", "eden_park"),
        ("varah_swamy", "varah_swamy"),
        ("sarjapur_plots", "sarjapur_plots"),
    ]

    upload =models.ForeignKey(Upload,on_delete=models.CASCADE,related_name="leads")
    created_at = models.DateTimeField(null=True,blank=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    country_code = models.CharField(max_length=10, blank=True)
    mobile_without_country_code = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=255,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    lead_owner = models.EmailField(blank=True)
    crm_status = models.CharField(max_length=30, choices=STATUS_CHOICES, blank=True)
    crm_note = models.TextField(blank=True)
    data_source = models.CharField(max_length=50,choices=DATA_SOURCE_CHOICES,blank=True)
    possession_time = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    imported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or " Unknown Lead"