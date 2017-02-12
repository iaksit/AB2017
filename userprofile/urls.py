"""collectivework URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url


from ticket.views import list_ticket, create_ticket, list_my_ticket, list_moderation_requests, show_ticket
from userprofile.views import login, logout, signup, update

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^signup/$', signup, name="signup"),
    url(r'^update/$', update, name="update"),
    url(r'^logout/$', logout, name="logout"),
]