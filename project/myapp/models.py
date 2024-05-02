from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username + ' (' + self.specialization + ')'

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username + ' (' + str(self.date_of_birth) + ')'


class MedicalData(models.Model):
    condition=models.CharField(max_length=100)
    date_of_diag=models.DateField(auto_now=False,auto_now_add=False)
    treatments=models.CharField(max_length=200)
    add_info=models.TextField()
    report=models.FileField(upload_to='doc',blank=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return self.condition + ' (' + self.treatments + ')' + ' (' + self.add_info + ')'