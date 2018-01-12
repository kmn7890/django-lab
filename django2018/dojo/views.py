import os
from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
# Create your views here.

def mysum(request, numbers):
    # numbers = "1/2/12/123/1234/1231231"
    # request : HttpRequest의 인스턴스))
    result = sum(map(lambda s: int(s or 0), numbers.split('/')))
    return HttpResponse(result)

def hellogongyoo(request, name, age):
    return HttpResponse('Hello {} {} age year old'.format(age, name))


def postlist1(request):
    name = "공유"
    return HttpResponse('''
    <h1>Function Based View Responded by HTML Form</h1>
    <p> {name} </p>
    <p> Hello, This is written in HTML code format </p>
    '''.format(name=name))


def postlist2(request):
    name="공유"
    which_view='Function Based View'
    return render_to_response('dojo/post_list.html', {'name':name, 'which_view':which_view})


#json 형식으로 응답하기
def postlist3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items':['python','django','celery','azure','aws']
    },json_dumps_params={'ensure_ascii':False})


def exceldownload(request):
    # filepath = '/Users/kangmina/djproject/django2018/커리큘럼ver2.xlsx'
    filepath = os.path.join(settings.BASE_DIR, '커리큘럼ver2.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') #text/html
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response