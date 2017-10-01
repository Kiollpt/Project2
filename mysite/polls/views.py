from django.http import HttpResponse,HttpResponseRedirect

from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question,Choice,Comment
from django.urls import reverse
#2017-09 Add posting board
from .forms import CommentForm
from django.shortcuts import redirect
#2017-09 Add posting board

#2017.10.1 Add login/out mechanisim
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as aa_login
from django.contrib.auth import authenticate
#2017.10.1 Add login/out mechanisim

# Create your views here.
def index(request):
    if request.method == "POST":
        return redirect('polls:index')

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    #return HttpResponse("Hello Ths is Harry")
    #return HttpResponse(output);


def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)

    #2017.9.19 Add posting board#
    all_comment_list= Comment.objects.all()
    #2017.9.19 Add posting board#

    return render(request, 'polls/details.html', {'question': question, 'all_comment_list':all_comment_list})



def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})





#2017.10.1 Add login mechanisim
def login(request):
    if request.method =='GET':
        print("call login")
        return render(request,'registration/login.html')

    name= request.POST.get('username')
    password= request.POST.get('password')
    user= authenticate(username=name,password=password)
    #print(name,password)
    #print(user)
    if not user:
        return render(request,'registration/login.html')
    aa_login(request,user)
    return  redirect('polls:index')


#2017.10.1 Add login mechanisim
'''
@:means python decorator as for packing a gift
'''
@login_required(login_url='/polls/login/')
#2017.10.1 Add login mechanisim
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#2017.9.19 Add posting board#
def post(request,question_id):
    if request.method == "POST":
        form= CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:detail',question_id)
    else:
        form= CommentForm()

    return render(request, 'polls/add_comment_to_post.html', {'form': form})

#2017.9.19 Add posting board#
