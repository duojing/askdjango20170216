from django.contrib import admin
from blog.models import Post, Comment, Tag
from blog.forms import PostForm


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'lnglat', 'created_at', 'content_length'] #이 작업 해주지 않으면 포스트 제목이 보이지않고 Post Object라는 명으로 뜸.
    list_display_links = ['title'] #링크가 아이디가 아닌 타이틀에 들어가게
    search_fields = ['title'] #제목 검색 가능하게
    list_filter = ['created_at'] #필터링링
    form = PostForm

    #포스트의 글자수 보이게 커스터마이징
    def content_length(self, post):
        return "{}글자".format(len(post.content))
    content_length.short_description = '글자수'
    #함수에게도 attribute를 지정해줄 수 있으므로 "'글자수'를 컬럼 네임으로 쓰겠다"는 선언.

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)

admin.site.register(Tag)