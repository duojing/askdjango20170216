from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime
from django.http import HttpResponse
from blog.models import Post
from blog.forms import PostForm

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post,
        })


def post_list(request):
    return render(request, 'blog/post_list.html/', {'post_list' : Post.objects.all()})

    #now = datetime.datetime.now()
    #return render(request, 'blog/post_list.html',{'now':now,})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('통과한 값: ', form.cleaned_data)
            #return redirect(post)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.info(request, '포스팅을 잘 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
        })

    # form = PostForm()
    # return render(request, 'blog/post_form.html',{
    #     'form' : form,
    #     })

@login_required
def post_edit(request, pk):
    post = Post.objects.get(pk = pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            print('통과한 값: ', form.cleaned_data)
            # return redirect(post)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.info(request, '포스팅을 잘 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
        })


def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse ('현재 시간은 <b>{}</b> 입니다.'.format(now))

"""
class NowTemplateView:
    @staticmethod
    def as_view(template_name = None):
        def view(request):
            now = datetime.datetime.now()
            if template_name is None:
                return HttpResponse('현재 시각은 {}입니다.'.format(now))
            return render(request, template_name, {'now':now,
                })
        return view

post_list = NowTemplateView.as_view('blog/post_list.html')

current_datetime = NowTemplateView.as_view()
"""

def mysum(request, x):
    result = 0
    y = x.split('/')
    for i in y:
        if i != '':
            result += int(i)
    return HttpResponse(result)

def name_and_age(request, name, age):
    #age=None 으로 설정하면
    #if age : message = '안녕하세요. {}님. {}살이시네요.'.format(name, age)
    #else : message = '안녕하세요. {}님.'.format(name)
    #return HttpResponse(message)
    return HttpResponse("안녕하세요. {}. {}살 이시네요.".format(name, age))

#if 'name' in request.GET:
 #   name = request.GET['name'] #값을 하나만 가져옴
  #  name_list = ','.join(request.GET.getlist('name')) #다수 획득
   # message
