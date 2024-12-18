from django.urls import path
from . import views

urlpatterns = [
    path('',views.sai, name='sai'),
    path('get/<int:id>', views.get_update, name='get_update'),
    path("update_s/<int:id>", views.update_s, name='update_s'),
]