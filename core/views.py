from django.shortcuts import render
from django.views import View
# Create your views here.
class CoreIndex(View):
    def get(self, request):
        return render(request, 'core/index.html')