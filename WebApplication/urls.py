"""WebApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from WebApp.views import home,upload,view_hello_world,table,data_save,view_update_booking,view_update_form_data_in_db,delete_object,view_register_user
from restapi.views import view_get_post_book,view_getByID_updateByID_deleteByID,api_update_data
from uploadapp.views import index,normalupload
from WebApp.views import view_authenticate_user

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path("table/",table,name="table"),
    path('table/booking',home,name="booking"),
    path('table/booking/save',data_save),
    path("table/table",table),
    path("save",data_save),
    path("upload",upload),
    path("table/upload",upload),
    path("table/save",data_save),
    path("edit/<int:ID>",view_update_booking),
    path("table/edit/<int:ID>",view_update_booking),
    path("edit/update/<int:ID>",view_update_form_data_in_db),
    path("table/edit/update/<int:ID>",view_update_form_data_in_db),
    path('table/delete/<int:ID>',delete_object),
    path('delete/<int:ID>',delete_object),
    path('upload',index),
    path('normalupload',normalupload,name="noramalupload"),
    path('signup/',view_register_user,name="signup"),
    path('restrictpage/',view_hello_world),
    path('api/book/',view_get_post_book),
    path('api/book/<int:ID>',view_getByID_updateByID_deleteByID),

    path('api/book/update/<int:ID>',api_update_data),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=[
    path('accounts/login/',view_authenticate_user,name="login")
]
