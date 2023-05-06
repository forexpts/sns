from django.views import generic
from django.shortcuts import render, redirect
from .models import Post, Favorite
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from account.models import Account, Follow
from django.db.models import Q
# Create your views here.

#投稿一覧
def index(request, num=1):
    data = Post.objects.filter(visibility='public')
    page = Paginator(data, 5)
    params = {
        'object_list': page.get_page(num)
    }
    return render(request, 'post/home.html', params)

#投稿作成
@login_required(login_url='login')
def create_post(request):
    #送信時の処理
    if request.method == 'POST':
        content = request.POST['content']
        user = request.user
        #モデルに保存
        post = Post()
        post.content = content
        post.owner = user
        post.visibility = request.POST['visibility']
        if request.FILES:
            post.image = request.FILES['image']
        post.save()
        messages.success(request, '投稿しました')
        return redirect(to='/')
    #それ以外
    else:
        form = PostForm()
    params = {
        'form': form
    }
    return render(request, 'post/create.html', params)

#投稿詳細
def post_detail(request, pk):
    data = Post.objects.get(pk=pk)
    params = {
        'object': data,
        'is_favorite': False
    }
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(owner=request.user).filter(content_id=data).count()
        if is_favorite > 0:
            params['is_favorite'] = True
    return render(request, 'post/detail.html', params)

#投稿削除
@login_required(login_url='login')
def delete_post(request, pk):
    if request.method == 'POST':
        data = Post.objects.get(pk=pk, owner = request.user)
        data.delete()
        messages.success(request, 'メッセージを削除しました')
    else:
        messages.error(request, '正しい方法で削除してください')
    return redirect(to='/')

#いいね
@login_required
def post_favorite(request, pk):
    if request.method == 'POST':
        #いいねを押した投稿を取得
        data = Post.objects.get(pk=pk)
        #自分がすでにいいねしているか確認
        is_favorite = Favorite.objects.filter(owner=request.user).filter(content_id=data).count()
        if is_favorite > 0:
            #いいね数を更新
            data.favorite_count -= 1
            data.save()
            #いいねを削除
            favorite = Favorite.objects.filter(owner=request.user).filter(content_id=data)
            favorite.delete()
            messages.success(request, 'お気に入りから削除しました')
        else:
            #いいね数を更新
            data.favorite_count += 1
            data.save()
            #いいねを保存
            favorite = Favorite()
            favorite.owner = request.user
            favorite.content_id = data
            favorite.save()
            messages.success(request, 'メッセージをお気に入りに登録しました')
    else:
        messages.error(request, '正しい方法でお気に入り登録してください')
        
    return redirect(to='/')

#投稿説明
def explain(request):
    return render(request, 'post/explain.html')