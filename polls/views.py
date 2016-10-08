from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,t_apk_system_config,Choice
from django.template import loader
from django.core.urlresolvers import reverse

# Create your views here.

#def index(request):
#	return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	#output=','.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)
	template=loader.get_template('polls/index.html')
	context={
	    'latest_question_list':latest_question_list}
	return HttpResponse(template.render(context,request))

def detail(request, question_id):
	#return HttpResponse("You're looking at question %s"%(question_id))
	try:
		question=Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist!")
	return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
	#response="You're looking at the result of question %s."
	#return HttpResponse(response % (question_id))
	question=get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'result':question})

def vote(request, question_id):
	#return HttpResponse("You're voting on question %s."%(question_id))
	question=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
		  'question':question,
		  'error_message':'You didn`t select a choice',
		})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))































