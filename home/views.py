from django.shortcuts import render, HttpResponse

def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is a Homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is a Aboutpage")

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("This is a contactpage")

def features(request):
    return render(request,'features.html')
    # return HttpResponse("This is a featurespage")
