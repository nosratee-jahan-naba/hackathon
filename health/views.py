from django.shortcuts import render
from .models import HealthCheck

# Home page with list of all health check-ins
def home(request):
    checks = HealthCheck.objects.all()
    return render(request, 'home.html', {'checks': checks})

# Check-in page
def check_in(request):
    if request.method == "POST":
        mood = request.POST.get('mood')
        note = request.POST.get('note')
        new_check = HealthCheck(user_name="Anonymous", mood=mood, note=note)
        new_check.save()
    return render(request, 'check_in.html')
