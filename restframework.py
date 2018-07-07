from rest_framework import serializers

def get_slug_related_field(field_name='name'):
    return serializers.SlugRelatedField(
        many=True, read_only=True, slug_field=field_name)
