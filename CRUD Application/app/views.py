from django.shortcuts import render, redirect
#importing all classes from models.py to store InsertData into model 
from .models import *
# Create your views here.
""" Here we need to create url for every function(or say view)"""

def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):
    # Data come from HTML to View
    """ Here this fname,lname etc.. in sq. brackets is the name which is given to tags in insert.html"""
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    contact = request.POST.get('contact')

    # Creating Object of Model Class
    # Inserting Data into Table

    """ Here Blue variables are the name of variables from models.py and =variable from above InsertData fn"""
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,    
                                        Email=email,Contact=contact)

    # After Insert render on Show.html
    # Render means only calling the page
    """ Redirect a library in django which redirects to another view through view
        i.e. redirect reponses to another view"""  
    #return render(request,"app/show.html")
    # This 'showpage' is the name of url of ShowPage function
    # After Insert render on Showpage view
    return redirect('showpage')

def ShowPage(request):
    # Select * from tablename
    #For fetching all data of the table
    all_data = Student.objects.all()
    #all data is passed if the form of dict with the help of key(context)
    return render(request,"app/show.html",{'key1':all_data})

#Edit Page View
def EditPage(request, pk):
    #Fetching the data of particular ID
    get_data = Student.objects.get(id=pk)
    return render(request, "app/edit.html",{'key2':get_data})

#Update Data View
def UpdateData(request, pk):
    udata = Student.objects.get(id=pk)
    #Ftrstname from database fname from edit.html
    udata.Firstname = request.POST.get('fname')
    udata.Lastname = request.POST.get('lname')
    udata.Email = request.POST.get('email')
    udata.Contact = request.POST.get('contact')
    #Query for update
    udata.save()
    # Render to ShowPage
    return redirect('showpage')

#Delete Data View
def DeleteData(request, pk):
    ddata = Student.objects.get(id=pk)
    #Query for Delete
    ddata.delete() 
    return redirect('showpage')
