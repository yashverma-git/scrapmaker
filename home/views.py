from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from .models import Contact  # Import at top unless circular import issue


# Home page view
def index(request):
    context = {
        'variable': "this is sent"  # example variable to pass to template
    }
    return render(request, 'index.html', context)


# About page view
def about(request):
    return render(request, 'about.html')


# Features page view
def features(request):
    return render(request, 'features.html')


# Contact page view
def contact(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        # Save contact form data to database
        new_contact = Contact(
            name=name,
            email=email,
            phone=phone,
            description=description,
            date=datetime.today()
        )
        new_contact.save()

        # Add a success message
        messages.success(request, "Your request has been sent!")

        # Render with success context
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


# Buy page view
def buy(request):
    return render(request, 'buy.html')


# Sell page view
def sell(request):
    return render(request, 'sell.html')


# Offer page view
def offer(request):
    return render(request, 'offer.html')
