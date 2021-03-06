from django.contrib import admin

from .models import Meetup, Location, Participant


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}


class MeetupAdminLocation(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('name',)


admin.site.register(Meetup, MeetupAdmin, )
admin.site.register(Location, MeetupAdminLocation)
admin.site.register(Participant)
