from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from . import forms


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')