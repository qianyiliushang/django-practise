# coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Question
from .models import Choice
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import sys
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

reload(sys)
sys.setdefaultencoding('utf-8')


class IndexView(generic.ListView):
    template_name = '../templates/polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = '../templates/polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = '../templates/polls/results.html'


# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {'latest_question_list': latest_question_list, })
#     return HttpResponse(template.render(context))
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, '../templates/polls/detail.html', {'question': p, 'error_message': '请做出选择'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
