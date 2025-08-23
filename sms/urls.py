from django.urls import path
from . import views

urlpatterns = [
    path("send/", views.send_message_view, name="send_message"), 
    path("delivery/", views.delivery_report_view, name="delivery_report"),  # 👈 new one

]
