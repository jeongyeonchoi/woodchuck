"""prenewbiethonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.main, name='main'),
    path('crud/<int:post_id>', crud.views.show, name='show'),
    path('crud/new', crud.views.new, name='new'),
    path('crud/postcreate', crud.views.postcreate, name='postcreate'),
    path('crud/edit', crud.views.edit, name='edit'),
    path('crud/postupdate/<int:post_id>', crud.views.postupdate, name='postupdate'),
    path('crud/postdelete/<int:post_id>', crud.views.postdelete, name='postdelete'),
]
