from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = "index.html"

    def get_queryset(self):
        queryset = Post.objects.filter(status="published").order_by("-published")
        return queryset

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(status="published").order_by("-published")
        kwargs["recent6"] = posts[:6]
        kwargs["all"] = posts[6:]

        return super().get_context_data(**kwargs)


class HotelView(ListView):
    model = Post
    template_name = "hotel.html"

    def get_queryset(self):
        queryset = Post.objects.filter(category_id=1, status="published").order_by(
            "-published"
        )
        return queryset

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(category_id=1, status="published").order_by(
            "-published"
        )
        kwargs["recent6"] = posts[:6]
        kwargs["all"] = posts[6:]

        return super().get_context_data(**kwargs)


class RestaurantView(ListView):
    model = Post
    template_name = "restaurant.html"

    def get_queryset(self):
        queryset = Post.objects.filter(category_id=2, status="published").order_by(
            "-published"
        )
        return queryset

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(category_id=2, status="published").order_by(
            "-published"
        )
        kwargs["recent6"] = posts[:6]
        kwargs["all"] = posts[6:]

        return super().get_context_data(**kwargs)


class InterviewView(ListView):
    model = Post
    template_name = "interview.html"

    def get_queryset(self):
        queryset = Post.objects.filter(category_id=3, status="published").order_by(
            "-published"
        )
        return queryset

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(category_id=3, status="published").order_by(
            "-published"
        )
        kwargs["recent6"] = posts[:6]
        kwargs["all"] = posts[6:]

        return super().get_context_data(**kwargs)


class DetailView(DetailView):
    model = Post
    template_name = "details.html"


class CreatePostView(CreateView):
    model = Post
    template_name = "create.html"
    fields = (
        "category",
        "title",
        "title_tag",
        "content",
        "author",
        "published",
        "created",
        "status",
        "image",
    )


class UpdatePostView(UpdateView):
    model = Post
    template_name = "update.html"
    fields = ["title", "category", "title_tag", "content", "image", "status"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("index")


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("details", args=[str(pk)]))

    