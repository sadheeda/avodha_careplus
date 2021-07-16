from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.fun,name='fun'),
    path('doctors.html/', views.doctors, name="doctors"),
    path('blog.html/', views.blog, name="blog"),
    path('blog.html/blog-single.html/', views.blogs, name="blogs"),
    path('blog.html/opthalmology.html/', views.opth, name="opth"),
    path('blog.html/gynaecology.html/', views.gyn, name="gyn"),
    path('blog.html/ent.html/', views.ent, name="ent"),
    path('services.html/', views.services, name="services"),

]