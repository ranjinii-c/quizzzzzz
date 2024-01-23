from django.urls import path
from .views import welcome,quiz,quiz_home, submit_quiz

app_name = 'quiz'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('quiz/', quiz, name='quiz'),
    path('quizhome/', quiz_home, name='quiz_home'),
    path('submit/', submit_quiz, name='submit_quiz'),
]

