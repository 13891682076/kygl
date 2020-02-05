from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView



User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    # pk_url_kwarg = 'pk'
    template_name = 'users/user_detail.html'
    # context_object_name = 'object' or 'user'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView,self).get_context_data()

        return context


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["nickname", "job", "introduction", "avatar", "address", "birthday",
              "personal_url", "weibo", "zhihu", "github", "linkedin"]
    template_name = 'users/user_form.html'

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)
        # return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

# resole :正向解析
# reverse: 反向解析
