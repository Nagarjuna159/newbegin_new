from django.urls import path,include
from mainapp import views

urlpatterns=[
    path('',views.index_view,name='index'),
    path('contact',views.contact_view,name='contact'),
    path('about',views.about_view,name='about'),
    path('python_web',views.pyweb_view,name='python_web'),
    path('javapy',views.javapy_view,name='javapy'),
    path('fullstack',views.fullstack_view,name="fullstack"),
    path('java',views.java_view,name='java'),
    path('thankyou',views.thankyou_view,name='thankyou'),
    path('Enroll',views.enquire_course_view,name='enroll'),
    path('quiz',views.quiz_view,name='quiz'),
    path('answers',views.answers_view,name='answers'),
    path('signup',views.signup_view,name='signup'),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
]