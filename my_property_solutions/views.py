from django.shortcuts import redirect
from django.shortcuts import render

def landing_page(request):
    return render(request, 'account/signup.html')
    return redirect('https://www.mypropertysystem.com.au/')
