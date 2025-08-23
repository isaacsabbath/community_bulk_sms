from django.contrib import admin
from .models import Leader, Message

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")
    search_fields = ("name", "phone_number")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at")
    filter_horizontal = ("sent_to",)
