

# Create your views here.
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('', views.landing, name='landing'),
  path('blog/', views.blog, name='blog'),
  path('my_account/', views.my_account, name='my_account'),
  path('login/', views.login, name='login'),
]


