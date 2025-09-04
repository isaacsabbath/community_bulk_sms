from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Leader, Message
from .services import send_sms
from django.views.decorators.csrf import csrf_exempt


def send_message_view(request):
    if request.method == "POST":
        content = request.POST.get("content")
        recipients = list(Leader.objects.values_list("phone_number", flat=True))
        
        if recipients:
            result = send_sms(content, recipients)
            if result["status"] == "success":
                msg = Message.objects.create(content=content)
                msg.sent_to.set(Leader.objects.all())
                messages.success(request, "Message sent successfully to all Residents!")
            else:
                messages.error(request, f"Failed: {result['message']}")
        else:
            messages.warning(request, "No leaders registered.")
        
        return redirect("send_message")

    return render(request, "send_message.html")


# views.py
from django.http import HttpResponse


# views.py
@csrf_exempt
def delivery_report_view(request):
    if request.method == "POST":
        print("✅ Headers:", request.headers)
        print("✅ POST data:", request.POST)
        print("✅ Raw body:", request.body.decode("utf-8", errors="ignore"))

        return HttpResponse("OK", status=200)
    else:
        return HttpResponse("Only POST allowed", status=405)