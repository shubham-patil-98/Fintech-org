from django.contrib import admin
from .models import Complaint, Detail, recharge
# Register your models here.
admin.site.register(Complaint)
admin.site.register(Detail)
admin.site.register(recharge)