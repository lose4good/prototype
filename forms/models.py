from django.db import models
from django.contrib.auth.models import User
# Create your models here.

     

    
class WeightLoser(models.Model):
    user = models.OneToOneField(User) 
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    dob = models.DateField(null=True,blank=True)
    gender = models.BooleanField(blank=True)
    #userId=models.CharField(max_length=15)
    emailId=models.EmailField()
    weightloserId=models.AutoField(primary_key=True)
    currentWeight=models.FloatField()
    
    def __unicode__(self):
        return u'%s %s'%(self.fname,self.lname)
    
class FinancialOfficer(models.Model):
    name=models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    emailId=models.EmailField()
    
class Charity(models.Model):
    name=models.CharField(max_length=100)
    emailId=models.EmailField()
    charityId=models.AutoField(primary_key=True)
    def __unicode__(self):
        return u'%s'%(self.name)
    
    #def getCharities(self):
    #    Charity_choices=()
    #    charityobjectlist = Charity.objects.all()
        
    #    for charity in charityobjectlist:
                #charity.name
                #charitylist.append(charity.name)
                #replace with charity id
    #            Charity_choices=Charity_choices+((charity.charityId,charity.name),)
    #    return Charity_choices
    
class Sponsor(models.Model):
    sponsorId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=80)
    emailId=models.EmailField()
    
    
    