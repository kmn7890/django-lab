#dojo앱의 forms.py
#파이썬에서는 어떤 것이든간에 텍스트 양을 구분하지 못하므로 할 수 없다

from django import forms
from .models import Post

#form에서 validator는 예외발생유무로 처리한다. url에서는 False냐 True냐만 중요한데.
#validator는 함수 단위로 구현하고 값을 늘 받음 이 value에 담겨서 title의 char이 넘겨지는 것 . 그리고 이 validator에서 Error를 내는 것
#validator는 우편 번호, 사업자 등록번호 많은 것이 가능할 것. 원하는 형식이 아니면 잘 전달되게 할 수 있음
def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('3글자 이상 입력해야합니다')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    '''
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea()) #여러줄 입력받는 것으로 됨 클래스(Textarea)도 되고, 인스턴스(Textarea())도 된다.
    #함수를 넘기는 것. 함수를 호출하는게 아님 . 1급객체의 특징

    '''

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post


