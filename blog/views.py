from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView)
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def hello(request):
    return HttpResponse('Olá Mundo!')


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    # context_object_name = 'custom'   # default: object


class BlogCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_new.html'
    success_message = '%(field)s: Criado com Sucesso!'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_message = '%(field)s: Alterado com Sucesso!'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )


class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = 'Removido com Sucesso!'   #'%(field)s: Removido com Sucesso!'

    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #         field=self.object.title,
    #     )
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)