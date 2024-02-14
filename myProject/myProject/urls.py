from myApp.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signUp, name='signUp'),
    path('loginPage/', loginPage, name='loginPage'),
    path('home/', homePage, name='homePage'),
    path('studentAdd/', studentAdd, name='studentAdd'),
    
    path('studentDelete/<str:id>', studentDelete, name='studentDelete'),
    path('studentUpdate/<str:id>', studentUpdate, name='studentUpdate'),
    
    path('subjectAdd/', subjectAdd, name='subjectAdd'),
    path('subjectDelete/<str:id>', subjectDelete, name='subjectDelete'),
    path('subjectUpdate/<str:id>', subjectUpdate, name='subjectUpdate'),
    
    
    path('gradeAdd/', gradeAdd, name='gradeAdd'),
    path('gradeDelete/<str:id>', gradeDelete, name='gradeDelete'),
    path('gradeUpdate/<str:id>', gradeUpdate, name='gradeUpdate'),
    path('giveMark/<str:id>', giveMark, name='giveMark'),
    
    
    path('resultView/<str:id>', resultView, name='resultView'),
]
