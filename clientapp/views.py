from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from adminapp.models import Book
from django.contrib.auth.models import User
from . import forms


# Create your views here.
class Index(generic.ListView):
    template_name = "clientapp/index.html"
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.all()


def registerView(request):
    form = forms.UserRegistrationForm(request.POST)
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)         # create form with user input data
        user = form.save()
        user.set_password(user.password)
        user.save()
        print('User saved')
        return HttpResponseRedirect(reverse('client_app:login'))
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'clientapp/register.html', {'form': form })


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('client_app:indexpage'))
        else:
            print("They used username: {} and password: {}".format(username, password))
            failed =True
            return render(request, 'clientapp/login.html',{'failed':failed})
            return HttpResponse("Invalid login credentials")
    else:
        return render(request,'clientapp/login.html')

@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('client_app:indexpage'))

class SingleProduct(generic.DetailView):
    model = Book
    template_name = 'clientapp/book_detail.html'


def profileView(request,pk):
    user = User.objects.get(pk=pk)
    print(user)
    form = forms.UserRegistrationForm(user)
    return render(request, 'clientapp/account.html', {'user':user})

        # pk = self.kwargs.get('pk')
        # if 'personalForm' not in context:
        #     context['personalForm'] = self.form_class(request=self.request)
        #     return get_object_or_404(User.objects.all(), pk=pk)
        # if 'addressForm' not in context:
        #     context['personalForm'] = self.second_form_class(request=self.request)
        # return context


    # def get(self, request, *args, **kwargs):
    #     personalInfoForm = UserInfoForm
    #     addressForm = UserAddressForm
    #
    #     context = self.get_context_data(**kwargs)
    #     context['personalInfoForm'] = personalInfoForm
    #     context['addressForm'] = addressForm
    #
    #     if 'personalForm' in request.POST:
    #         object = UserInfo.objects.get(id=self.kwargs['pk'])
    #         print('Found')
    #         form = UserInfoForm(request.POST)
    #         if form.is_valid():
    #             print('Valid')
    #
    #     return self.render_to_response(context)

