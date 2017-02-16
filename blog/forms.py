from django import forms
from .models import Post

# class PostForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        if len(content) % 2 == 0:
            self.add_error('content', '홀수 길이로 입력하세요')
        content = '  '.join(word for word in content.split())
        return content
        #clean은 return값이 꼭 있어야 한다.
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

# .get => (사전 타입에서) 찾는 key가 없으면 keyerror를 발생하지 않고 값으로서 어떤 것을 return하겠다 를 지정할 수 있음.
# self.cleaned_data.get('content', '') 는 'content'라는 키가 없으면 ''을 return하겠다는 뜻.