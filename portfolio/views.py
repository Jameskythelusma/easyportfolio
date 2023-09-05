from django.shortcuts import render,redirect
from portfolio.forms import*
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm

def home(request):
    users = User.objects.order_by('-date_joined')
    context={
        'users':users,
    }

    return render(request,'index.html',context)



def signin(request):

    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=user_name,password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            print('li pa otantifye')
    form = UserForm()

    context={
            'form':form
        }

    return render(request,'signin.html',context)



def signup(request):
    if request.method == "POST":
         form =UserCreationForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect(signin)
    else:
        form = UserCreationForm()

    context={
            'form':form
        }
    return render(request,'signup.html',context)



def logout_user(request):
    print("Mwen ekzekite avan dekoneksyon an")
    logout(request)
    return redirect(home)



def userdetails(request,pk):

    user_det=User.objects.get(id=pk)
    projects=Project.objects.filter(user=user_det.id)
    context={
        'user_det':user_det,
        'projects':projects
    }
    return render(request,'userdetails.html',context)


def createproject(request):
    form = ProjectForm()
    context={
            'form':form
        }
    if request.user.is_authenticated:
        if request.method == 'POST':
             form = ProjectForm(data=request.POST,files=request.FILES)
             if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user  
                project.save()
                return redirect('home')  
    else:
        return redirect('signin')  
    return render(request,'createproject.html',context)
     



def projectdetails(request,pk):
    projects=Project.objects.filter(id=pk)

    context={
        'projects':projects
    }

    return render (request, 'projectdetails.html',context)

def deleteproject(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user == project.user:
        
        project.delete()
        return redirect('home') 


def profil(request):
    if request.user.profile is None:
        formprofil=profilform()

    user =request.user.profile
    form=profilform(instance=user)

    if request.method == 'POST':
        form=profilform(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('home') 

    context={

        'form':form,
        'formprofil':formprofil
    }
    return render(request,'profil.html',context)