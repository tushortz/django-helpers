from django.db.models import Q
import re


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    '''
    query = None
    terms = re.findall(r'"[^"]+"|\S+', query_string)

    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search_model(request, model, search_field, query_params={}):
    query = ''
    results = None

    results = model.objects.all()
    if ('q' in request.GET) and request.GET['q'].strip():
        query = request.GET['q'].strip()
        entry_query = get_query(query, search_field)
        results = model.objects.filter(entry_query)

    results = results.filter(**query_params)

    context = {
        'query': query,
        'results': results,
    }

    return context
