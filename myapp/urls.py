
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.myfunc,name="myfunc"),
    path('log-in',views.login,name="login"),
    path('cancel',views.cancel,name="cancel"),
    path('reg-in',views.regist,name="regist"),
    path('reg-sub',views.add,name="add"),
    path('log-sub',views.save,name="save"),
    path('add-btn',views.add_btn,name="add_btn"),
    path('asset-add',views.asset_data,name="asset_data"),
    path('view-btn',views.asset_view,name="asset_view"),
    path('edit-btn',views.edit,name="edit"),
    path('dataedit',views.asset_edit,name="asset_edit"),
    path('asset-update',views.asset_update,name="asset_update"),
    path('del-btn',views.del_but,name="del_but"),
    path('deleted',views.deletee,name="deletee"),
   
    path('backhome1',views.home,name="home"),
]
