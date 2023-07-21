# from django.shortcuts import render
# from .models import Post
# from django.core.paginator import Paginator

# # Create your views here.


# def post_list(request):
#     all_post = Post.objects.all().order_by('id')
#     paginator = Paginator(all_post, 3)
#     page_number = request.GET.get('page')
#     all_post = paginator.get_page(page_number)
#     return render(request, 'pagination/index.html', {'all_post': all_post})

###################################################################################

# class based pagination
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.views import View


class PostListView(View):
    def get(self, request):
        all_posts = Post.objects.all().order_by('id')
        paginator = Paginator(all_posts, 3)
        page_number = request.GET.get('page')
        paginated_posts = paginator.get_page(page_number)
        return render(request, 'pagination/index.html', {'all_post': paginated_posts})
