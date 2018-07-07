from firstlove.helpers import file_manager
from django.db.models import F
from django.http import request

def export_to_csv(modeladmin, request, queryset):
    file_name = modeladmin.model.__name__
    return file_manager.download_as_csv(request, queryset, file_name)


def assign_members_to_self(modeladmin, request, queryset):
    queryset.update(field_name=request.user.id)


export_to_csv.short_description = 'Export to csv'
assign_members_to_self.short_description = "Assign members to myself"
