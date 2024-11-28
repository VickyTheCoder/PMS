from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(
        request=request,
        template_name='index.html'
    )

def login_page(request):
    return render(
        request=request,
        template_name='login.html'
    )

def signup_page(request):
    return render(
        request=request,
        template_name='signup.html'
    )

def dashboard_page(request):
    return render(
        request=request,
        template_name='dashboard.html'
    )