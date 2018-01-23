from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, TimeCheck

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html',{
        'post_list':qs,
        'q':q,
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {
        'post':post,
    })


def test_time(request):
    time_list = TimeCheck.objects.all()
    post_list = Post.objects.all()
    value = "pocketmon@gmail.com"
    return render(request, 'blog/timetest.html', {
        'time':time_list,
        'post_list':post_list,
        'value':value,
    })