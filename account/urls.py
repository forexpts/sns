from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.AccountSignUpView.as_view(), name='signup'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),
    #アカウント削除
    path('<int:pk>/delete/', views.AccountDeleteView.as_view(), name='delete_account'),

    path('password_change/', views.AccountPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.AccountPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('avator/upload/', views.AccountAvatorUploadView.as_view(), name='avator_upload'),
    path('avator/upload/done/', views.AccountAvatorUploadDoneView.as_view(), name='avator_upload_done'),

    path('<int:pk>/', views.AccountDetailView.as_view(), name='detail_account'),
    path('<int:pk>/follow/', views.post_follow, name='follow'),
]

#computer9