from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from . models import *
from . forms import *
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#from . filters import BabyFilter
# Create your views here.

#login and register views
def registerpage(request):
    form =CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request, 'Account was created for'+ user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'DaystarApp/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
          

    context = {}    
    return render(request, 'DaystarApp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')










@login_required(login_url='login')
def home(request):
    return render(request, 'DaystarApp/home.html')

def index(request):
    babies = Baby.objects.all()
    return render(request, 'DaystarApp/index.html', {'babies':babies})


# def view_baby(request,id):
#     babies = Baby.objects.get(pk=id)
#     return HttpResponseRedirect(reverse('index'))


def view_baby(request, id):
   baby = Baby.objects.get(pk=id)
   return render(request, 'DaystarApp/view_baby.html', {'baby': baby})

def add(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            new_B_name = form.cleaned_data['B_name']
            new_age = form.cleaned_data['age']
            new_Gender = form.cleaned_data['Gender']
            new_fathers_name = form.cleaned_data['fathers_name']
            new_mothers_name = form.cleaned_data['mothers_name']
            new_location = form.cleaned_data['location']
            new_mothers_phone = form.cleaned_data['mothers_phone']
            new_fathers_phone = form.cleaned_data['fathers_phone']
            new_brought_by = form.cleaned_data['brought_by']
            new_timeIn = form.cleaned_data['timeIn']
            new_timeOut = form.cleaned_data['timeOut']
            new_baby_number = form.cleaned_data['baby_number']
            new_c_stay = form.cleaned_data['c_stay']
            new_assign = form.cleaned_data['assign']

            new_baby = Baby (
                B_name = new_B_name,
                age = new_age,
                Gender = new_Gender,
                fathers_name = new_fathers_name,
                mothers_name = new_mothers_name,
                location = new_location,
                mothers_phone= new_mothers_phone,
                fathers_phone = new_fathers_phone,
                brought_by = new_brought_by,
                timeIn = new_timeIn,
                timeOut = new_timeOut,
                baby_number = new_baby_number,
                c_stay = new_c_stay,
                assign = new_assign,
            )
            new_baby.save()
            return render(request, 'DaystarApp/add.html', {
                'form':BabyForm(),
                'success': True
            })
    else:
        form = BabyForm()
    return render(request, 'DaystarApp/add.html', {'form': BabyForm(),})


def edit(request,id):
    if request.method =='POST':
     baby = Baby.objects.get(pk=id)
     form = BabyForm(request.POST, instance=baby)
     if form.is_valid():
        form.save()
        return render(request, 'DaystarApp/edit.html', {
            'form':form,
            'success':True
            })
    else:
        baby = Baby.objects.get(pk=id)
        form = BabyForm(instance=baby)
    return render(request, 'DaystarApp/edit.html',{'form':form})
      
# def delete(request, id):
#     if request.method == 'POST':
#         baby = Baby.objects.get(pk=id)
#         baby.delete()
#         return HttpResponseRedirect(reverse('index'))



def delete(request, id):
    if request.method == 'POST':
        try:
            baby = Baby.objects.get(pk=id)
            baby.delete()
            return HttpResponseRedirect(reverse('index'))
        except ObjectDoesNotExist:
            # Handle the case where the Baby object does not exist
            # You might want to render an error page or redirect to another URL
            pass

#sitter views
# def allsitters(request):
#     allsitters = Sitter.objects.all()
#     return render(request, 'DaystarApp/allsitters.html', {'allsitters': allsitters})




def view_sitter(request, id):
   sitter = Sitter.objects.get(pk=id)
   return render(request, 'DaystarApp/view_sitter.html', {'sitter': sitter})


   
    

def editsitter(request,id):
    if request.method =='POST':
     sitter = Sitter.objects.get(pk=id)
     form = SittersForm(request.POST, instance=sitter)
     if form.is_valid():
        form.save()
        return render(request, 'DaystarApp/editsitter.html', {
            'form':form,
            'success':True
            })
    else:
        sitter = Sitter.objects.get(pk=id)
        form = SittersForm(instance=sitter)
    return render(request, 'DaystarApp/editsitter.html',{'form':form})

def deletesitter(request, id):
    if request.method == 'POST':
        try:
            sitter = Sitter.objects.get(pk=id)
            sitter.delete()
            return HttpResponseRedirect(reverse('index'))
        except ObjectDoesNotExist:
            # Handle the case where the Baby object does not exist
            # You might want to render an error page or redirect to another URL
         pass
def addsitter(request):
    if request.method == 'POST':
        form = SittersForm(request.POST)
        if form.is_valid():
            new_S_name = form.cleaned_data['S_name']
            new_Gender = form.cleaned_data['Gender']
            new_recommenders_name = form.cleaned_data['recommenders_name']
            new_next_of_kin = form.cleaned_data['next_of_kin']
            new_location = form.cleaned_data['location']
            new_contact = form.cleaned_data['contact']  # Corrected field name
            new_religion = form.cleaned_data['religion']
            new_NIN = form.cleaned_data['NIN']
            new_education_level = form.cleaned_data['education_level']
            new_sitter_number = form.cleaned_data['sitter_number']
          
            new_sitter = Sitter(
                S_name=new_S_name,
                Gender=new_Gender,
                recommenders_name=new_recommenders_name,
                next_of_kin=new_next_of_kin,
                location=new_location,
                NIN=new_NIN,
                education_level=new_education_level,
                religion=new_religion,
                contact=new_contact,
                sitter_number=new_sitter_number,
            )
            
            new_sitter.save()
            return render(request, 'DaystarApp/addsitter.html', { 
                'form': SittersForm(),
                'success': True
            })
    else:
        form = SittersForm()
    return render(request, 'DaystarApp/addsitter.html', {
        'form': SittersForm(),
    })















@login_required(login_url='login')
def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page
    else:
        form = PaymentForm()
    return render(request, 'DaystarApp/payments.html', {'form': form})

def allpayments(request):
    allpayments = Payment.objects.all()
    return render(request, 'DaystarApp/paymentlist.html', {'allpayments': allpayments})
