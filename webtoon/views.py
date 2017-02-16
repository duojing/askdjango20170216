from django.shortcuts import render

from .models import Webtoon


#q는 query의 약자로 선생님이 임의로 지정.
def webtoon_list(request):
    q = request.GET.get('q', '')
    qs = Webtoon.objects.all()

    if q:
        qs = qs.filter(title__icontains=q)
        # 필터를 씌운 것을 다시 ... ?
        # TODO !!!!
        pass

    return render (request, 'webtoon/webtoon_list.html', {
        'webtoon_list' :
        #Webtoon.objects.all(),
        qs,
        'q': q,
        })

def webtoon_detail(request, id):
    webtoon = Webtoon.objects.get(id=id)
    return render(request, 'webtoon/webtoon_detail.html', {
        'webtoon': webtoon,
        })