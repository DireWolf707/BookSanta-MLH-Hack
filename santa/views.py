from django.shortcuts import render
from django.views import View

class BookView(View):
    def post(self,request):
        context = {"data_url":"https://calendly.com/book_santa?location="+request.POST.get('loc')}
        return render(request,'book.html',context=context)

class ConfirmView(View):
    def get(self,request):
        print(request.GET)
        # event_type_name
        # event_start_time - event_end_time
        # invitee_full_name
        # invitee_email
        return render(request,'confirm.html')