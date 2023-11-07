from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # get and post req. for insert
    # get and post req. for update

    # get  req. to retrieve and display
    path('master/setting/dis', views.setting_display_list,
         name='setting_display_list'),
    path('master/setting/add', views.setting_create, name='setting_create'),
    path('master/setting/detail/<setting>',
         views.setting_detail, name='setting_detail'),
    path('master/setting/edit/<setting>',
         views.setting_edit, name='setting_edit'),
    path('master/setting/delete/<setting>',
         views.setting_delete, name='setting_delete'),
    # path('master/',views.api_modelname_call, name = 'master'),
    path('master/demo2', views.search_item, name='master2'),
    path('master', views.search_item, name='master3'),
    path('master/mock1', views.master, name='mock1'),
    path('master/demo4', views.master4, name='master4'),
    path('master/scan', views.scan_barcode, name='scan'),



]
