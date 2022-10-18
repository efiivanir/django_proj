from django.views.generic import ListView, DetailView
from .models import Post


# new
class BlogListView(ListView):
        model = Post
        template_name = "home.html"


class BlogDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"