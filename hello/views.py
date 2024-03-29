#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from django.urls import path

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list} #딕셔너리 형태
    return render(request, 'hello/question_list.html',context)
    
def detail(request, question_id):
    question = Question.objects.get(id = question_id)
    answer_list = Answer.objects.filter(question_id = question_id)
    context = {'question': question, 'answer_list': answer_list}
    return render(request, 'hello/question_detail.html', context)

def answer_create(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    #form에 POST된 내용을 바탕으로 question 객체에 연결되는 answer 객체를 생성
    question. answer_set.create(content= request.POST.get('content'), create_date= timezone.now())
    return redirect('hello:detail', question_id= question.id)    #여기서 디테일은 urls 파일에 있는 별칭이다.

def question_form(request):
    return render(request, 'hello/question_form.html')

def question_create(request):
    question= Question(subject = request.POST.get('subject'),create_date=timezone.now())
    question.save()
    return redirect('hello:index')
    
    #response = ""
    #for i in range(1, 4):  # i는 몇 번째 세트인지를 나타냄
        #response += "회원님~! {} 세트 시작하겠습니다\n".format(i)
        #for j in range(1, 11):  # j는 해당 세트에서 동작을 몇 번 반복했는지를 나타냄
            #response += "{}\n".format(j)
    #return HttpResponse(response)