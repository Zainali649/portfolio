from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request,'projects.html')


def contact ( request ) :
    if request.method == "POST" :
        name = request.POST.get ( 'name' , '' )
        email = request.POST.get ( 'email' , '' )
        phone = request.POST.get ( 'phone' , '' )
        desc = request.POST.get ( 'desc' , '' )
        contact = Contact ( name = name , email = email , phone = phone , desc = desc )
        contact.save ( )
        print ( "Data has been save successfully!!" )

    return render ( request , 'contact.html' )
