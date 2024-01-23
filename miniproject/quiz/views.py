from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse

def welcome(request):
    return render(request,'quiz/welcome.html')

def quiz(request):
    return render(request,'quiz/quiz.html')

def quiz_home(request):
    
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'quiz/quiz_home.html', context)


def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        for question_id, submitted_choice_id in request.POST.items():
            if question_id.isdigit():
                try:
                    question = get_object_or_404(Question, pk=question_id)
                    selected_choice = question.choice_set.get(pk=int(submitted_choice_id))
                except (Question.DoesNotExist, Choice.DoesNotExist, ValueError) as e:
                    print(f"Error processing question {question_id}: {e}")
                    selected_choice = None  
                
                if selected_choice and selected_choice.is_correct:
                    score += 1

        request.session['quiz_score'] = score

        messages.success(request, 'QUIZ SUBMITTED!!!')
        
        return render(request,'quiz/submit_quiz.html')



   