from django.contrib import admin
from django.urls import path
from shop import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path("register/",views.Register,name="register"),
    path("login/",LoginView.as_view(template_name="shop/login.html"),name="login"),
    path("profile/",views.Profile,name="profile"),
   
]