from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def render_publicaciones(request):
    # pylint: disable=E1101
    posts = Post.objects.all()
    return render(request, 'publicaciones.html', {'posts': posts})

def post_detail(request, post_id):
    post= get_object_or_404(Post,pk=post_id)
    return render(request, 'post_detail.html', {"post": post})