from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #모델로부터 객체목록을 전달받을 수 있게 함 == 쿼리셋 // 메소드
    return render(request, 'home.html', {'blogs': blogs})

#쿼리셋과 메소드의 형식
#모델.쿼리셋(objects).메소드

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id) #이용자가 원하는 몇 번째 블로그 객체
    #home화면처럼 모든 객체를 보여주는 것이 아닌 '특정 번호의 객체'를 담아야 함
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):#new.html을 띄어주는 함수
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    #blog라는 객체에 해당하는 내용을 데이터베이스에 저장해라
    return redirect('/blog/'+str(blog.id))
    #render함수와 redirect함수의 차이 : 함수의 인자(상황)에 따라 달라짐
    #redirect함수 : 다른 url을 연결할 수 있음
    #render함수 : 세번째 인자로 키값을 받음. 데이터를 담아서 처리하고 싶을때 사용
    