from django.shortcuts import render
from .models import Portfolio, Student
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.

def index(request):
    # return render(request, 'portfolio_app/index.html')
    # Retrieve active portfolios
    active_portfolios = Portfolio.objects.filter(
        is_active = True
    )
    return render(
        request,
        'portfolio_app/index.html',
        {'active_portfolios': active_portfolios}
    )

class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'portfolio'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'major']
    template_name = 'portfolio_app/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'major']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('student-detail', kwargs={'pk': self.object.pk})
