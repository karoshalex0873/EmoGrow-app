from django.shortcuts import get_object_or_404, render, redirect
from emoAdmins.forms import AssignmentForm, QuestionForm
from django.contrib import messages
from emoAdmins.models import Question, teacher, Assignment
from emoAdmins.forms import AssignmentForm


def admin_site(request):
    if request.method == "POST":
        if teacher.objects.filter(
            email=request.POST["email"], password=request.POST["password"]
        ).exists():
            users = teacher.objects.get(
                email=request.POST["email"], password=request.POST["password"]
            )
            return render(request, "admin.html",{'user':users})
        else:
            return render(
                request, "loginAdmin.html", {"error": "Invalid email or password"}
            )
    return render(request, "admin.html")


def adminLogin(request):
    return render(request, "loginAdmin.html")


def Upload(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Assignment uploaded successfully!")
            return redirect("upload")
        else:
            messages.error(request, "Error uploading assignment. Please try again.")
    else:
        form = AssignmentForm()
    assignments = Assignment.objects.all()  # Fetch all uploaded assignments
    return render(request, "admin.html", {"form": form, "docs": assignments})


def post_question(request):
    """Handles posting and displaying questions."""
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your question has been submitted successfully!")
            return redirect(
                "post_question"
            )  # Redirect to the same page after submission
        else:
            messages.error(
                request,
                "There was an error submitting your question. Please try again.",
            )
    else:
        form = QuestionForm()

    # Fetch all questions to display
    questions = Question.objects.all().order_by(
        "-created_at"
    )  # Assuming 'created_at' is a timestamp in the model

    return render(
        request,
        "post_question.html",
        {
            "form": form,
            "questions": questions,
        },
    )


def delete_assigment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    assignment.delete()
    messages.success(request, "Assignment deleted successfully!")
    return redirect("upload")

