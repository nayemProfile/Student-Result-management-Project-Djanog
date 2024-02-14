from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Custom_User)
admin.site.register(Student_Model)
admin.site.register(Subject_Model)
admin.site.register(Grade_Model)
admin.site.register(Result_Model)