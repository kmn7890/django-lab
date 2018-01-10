from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mysum(request):
    # request : HttpRequest의 인스턴스
    return HttpResponse(x)