from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class TaskView(View):
    # For web form, to create task
    def get(self, request):
        return render(
            request=request,
            template_name='create_task.html'
        )
    def post(self, request):# CREATE Task as AJAX Request
        pass