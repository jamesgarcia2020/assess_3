from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Widget
# Create your views here.


def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})


class WidgetCreate(CreateView):
  model = Widget
  fields = "__all__"

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'

class WidgetUpdate(UpdateView):
    model = Widget
    fields = "__all__"