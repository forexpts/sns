from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import AccountSiginupForm, AccountLoginForm, AccountPasswordChangeForm, AccountAvatorUploadForm
from .models import Account, Follow
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

# Create your views here.
class AccountSignUpView(generic.CreateView):
    form_class = AccountSiginupForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

class AccountLoginView(auth_views.LoginView):
    form_class = AccountLoginForm
    template_name = 'account/login.html'

class AccountLogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'

class AccountDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Account
    success_url = reverse_lazy('signup')
    template_name = 'account/delete.html'

    def test_func(self):
        account = self.get_object()
        return account == self.request.user

    def handle_no_permission(self):
        return HttpResponseForbidden()

class AccountDetailView(generic.DetailView):
    model = Account
    template_name = 'account/detail.html'

class AccountPasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    form_class = AccountPasswordChangeForm
    template_name = 'account/password_change.html'

class AccountPasswordChangeDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'

class AccountAvatorUploadView(LoginRequiredMixin, generic.FormView):
    template_name = 'account/avator_upload_form.html'
    form_class = AccountAvatorUploadForm

    def form_valid(self, form):
        user = self.request.user
        avator = form.cleaned_data['avator']
        account = Account.objects.get(username=user)
        account.avator = avator
        account.save()
        return redirect('avator_upload_done')

class AccountAvatorUploadDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/avator_upload_done.html'

@login_required
def post_follow(request, pk):
    if request.method == 'POST':
        #Followするユーザを取得
        follow_user = Account.objects.get(pk=pk)
        #自分自身か確認
        if request.user == follow_user:
            messages.error(request, '自分自身をフォローすることはできません')
            return redirect(to='/')
        
        #すでにフォローしているか確認
        is_follow = Follow.objects.filter(follow_id=request.user).filter(follower_id=follow_user).count()
        if is_follow > 0:
            #フォロー解除
            follow_user.follower_count -= 1
            follow_user.save()
            request.user.following_count -= 1
            request.user.save()

            follow = Follow.objects.get(follow_id=request.user, follower_id=follow_user)
            follow.delete()
            messages.success(request, 'ユーザのフォローを解除しました')
        else:
            #Followerを増やす
            follow_user.follower_count += 1
            follow_user.save()
            #Followingを増やす
            request.user.following_count += 1
            request.user.save()

            follow = Follow()
            follow.follow_id = request.user
            follow.follower_id = follow_user
            follow.save()

        messages.success(request, 'ユーザをフォローしました')
    else:
        messages.error(request, '正しい方法でリクエストしてください')
    return redirect(to='/')