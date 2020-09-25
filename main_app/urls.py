from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addwidget/', views.WidgetCreate.as_view(), name='add_widget'),
    path('<int:pk>/delete/', views.WidgetDelete.as_view(), name='widgets_delete'),
    path('<int:pk>/update/', views.WidgetUpdate.as_view(), name='widgets_update'),
]