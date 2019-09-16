from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View


from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

# Create your views here. Логика отображения
def posts_list(request):                                               #функция "представление"
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):           #Создание Поста
    model_form = PostForm
    template = 'blog/post_create_form.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'



class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):            #Создание Тэга

    model_form = TagForm
    template = 'blog/tag_create.html'

class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'

class TagDelte(View):
    def get(self, requset, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(requset, 'blog/tag_delte_form.html', context={'tag':tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect()

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)        # request.POST получаем данные от пользователя
    #                                                             # через словарь POST объекта request
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()                         #создаем поправленный Tag
    #         return redirect(new_tag)                            # функция возвращает redirect на поправленный экземепляр класса Tag
    #     return render(request, 'blog/tag_update_form.html', instance=tag)

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})





# -----------------------------------------------------------------------------------------------------------------
# class PostCreate(View):
#
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'blog/post_create_form.html', context={'form': form})
#
#     def post(self, request):
#         bound_form = PostForm(request.POST)
#         if bound_form.is_valid():
#             new_post = bound_form.save()
#             return redirect(new_post)
#         return render(request, 'blog/post_create_form.html', context={'form': bound_form})

# class TagCreate(View):
#     def get(self, request):
#         form = TagForm()
#         return render(request, 'blog/tag_create.html', context={'form': form})
#
#     def post(self, request):
#         bound_form = TagForm(request.POST)
#
#         if bound_form.is_valid():
#             new_tag = bound_form.save()
#             return redirect(new_tag)
#
#         return render(request, 'blog/tag_create.html', context={'form': bound_form})
#
# -------------------------------------------------------------------------------------
# class TagUpdate(View):
#     def get(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         bound_form = TagForm(instance=tag)
#         return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})
#
#     def post(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         bound_form = TagForm(request.POST, instance=tag)        # request.POST получаем данные от пользователя
#                                                                 # через словарь POST объекта request
#         if bound_form.is_valid():
#             new_tag = bound_form.save()                         #создаем поправленный Tag
#             return redirect(new_tag)                            # функция возвращает redirect на поправленный экземепляр класса Tag
#         return render(request, 'blog/tag_update_form.html', instance=tag)