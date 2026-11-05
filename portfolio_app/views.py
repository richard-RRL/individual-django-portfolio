from django.shortcuts import render
from .models import Portfolio
from django.views.generic import ListView
from .models import Student
from django.views.generic import DetailView
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