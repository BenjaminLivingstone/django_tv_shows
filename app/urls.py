from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.show),
    path('shows/', views.show),
    path('shows/new/', views.newshowform),
    path('shows/new/addshow/', views.addshow),
    path('shows/<int:num>/', views.detail),
    path('shows/<int:num>/edit', views.edit),
    path('shows/<int:num>/destroy', views.destroy),
]