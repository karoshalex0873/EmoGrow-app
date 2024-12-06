from django.shortcuts import redirect, render
from emoapp.models import Student
from emoAdmins.models import Assignment

# Create your views here.
def Getstarted(request):
    return render(request, "index.html")
def About(request):
    return render (request, 'about.html')
def Contact(request):
    return render(request ,'contact.html')
def Pricing(request):
    return render(request, 'pricing.html')

def Main(request):
    if request.method == "POST":
        if Student.objects.filter(
            email=request.POST["email"], password=request.POST["password"]
        ).exists():
            users = Student.objects.get(
                email=request.POST["email"], password=request.POST["password"]
            )
            return render(request, "main.html",{'user':users})
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


def notices(request):
    docs = Assignment.objects.all()
    for doc in docs:
        # Check if the file is a PDF
        if doc.file:
            file_extension = doc.file.name.split(".")[-1].lower()
            if file_extension == "pdf":
                doc.is_pdf = True
            else:
                doc.is_pdf = False
        else:
            doc.is_pdf = False
    return render(request, "notice.html", {"notices": docs})
