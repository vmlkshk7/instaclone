from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from InstaClone.views import signup_view, login_view, feed_view, post_view

urlpatterns = [
    url('feed/', feed_view),
    url('login/', login_view),
    url('', signup_view)
]