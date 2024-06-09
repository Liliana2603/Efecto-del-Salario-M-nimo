from django.urls import path
from .views import render_publicaciones, post_detail
app_name = 'link'
urlpatterns = [
    path('', render_publicaciones, name='publicaciones'),
    path('<int:post_id>', post_detail, name="post_detail"),
]
