from django.shortcuts import render
from django.views import View


class OnCallView(View):
    def get(self, request):
        return render(request, "ltc/index.html")
    
index = OnCallView.as_view()