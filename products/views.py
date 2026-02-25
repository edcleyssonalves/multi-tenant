from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, permissions


class ProductListView(LoginRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return models.Product.objects.filter(
            user=self.request.user
        )


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProductDetailView(LoginRequiredMixin, permissions.UserIsOwnerMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'


class ProductUpdateView(LoginRequiredMixin, permissions.UserIsOwnerMixin, UpdateView):
    pass


class ProductDeleteView(LoginRequiredMixin, permissions.UserIsOwnerMixin, DeleteView):
    pass