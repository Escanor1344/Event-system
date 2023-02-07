from django.contrib import admin
from .models import Event, EventType


class EventTypeAdmin(admin.ModelAdmin):
    """ Admin settings for model.EventType. """
    list_display = ('id', 'name', )
    list_display_links = ('name', )


class EventAdmin(admin.ModelAdmin):
    """ Admin settings for model.Event. """
    list_display = ('id', 'user', 'event_type', 'info', 'created_at', )
    list_filter = ('event_type', 'timestamp', )


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
