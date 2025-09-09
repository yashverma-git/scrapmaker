# home/views.py
from django.shortcuts import render
from datetime import datetime

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
        # Local import to avoid circular import
        from .models import Contact

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

        # Render the same page with a success message
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

