from django.urls import path
from . import views
from django.urls import reverse_lazy, reverse

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('xodim/', views.XodimCreateView.as_view(), name='xodim'),
    path('mydoc/', views.MyDocListView.as_view(), name='mydoc'),
    path('editdoc/<int:pk>/', views.EditDocDetailView.as_view(), name='editdoc'),
    path('archive/<int:pk>/', views.ArchiveDocDetailView.as_view(), name='archive'),
    path('checked_doc/', views.CheckedDocListView.as_view(), name='checked_doc'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
