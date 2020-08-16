from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from . utils import *

# Create your views here.


def single_profile_search(request):

    data = ''
    contest_info = ''
    submission_info = ''
    if request.method == 'POST':
        handle = request.POST['handle']
        data = get_user_info(handle)
        contest_info = get_contest_info(handle)
        submission_info = get_submission_info(handle)
        
        if len(data)==0:
            messages.error(request, "Invalid user handle. Please provide a valid one.")

    context = {'data': data, 'contest_info': contest_info, 'submission_info': submission_info}

    return render(request, 'analyzer/single_search.html', context=context)


def single_profile_detail(request):
    return HttpResponse("<h1>Single Result</h1>")


def dual_profile_search(request):
    return HttpResponse("<h1>Dual Search</h1>")


def dual_profile_detail(request):
    return HttpResponse("<h1>Dual Result</h1>")