from django.shortcuts import render,redirect
from . models import Image
from . forms import ImageForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request,"index.html",{'obj':obj})
    
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request,"index.html",{'img':img, 'form':form})