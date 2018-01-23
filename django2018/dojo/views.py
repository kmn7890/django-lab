import os
from django.conf import settings
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import PostForm
from .models import Post
# Create your views here.

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # 인자가 다 있음 함께 넘겨서 validator에서 문제 안생기먄
        if form.is_valid():
            post = form.save(commit=False)
            # 모델폼에서 지원되는 commit kwargs를 활용해서 save 하면 됨
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            #방법1)
             # post = Post()
             # post.title = form.cleaned_data['title']
             # post.content = form.cleaned_data['content']
             # post.save()

             # 방법2)
            # post = Post(title=form.cleaned_data['title'],
            #               content=form.cleaned_data['content'])
            # post.save()

            # 방법3)
            # post = Post.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'])


            # 방법4)
            # post = Post.objects.create(**form.cleaned_data)
            return redirect('blog:post_list')
        else:
            form.errors
            # 방법3)
            # post = Post.objects.create(title=form.cleaned)
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form':form,
    })

def post_detail(request, id):
    post = Post.objects.filter(id=id)
    return render(request, 'dojo/post_detail.html',{
                'post':post,
                    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('blog:post_list')
        else:
            form.errors
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form':form,
    })

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