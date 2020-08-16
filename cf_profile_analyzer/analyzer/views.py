from django.shortcuts import render
from django.http import HttpResponse
from . utils import *

# Create your views here.


def single_profile_search(request):
    data = None
    if request.method == 'POST':
        handle = request.POST['handle']
        data = get_user_info(handle)

    return render(request, 'analyzer/single.html', data)


def single_profile_detail(request):
    return HttpResponse("<h1>Single Result</h1>")


def dual_profile_search(request):
    return HttpResponse("<h1>Dual Search</h1>")


def dual_profile_detail(request):
    return HttpResponse("<h1>Dual Result</h1>")