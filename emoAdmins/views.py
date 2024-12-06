from django.shortcuts import render, redirect
from emoAdmins.forms import AssignmentForm
from django.contrib import messages
from emoAdmins.models import teacher, Assignment


def admin_site(request):
    if request.method == "POST":
        if teacher.objects.filter(
            email=request.POST["email"], password=request.POST["password"]
        ).exists():
            return render(request, "admin.html")
        else:
            return render(
                request, "loginAdmin.html", {"error": "Invalid email or password"}
            )
    return render(request, "admin.html")


def adminLogin(request):
    return render(request, "loginAdmin.html")


def show_assignments(request):
    if request.method == "POST":
        title = request.POST.get("title")  # Fetch the title from the form
        uploaded_file = request.FILES.get("file")  # Get the uploaded file
        if title and uploaded_file:
            # Save the assignment
            Assignment.objects.create(title=title, file=uploaded_file)
            return redirect("show_assignments")  # Redirect to the same page
    # Retrieve all assignments
    docs = Assignment.objects.all()
    return render(request, "upload_assignments.html", {"docs": docs})
