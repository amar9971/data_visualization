from django.shortcuts import render , redirect
from .models import Countrydata
from.forms import CountryDataForms

# Create your views here.
def index(request):
    data=Countrydata.objects.all()
    if request.method == "POST":
        form = CountryDataForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = CountryDataForms()    
        
    
    context = {
        'data': data,
        'form' : form,

    }
    return render(request, 'dashboard/index.html', context)
