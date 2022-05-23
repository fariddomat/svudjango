from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import Search,StoreC
from .search import  search, storec,resetC
# Create your views here.



def v1(response):
    return HttpResponse("<h1>view 1</h1>")

def home(response):
    data=""
    data2=""
    if response.method=="POST":
        search_form=Search(response.POST)
        # print(response)
        store_form=StoreC()
        if search_form.is_valid():
            data = search(search_form.cleaned_data["source"],search_form.cleaned_data["destination"])
         
    else:
        search_form=Search()
        store_form=StoreC()
    return render(response,'main/home.html', {"search_form":search_form,"store_form":store_form, "data":data, "data2":data2})

def store(response):
    data=""
    data2=""
    if response.method=="POST":
        store_form=StoreC(response.POST)
        search_form=Search()
        # print(response)
        if store_form.is_valid():
            data2 = storec(store_form.cleaned_data["graph"],store_form.cleaned_data["straight_line"])
              
    else:
        search_form=Search()
        store_form=StoreC()
    return render(response,'main/home.html', {"search_form":search_form,"store_form":store_form, "data":data, "data2":data2})

def reset(response):
    date=""
    date=resetC()
    return redirect('home')