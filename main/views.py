from ast import pattern
from audioop import reverse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from . import sql_queries
from . import models
from django.shortcuts import redirect
from django.contrib import messages

def home(request):
    #print(models.questionBank.objects.all())
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('form_check') == 'question':

            view = request.POST.get('subject_view')

            subject = request.POST.get('subject_add')
            marks = request.POST.get('marks')
            question = request.POST.get('question')
            topic = request.POST.get('topic')
            print(subject,marks,question,topic,view)
            sql_queries.questionEntry(subject,question,marks,topic)

            context = {'message_from':'add'}
            messages.success(request,'Question Added Sucessfully')

            return render(request,'main/home.html',context)

        elif request.POST.get('form_check') == 'generate':

            chapter_list = []
            chapter1 = request.POST.get('chapter1')
            chapter2 = request.POST.get('chapter2')
            chapter3 = request.POST.get('chapter3')
            chapter4 = request.POST.get('chapter4')
            chapter5 = request.POST.get('chapter5')
            chapter6 = request.POST.get('chapter6')

            if chapter1 is not None:
                chapter_list.append(chapter1)
            if chapter2 is not None:
                chapter_list.append(chapter2)
            if chapter3 is not None:
                chapter_list.append(chapter3) 
            if chapter4 is not None:
                chapter_list.append(chapter4)
            if chapter5 is not None:
                chapter_list.append(chapter5)
            if chapter6 is not None:
                chapter_list.append(chapter6)

            pattern = request.POST.get('pattern')
            print(pattern)
            subject = request.POST.get('subject')
            sql_queries.questionSelector(subject,chapter_list,pattern)

            context = {'message_from':'pdf'}
            messages.success(request,'PDF Generated Sucessfully')

            return render(request,'main/home.html',context)

        # elif request.POST.get('form_check') == 'login':
        #     return redirect('home')
        else:

            subj = request.POST.get('subject_questions')
            return redirect('questions',subj = subj)
            


    else:
        return render(request,'main/home.html')

def viewQuestions(request,subj):
    context = {}
    questions = models.questionBank.objects.filter(subj=subj)
    context = {'questions':questions}
    return render(request,'main/questions.html',context)

def viewLogin(request):
    # context = {}
    return render(request,'main/login.html')

# def vLogin(request):
#     # context = {}
#     return redirect('home')