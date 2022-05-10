from django.urls import path
from . import views

app_name = 'pastebin'
urlpatterns = [
    path('', views.PasteList.as_view(), name='paste_list'),
    path('paste/create', views.PasteCreate.as_view(), name='create'),
    path('paste/<int:pk>', views.PasteDetail.as_view(), name='paste_detail'),
    path('paste/edit/<int:pk>', views.PasteUpdate.as_view(), name='paste_update'),
    path('paste/delete/<int:pk>', views.PasteDelete.as_view(), name='paste_delete'),



]