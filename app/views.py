from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Contact, Professional
from .forms import Contact_form, Profile_update_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import DetailView


@login_required(login_url='index')
def home_view(request):
    return render(request, 'home.html')



def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully signed in")
            return redirect('profile')

        else:
            messages.error(request, "Invalid Credentials")
            return redirect('index')

    return render(request, 'registration/login.html')





def register_view(request):
    if request.method == "POST":
        username=request.POST['username'].lower()
        email=request.POST['email'].lower()
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>20:
            messages.warning(request,"Username is too large")
            return redirect('index')

        if len(username)==0:
            messages.warning(request,"Please fill the Username")
            return redirect('index')


        if len(fname)==0:
            messages.warning(request,"Please fill the First Name")
            return redirect('index')

        if len(fname)>20:
            messages.warning(request,"Please keep First Name under 20 characters.")
            return redirect('index')

        if len(lname)==0:
            messages.warning(request,"Please fill the Last Name")
            return redirect('index')

        if len(lname)>20:
            messages.warning(request,"Please keep Last Name under 20 characters.")
            return redirect('index')

        if len(email)==0:
            messages.warning(request,"Please fill the email")
            return redirect('index')

        if len(email)>80:
            messages.warning(request,"Please keep email address shorter")
            return redirect('index')

        if len(pass1)>100:
            messages.warning(request,"Please keep password shorter to remember.")
            return redirect('index')

        if len(pass1)<5:
            messages.warning(request,"Password too short")
            return redirect('index')


        if len(pass1)==0:
            messages.warning(request,"Please fill password.")
            return redirect('index')

        if not username.isalnum():
            messages.warning(request, "Username consists of alphabet and numbers only")
            
        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('index')


        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists or taken.")
            return redirect('index')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken, please try something else.")
            return redirect('index')
            
        
        
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('index')

    else:
        return HttpResponse("404 - Not found")





def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    form = Contact_form(request.POST or None)
    if request.method =='POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            
            form = Contact_form()

    return render(request, 'contact.html', {'form':form})


@login_required(login_url='index')
def subscription_view(request):

    return render(request, 'subscription.html')




@login_required(login_url='index')
def profile_view(request):

    
    return render(request, 'profile.html')


import os
@login_required(login_url='index')
def profile_update_view(request):

    if request.method =='POST':
        profile_form = Profile_update_form(request.POST, request.FILES, instance=request.user.professional)
        if profile_form.is_valid():

            profile_form.save()
            return redirect('profile')

    else:
        profile_form = Profile_update_form(instance=request.user.professional)

    context = {
        'profile_form':profile_form
    }
    
    return render(request, 'edit_profile.html', context)




@login_required(login_url='index')
def logout_view(request):
    
    logout(request)
    messages.success(request, "Successfully signed out")
    return redirect('index')


def search_view(request):
    query = request.GET['query']
    
    if len(query)>10:
        messages.warning(request, "Please type correct username")
        return redirect('profile')
        
    else:       
        query_filter  = Professional.objects.filter(user__username__icontains=query).order_by()

    if query_filter.count()==0:
        messages.warning(request, "Please type correct username")
        return redirect('profile')
        
    # print(query)

    context = {
            'query':query,
            'query_filter':query_filter,
        }

    return render(request, 'search.html',context)
    


class Profile_search_view(DetailView):
    model = Professional
    template_name = 'profile_search.html'
    context_object_name = 'query_result'
    pk_url_kwargs = 'pk'