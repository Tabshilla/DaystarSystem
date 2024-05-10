from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    
    #baby paths
    path('<int:id>', views.view_baby, name='view_baby'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),

    #sitter paths
    path('<int:id>', views.view_sitter, name='view_sitter'),
    path('addsitter/', views.addsitter, name='addsitter'),
    #path('allsitters/', views.allsitters, name='allsitters'),
    path('editsitter/<int:id>/', views.editsitter, name='editsitter'),
    path('deletesitter/<int:id>/', views.delete, name='deletesitter'),

   #payment urls
   path('payment/', views.payment, name='payment'),
   path('allpayments/', views.allpayments, name='allpayments'),
  

   #login urls
   path('login/', views.loginpage, name='login'),
   path('register/', views.registerpage, name='register'),
   path('logout/', views.logoutUser, name='logout'),

    ]