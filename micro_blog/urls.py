"""micro_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login, name='login'),
    url(r'^about/', views.about, name='about'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^test/', views.test, name='test_feed'),
    url(r'^test_prof/', views.test_user_profile, name='test_user_profile'),
]

urlpatterns += url(r'^(?P<pk>\w+)', views.feed, name='feed'),
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)