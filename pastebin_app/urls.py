from django.urls import path
from . import views

app_name = 'pastebin'
urlpatterns = [
    path('', views.PasteList.as_view(), name='paste_list'),
    path('paste/create', views.PasteCreate.as_view(), name='create'),
    path('paste/<int:pk>', views.PasteDetail.as_view(), name='paste_detail'),

]