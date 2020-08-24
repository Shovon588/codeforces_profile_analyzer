from django.shortcuts import render
from django.contrib import messages
from . utils import *
from . models import UserName

# Create your views here.


def single(request):

    data = ''
    contest_info = ''
    submission_info = ''
    if request.method == 'POST':
        handle = request.POST['handle']
        handle = handle.lower()
        UserName.objects.get_or_create(username=handle)
        data = get_user_info(handle)
        if "message" in data:
            messages.error(request, data['message'])
            data = ''
        else:
            contest_info = get_contest_info(handle)
            submission_info = get_submission_info(handle)

    context = {'data': data, 'contest_info': contest_info, 'submission_info': submission_info}

    return render(request, 'analyzer/single.html', context=context)


def dual(request):
    user1 = ''
    user2 = ''
    user1_contest = ''
    user2_contest = ''
    user1_submission = ''
    user2_submission = ''

    if request.method=='POST':
        handle1 = request.POST['first']
        handle2 = request.POST['second']

        user1 = get_user_info(handle1)
        user2 = get_user_info(handle2)

        if 'message' in user1:
            messages.error(request, user1['message'])
            user1 = ''
        elif 'message' in user2:
            messages.error(request, user2['message'])
            user2 = ''
        else:
            user1_contest = get_contest_info(handle1)
            user1_submission  = get_submission_info(handle1)
            user2_contest = get_contest_info(handle2)
            user2_submission = get_submission_info(handle2)

    context = {'user1': user1, 'user1_contest': user1_contest, 'user1_submission': user1_submission,
               'user2': user2, 'user2_contest': user2_contest, 'user2_submission': user2_submission}

    return render(request, 'analyzer/dual.html', context=context)
