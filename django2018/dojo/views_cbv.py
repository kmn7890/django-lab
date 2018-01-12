import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.generic.base import TemplateView


class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>Class Based View Responded by HTML Form</h1>
        <p> {name} </p>
        <p> Hello, This is written in HTML code format </p>
        '''

postlist1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name']='공유'
        context['which_view']='Class Based View'
        return context

postlist2 = PostListView2.as_view()


class PostListView3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

    def get_data(self):
        return {
            'message': '안녕 파이썬&장고',
            'items': ['python', 'django', 'celery', 'azure', 'aws']
        }

postlist3 = PostListView3.as_view()

#CBV 엑셀 다운로드 응답하기
class ExcelDonwloadView(View):
    def get(self, request):
        filepath = os.path.join(settings.BASE_DIR, '커리큘럼ver2.xlsx')
        filename = os.path.basename(filepath)
        with open(filepath, 'rb') as f:
            response = HttpResponse(f,
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            return response

exceldownload = ExcelDonwloadView.as_view()
