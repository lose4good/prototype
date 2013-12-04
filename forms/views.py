# Create your views here.
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.forms import RegistrationForm, LoginForm
from accounts.models import WeightLoser



def WeightloserRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/') 
    
    if request.method=='POST':  
        form=RegistrationForm(request.POST)
        if form.is_valid():  
            emailtemp=str(form.cleaned_data['emailId'])
            name=emailtemp.split("@")[0]
            user = User.objects.create_user(username=name, email = form.cleaned_data['emailId'], password = form.cleaned_data['password'])
            user.save()
            weightloser = WeightLoser(user=user, fname=form.cleaned_data['fname'],lname=form.cleaned_data['lname'], dob=form.cleaned_data['dob'],gender=form.cleaned_data['gender'],emailId=form.cleaned_data['emailId'],currentWeight=form.cleaned_data['currentWeight'])
            
            weightloser.save()
            userwloser = authenticate(username=name, password=form.cleaned_data['password'])
            login(request, userwloser)
            print "user is "+str(request.user.is_authenticated())
            return HttpResponseRedirect('/profile/')
        else:  #display the form when not valid
            return render_to_response('RegisterPage.html',{'form':form}, context_instance=RequestContext(request))
    else:    #Showing the form
        '''user is not submitting the form, show them a blank registration form'''
        form=RegistrationForm()
        context={'form':form}
        return render_to_response('RegisterPage.html',context, context_instance=RequestContext(request))


@login_required
def Profile(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/')
        weightloser = request.user.get_profile
        context = {'weightloser': weightloser}
        return render_to_response('HomePage.html', context, context_instance=RequestContext(request))
        
    
def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        weightloser = authenticate(username=username, password=password)
                        if weightloser is not None:
                                login(request, weightloser)
                                return HttpResponseRedirect('/profile/')
                        else:
                                return render_to_response('LoginPage.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('LoginPage.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('loginPage.html', context, context_instance=RequestContext(request))
@login_required
def LogoutRequest(request):
        logout(request)
        return render_to_response('LogoutPage.html','','')
       
@login_required
def DisplayProfile(request):
        context={}
        return render_to_response('HomePage.html',context,'')


    #Build the html then the hook to this registration