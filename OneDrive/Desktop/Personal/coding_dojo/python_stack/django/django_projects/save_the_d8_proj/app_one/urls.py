from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_pg),
    path('register_pg', views.register_pg),
    path('register', views.register),
    path('login', views.login),
    path('main', views.main),
    path('add_new_pg', views.add_new_pg),
    path('add_new', views.add_new),
    path('all_people', views.all_people),
    path('select_person', views.select_person),
    path('show_person/<int:person_id>', views.show_person),
    path('add_gift/<int:person_id>', views.add_gift),
    path('logout', views.logout)

]