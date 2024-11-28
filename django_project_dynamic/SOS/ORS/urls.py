from django.urls import path

from . import views

urlpatterns = [
    path('welcome/',views.welcome, name="WELCOME"),
    path('login/',views.user_signin,name="SIGN_IN"),
    path('signup/',views.user_signup,name="SIGN_UP"),
    path('logout/',views.user_logout,name="LOG_OUT"),
    path('marksheet/',views.add_marksheet),
    path('list/',views.marsheet_list),
    path('edit/<int:id>',views.edit_marksheet),
    path('delete/<int:id>',views.delete_marksheet),
    path('',views.welcome),
]
