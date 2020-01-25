from django.shortcuts import render,redirect
import uuid
from .form import FileUploadForm
from .models import FileUpload
from django.http import HttpResponse
from user_registration.models import Registration,Friends

#a=uuid.uuid4()
def index(request):
    # #request the user to upload the Songs
    # if request.method=='POST':
    #     form =FileUploadForm(request.POST,request.FILES) #request the files
    #     if form.is_valid():
    #         form.save()
    #         form.clean()
    #         return redirect('songs:test')
    # else:
    #     form= FileUploadForm()
    # if request.session.haskey('username'):
    a=Registration.register.get(username=request.session['username'])
    return render(request,'songs/homepage.html',{'obj':'home','username':a.username,'profile':bool(a.profile_pic),'profilepc':a.profile_pic})

# music search
def searchMusic(request):
    return render(request,'songs/homepage.html',{'obj':'searched'})
def profile(request):
    return render(request,'songs/userprofile.html',{'username': request.session['username']})
