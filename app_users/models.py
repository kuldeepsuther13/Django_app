from django.db import models

# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    contact_details = models.CharField(max_length=250)

class Tests(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)

class Sample(models.Model):
    id = models.AutoField(primary_key=True)
    # patient = models.ForeignKey(Patient1, on_delete=models.CASCADE)
    # test = models.ForeignKey(Tests1, on_delete=models.CASCADE)
    sample_type= models.CharField(max_length=150)
    collection_date = models.DateField()

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    # patient = models.ForeignKey(Patient1, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=150,null=True, blank=True)
    specialization= models.CharField(max_length=150)
    contact_details = models.CharField(max_length=250)

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    # patient = models.ForeignKey(Patient1, on_delete=models.CASCADE)
    # test = models.ForeignKey(Tests1, on_delete=models.CASCADE)
    result_value = models.CharField(max_length=150)
    unit = models.CharField(max_length=150)
    interpretation = models.CharField(max_length=100)
    result_date = models.DateField()


