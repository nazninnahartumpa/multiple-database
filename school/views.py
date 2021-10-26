from django.shortcuts import render, redirect
from .models import School
from .forms import SchoolForm

# Create your views here.

def school(request):
    schools = School.objects.all()
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SchoolForm()
    context = {
        'schools': schools,
        'form' : form
    }

    return render(request, 'school/school.html', context)