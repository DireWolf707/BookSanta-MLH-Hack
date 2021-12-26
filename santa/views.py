from django.shortcuts import render
from django.views import View
from datetime import datetime

class BookView(View):
    def post(self,request):
        context = {"data_url":"https://calendly.com/book_santa?location="+request.POST.get('loc')}
        return render(request,'book.html',context=context)

class ConfirmView(View):
    def get(self,request):
        date = datetime.fromisoformat(request.GET.get("event_start_time"))
        context = dict()
        context['type']=request.GET.get("event_type_name")
        context['date']=date
        context['name']=request.GET.get("invitee_full_name")
        return render(request,'confirm.html',context=context)