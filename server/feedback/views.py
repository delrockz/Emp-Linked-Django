from django.shortcuts import render

# Create your views here.

def FeedbackView(request):
    return render(request,"contact.html",{})