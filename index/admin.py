from django.contrib import admin
from .models import Todo, DirectMessage, Alert, Conversation

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'created_on', 'note', 'status')


class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'receiver', 'status', 'body', 'created_on')
    search_fields = ('author', 'receiver')


class AlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'note', 'status', 'created_on')


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user_1', 'user_2')


admin.site.register(Todo, TodoAdmin)
admin.site.register(DirectMessage, DirectMessageAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Conversation, ConversationAdmin)
