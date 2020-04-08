from django.shortcuts import render,redirect
from .forms import Contact_form, Enquire_Course_Form, Quiz_form, SignupForm
from .models import Contact_Model, Enquire_Course_Model, Quiz
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
def signup_view(request):
    context = {}
    form = SignupForm
    if request.method:
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(new_user.password)
            new_user.save()
            return redirect('/accounts/login')
    else:
        form = SignupForm()
    context['form'] = form
    return render(request,'mainapp/signup.html',context)

def index_view(request):
    return render(request,'mainapp/index.html')

def contact_view(request):
    context = {}
    form = Contact_form
    if request.method :
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Contact_form
    context['form'] = form
    return render(request,'mainapp/contact.html',context)

def about_view(request):
    return render(request,'mainapp/about.html')

def pyweb_view(request):
    return render(request,'mainapp/pyweb.html')

def javapy_view(request):
    return render(request,'mainapp/java_py_combo.html')

def fullstack_view(request):
    return render(request,'mainapp/fulls.html')

def java_view(request):
    return render(request,'mainapp/java.html')

def enquire_course_view(request):
    context = {}
    form = Enquire_Course_Form
    if request.method :
        form = Enquire_Course_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/thankyou")
            
    else:
        form = Enquire_Course_Form
    context['form'] = form
    return render(request,'mainapp/enquire1.html',context)

def thankyou_view(request):
    return render(request,'mainapp/thankyou.html')

def quiz_view(request):
    context = {}
    questions = Quiz.objects.all()
    context['question'] = questions
    return render(request,'mainapp/quiz.html',context)

score = 0

def answers_view(request):
    context = {}
    questions = Quiz.objects.all()
    global score
    for question in questions:
        correct_answer = question.answer
        entered_answer = request.POST.get(str(question.id))

        if (entered_answer == correct_answer):
            score+=1

    context['score'] = score
    return render(request,'mainapp/answers.html',context)


