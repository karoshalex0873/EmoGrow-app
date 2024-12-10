from django.shortcuts import get_object_or_404, redirect, render
from emoAdmins.forms import AssignmentForm
from emoapp.models import S_Assignment, Student, SurveyQuestion
from emoAdmins.models import Assignment
from emoapp.forms import SubmitForm, SurveyResponseForm
from django.contrib import messages


# Create your views here.
def Getstarted(request):
    return render(request, "index.html")


def About(request):
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def Pricing(request):
    return render(request, "pricing.html")


def Main(request):
    if request.method == "POST":
        if Student.objects.filter(
            email=request.POST["email"], password=request.POST["password"]
        ).exists():
            users = Student.objects.get(
                email=request.POST["email"], password=request.POST["password"]
            )
            return render(request, "main.html", {"user": users})
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    else:
        return render(request, "login.html")


def Register(request):
    if request.method == "POST":
        register_user = Student(
            name=request.POST["name"],
            email=request.POST["email"],
            age=request.POST["age"],
            gender=request.POST["gender"],
            password=request.POST["password"],
        )
        register_user.save()
        return redirect("/login")
    else:
        return render(request, "register.html")


def Login(request):
    return render(request, "login.html")


def show_assignment(request):
    student_assigment = Assignment.objects.all().order_by("title")
    return render(request, "assignments.html", {"student_assigment": student_assigment})


def assignment_list(request):
    if request.method == "POST":
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("assignment")
        else:
            messages.error(request, "Error uploading assignment. Please try again.")
    else:
        form = SubmitForm()
    submitted = Assignment.objects.all()
    return render(request, "main.html", {"form": form, "submitted": submitted})


def survey_questions(request):
    questions = SurveyQuestion.objects.all()

    if request.method == "POST":
        question_id = request.POST.get("question_id")  # Get the specific question ID
        question = get_object_or_404(SurveyQuestion, id=question_id)
        form = SurveyResponseForm(request.POST)

        if form.is_valid():
            response = form.save(commit=False)
            response.question = question
            response.save()
            return redirect("survey_questions")  # Redirect to refresh the page

    else:
        form = SurveyResponseForm()

    return render(request, "main.html", {"questions": questions, "form": form})
