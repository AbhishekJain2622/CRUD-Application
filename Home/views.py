from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Home.models import Entry

def home(request):
    return render(request,"Home/home.html")

def show(request):
    data = Entry.objects.all()
    return render(request,"Home/show.html",{'data':data})

def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        data3 = request.POST.get('data3', '')  # Provide a default value or handle if missing

        # Create and save the Entry object
        Entry(ID=ID, data1=data1, data2=data2, data3=data3).save()
        
        msg = "Data Stored Successfully"
        return render(request, "Home/home.html", {'msg': msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID = request.GET['id']
    data1 = data2 = "Not Available"
    for data in Entry.objects.filter(ID=ID):
        data1 = data.data1
        data2 = data.data2
    return render(request,"Home/edit.html",{'ID':ID,'data1':data1,'data2':data2})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry.objects.filter(ID=ID).update(data1=data1,data2=data2)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")