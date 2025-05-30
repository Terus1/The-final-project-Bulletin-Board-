from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth import logout
from django.urls import reverse_lazy

from .models import *
from .forms import PostForm, ReplyForm, AcceptReplyForm
from .filters import ReplyFilter, PostFilter

from datetime import datetime

context = {
    'page_tile': 'Simple Blog Site'
}


def logoutuser(request):
    logout(request)
    return redirect('/')


# def home(request):
#     context['page_title'] = 'Home'
#     posts = Post.objects.filter(status='Не выполнено').all()
#     context['posts'] = posts
#     return render(request, 'home.html', context)


class PostsList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # posts = Post.objects.filter(status='Не выполнено').all()
        # context['posts'] = posts

        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset

        return context


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'posts_create.html'

    def get_success_url(self):
        return reverse("posts")


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_success_url(self):
        return reverse("posts")


class PostDelete(LoginRequiredMixin ,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class ReactionList(LoginRequiredMixin ,ListView):
    model = Reply
    template_name = 'reactions.html'
    context_object_name = 'reactions'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ReplyFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_success_url(self):
        return reverse("posts")


class ReactionCreate(LoginRequiredMixin, CreateView):
    # permission_required = ('upload_app.add_reaction',)
    form_class = ReplyForm
    model = Reply
    template_name = 'reaction_create.html'
    context_object_name = 'reaction'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("post", kwargs={"pk": pk})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReactionAccept(LoginRequiredMixin, UpdateView):
    form_class = AcceptReplyForm
    model = Reply
    template_name = 'reply.html'
    success_url = reverse_lazy('reactions')


class ReactionDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'reaction_delete.html'
    success_url = reverse_lazy('reactions')



