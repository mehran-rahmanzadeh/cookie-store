from django.contrib import admin
from django.contrib.sessions.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _user_data(self, obj):
        instance = obj.get_decoded().get('demo.models.User', None)
        if instance:
            return f'First name: {instance.first_name}, Last name: {instance.last_name}, Phone number: {instance.phone_number}, Email: {instance.email}, Birth date: {instance.birth_date}, Mass: {instance.mass}, Height: {instance.height}'
        return None

    list_display = ['session_key', '_user_data', 'expire_date']
