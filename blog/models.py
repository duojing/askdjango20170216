from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator

def lnglat_validator(value):
    if not re.match(r'^([+-]\d+\.?\d*), ([+-]\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model): #상속받기
    user = models.ForeignKey(User, related_name='blog_post_set')
    author = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=100,
    validators=[MinLengthValidator(10)]
,    verbose_name = '제목', help_text = "포스팅 제목으로 노출됩니다. 최대 100자까지 지원됩니다.") #descriptor syntax
#클래스변수나 ??변수를 선언한 것이 아니다.

    # blank=True or null=True : 옵션 필드
    # blank옵션/null옵션 제공X : 필수 필드

    content = models.TextField()#verbose_name = '내용')
    photo = models.ImageField()

#길이 제한이 있는 문자열/없는 문자열이 서로 다른 필드에.
    created_at = models.DateTimeField(auto_now_add=True)
    #포스팅 최초 생성 시각을 저장하기 위한 목적.
    #auto_now_add 를 True로 주면 자동으로 넣어줌.
    #created_at, updated_at 이 두 개의 필드는 자동화되어 우리가 따로 신경 쓸 필요 없음.
    updated_at = models.DateTimeField(auto_now=True)
    #수정 시각 저장하기 위한 목적.

    lnglat = models.CharField(max_length=50, blank=True, validators=[lnglat_validator])
    #경도, 위도 남기기
#결국 우리는 제목 / 내용 두 필드만 넣어주면 된다.

    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[-1]
        return None

    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]
        return None

    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name