from django.views import generic
from django.urls import reverse_lazy
from . import models


# Create your views here.
class BooksListView(generic.ListView):
    model = models.Book
    context_object_name = 'book_list'


class AddBookView(generic.CreateView):
    model = models.Book
    fields = "__all__"
    success_url = reverse_lazy('admin_app:adminhome')


class UpdateView(generic.UpdateView):
    form_class = models.Book
    fields = '__all__'
    success_url = reverse_lazy('admin_app:adminhome')


class BookDeleteView(generic.DeleteView):
    model = models.Book
    success_url = reverse_lazy("admin_app:adminhome")


class UpdateView(generic.UpdateView):
    model = models.Book
    fields = '__all__'
    success_url = reverse_lazy('admin_app:adminhome')


