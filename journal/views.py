from django.shortcuts import render
from .forms import PostForm
from .models import Post


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'journal/post_detail.html', {'post':post,
        })

def post_list(request):
    return render(request, 'journal/post_list.html/', {'post_list' : Post.objects.all()})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            return redirect(post)

    else:
        form = PostForm()
    return render (request, 'journal/post_form.html', {
        'form':form,
        })
#장고에서 form을 처리하는 가장 일반적인 방식.