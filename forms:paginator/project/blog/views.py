from .models import Blog #,Comment
#from .forms import CommentForm
#from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
#from matplotlib.pyplot import title
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from .form import BlogForm 
from django.core.paginator import Paginator

def detail(request,id):
    blog = get_object_or_404(Blog,pk = id)
    return render(request,'detail.html',{'blog':blog})


# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    paginator=Paginator(blogs,3)
    pagnum=request.GET.get('page')
    blogs=paginator.get_page(pagnum)
    return render(request,'home.html',{'blogs':blogs})

def new(request):
    #1. 데이터가 입력된 후 제출 버튼을 누르고 데이터 저장-> post
    #2. 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 -> get
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=BlogForm()
        return render(request,'new.html',{'form':form})

def create(request):
    new_blog=Blog()
    new_blog.title=request.POST['title']
    new_blog.content= request.POST['content']
    new_blog.author=request.user
    new_blog.image=request.FILES['image']
    new_blog.save()
    return redirect('detail',new_blog.id)

def edit(request,id):
    edit_blog = get_object_or_404(Blog,pk = id) # 파라미터 id를 받아서 디비에 해당 객체를 가져온다.
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog = get_object_or_404(Blog,pk=id) # 파라미터로 받은 id의 Blog 객체 가져옴
    update_blog.title = request.POST['title'] 
    update_blog.content = request.POST['content']
    if request.FILES:
        update_blog.image=request.FILES['image']
    update_blog.save()
    return redirect('detail',update_blog.id)

def delete(request,id):
    delete_blog  = get_object_or_404(Blog,pk = id) #파라미터로 받은 id에 해당하는 Blog객체 가져옴
    delete_blog.delete() #삭제
    return redirect('home')

###def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


