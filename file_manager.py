import csv
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied


def download_as_csv(request, queryset, filename="export"):
    if not request.user.is_staff:
        raise PermissionDenied

    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type='text/csv')

	# force download.
    response['Content-Disposition'] = 'attachment;filename=%s.csv' % filename
	# the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields if field.name != "id"]
    field_headers = [x.title().replace("_", " ") for x in field_names ]

	# Write a first row with header information
    writer.writerow(field_headers)


    for obj in queryset:
	    writer.writerow([getattr(obj, field) for field in field_names if field != "id"])

    return response


