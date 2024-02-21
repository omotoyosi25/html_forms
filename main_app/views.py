from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentData
from .forms import StudentForms, StudentForms2
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    student_form=StudentForms2()
    if request.method == 'POST':
        form_data=StudentForms2(request.POST)
        if form_data.is_valid():
            form_data.save()
    students=StudentData.objects.all()
    context={
        "students":students,
        "forms":student_form
    }

    return render(request, 'main/index.html', context)

@login_required
def delete_post(request, post_id):
    post=StudentData.objects.get(id=post_id)
    post.delete()
    return redirect("home")

@login_required
def edit_post(request, post_id):
    post_obj=get_object_or_404(StudentData, id=post_id)
    edit_form=StudentForms2(instance=post_obj)
    if request.method == 'POST':
        form_data=StudentForms2(request.POST, instance=post_obj)
        if form_data.is_valid():
            form_data.save()
            return redirect("home")
    context={
        'edit_form':edit_form
    }
    return render(request, 'main/edit_post.html', context)