from django_filters import FilterSet, ModelChoiceFilter

from .models import Reply, Post


class ReplyFilter(FilterSet):
    post = ModelChoiceFilter(
        field_name='post__title',
        queryset=Post.objects.all(),
        label='Пост',
        empty_label='Все посты'
    )

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(author=self.request.user)
        else:
            return qs

            # class Meta:
    #     model = Reply
    #     fields = {
    #         'post__title': ['icontains'],
    #     }


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }