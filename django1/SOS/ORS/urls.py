from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_signin),
    path('test/', views.test),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('welcome/', views.welcome),
    path('logout/', views.logout),
    path('list/', views.user_list),
    path('save/', views.user_save),
    path('edit/<int:id>/', views.edit_user),
    path('delete/<int:id>/', views.delete_user),
]
