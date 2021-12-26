from django.urls import path
from django.views.generic import TemplateView
from .views import BookView,ConfirmView

urlpatterns = [
    path('book', BookView.as_view(),name='book'),
    path('', TemplateView.as_view(template_name='map.html'),name='map'),
    path('confirmed/', ConfirmView.as_view(),name='confirm'),
]