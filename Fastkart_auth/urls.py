from django.urls import path
from Fastkart_auth import views

urlpatterns = [
    path('login/', views.handlelogin, name="handlelogin"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.handlelogout, name="handlelogout")
]
