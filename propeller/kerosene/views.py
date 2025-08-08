from django.shortcuts import render
from .models import aunt

def binayak(req):
    b=aunt.objects.all()
    return render (req,'TU.html',{'a' : b })
def bibash(rr):
    return render(rr,'bibash.html')