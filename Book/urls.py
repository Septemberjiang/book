"""Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from django.contrib import admin

from Book.views import log, register, BookHome
from Book import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', log.as_view()),
    path('register/', register.as_view()),
    path('bookhome/', BookHome.as_view()),
    # 支付宝
    path('book/',views.shopping),
    path('purchase/<goods_id>/',views.purchase),
    path('show_msg/',views.show_msg),
    # path('check_order/',views.check_order)

]
