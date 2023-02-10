from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uzduotys/', views.UzduotisListView.as_view(), name='uzduotis_list'),
    path('uzduotys/<int:pk>', views.UzduotisDetailView.as_view(), name='uzduotis_detail'),
    path('vartotojo_uzduotis/', views.UserUzduotysListView.as_view(), name='vartotojo_uzduotis'),
    path('vartotojo_uzduotis/new', views.UserUzduotisCreateView.as_view(), name='vartotojo_uzduotis_new'),
    path('vartotojo_uzduotis/<int:pk>/update', views.UserUzduotisUpdateView.as_view(), name='vartotojo_uzduotis_update'),
    path('vartotojo_uzduotis/<int:pk>/delete', views.UserUzduotisDeleteView.as_view(), name='vartotojo_uzduotis_delete'),
    path('register/', views.register, name='register'),
]

