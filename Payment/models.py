from django.db import models

# Create your models here.
class Complaint(models.Model):
    name=models.CharField(max_length=1000)
    complaint_id=models.IntegerField(primary_key=True,unique=True)
    complaints=models.CharField(max_length=500)

    def new(self):
        return self.complaint_id

class Detail(models.Model):
    details=models.ForeignKey(Complaint,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.details

class recharge(models.Model):
    select_choice=(
        ('completed','COMPLETED'),
        ('pending','PENDING')
    )

    status=models.CharField(choices=select_choice,max_length=1000)
    id_no=models.IntegerField()

    def __str__(self):
        return self.status

