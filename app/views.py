from django.shortcuts import render, redirect
from .models import Treatment
from django.middleware.csrf import get_token
import pymysql

# 执行搜索
class E_search:
    def search(self, content):
        return self.excerpt_search(content)

    def excerpt_search(self, title):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='science',
                               cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        title = f'%{title}%'
        str = 'select * from science.app_treatment where excerpt or bzimage like %s'
        cursor.execute(str, [title])
        response = cursor.fetchall()
        conn.close()
        print(response)
        return response


# Create your views here.

# 首页
def index(request):
    return render(request, 'index.html')


def process(request):
    return render(request, 'process.html')


def medicine(request):
    treatment = Treatment.objects.all()

    return render(request, 'medicine.html', locals())


def science(request):
    # allarticle = Treatment.objects.all().order_by('-id')
    treatment = Treatment.objects.all()

    return render(request, 'science.html', locals())


def introduce(request):
    return render(request, 'introduce.html')


def search(request):
    if request.method == 'GET':
        dic = [{'type': '', 'excerpt': ''}]
        return render(request, 'search.html', context={'dic': dic})
    elif request.method == 'POST':
        csrf_token = get_token(request)  # 添加csrf_token用于post请求
        data = request.POST.get('title')
        a = E_search()
        rsp = a.excerpt_search(data)
        return render(request, 'search.html', context={'dic': rsp})
