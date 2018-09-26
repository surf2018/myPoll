from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Poll,Choice
# Create your views here.
def index(request):
    Lastquestion_list=Poll.objects.all()
    context={'Lastquestion_list':Lastquestion_list}
    return render(request,'vote/index.html',context)
def detail(request,question_id):
    question=get_object_or_404(Poll,pk=question_id)
    context={'question':question}
    return render(request,"vote/detail.html",context)
def result(request,question_id)
    question=get_object_or_404(Poll,pk=question_id)
    context={'question':question}
    return render(request,"vote/result.html",context)
def vote(request,question_id):

