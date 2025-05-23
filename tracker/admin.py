from django.contrib import admin
from .models import Activity

# Register your models here.


class ActivityAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "event_type", "timestamp"]
    list_filter = ("event_type",)
    search_fields = ("user__username",)
    ordering = ("-timestamp",)


admin.site.register(Activity, ActivityAdmin)
