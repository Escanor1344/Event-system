from rest_framework import serializers

from mainapp.models import EventType, Event

# {"name": "Ruslan", "age": 22}


class EventSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    event_type = serializers.SlugRelatedField(slug_field='name', queryset=EventType.objects)
    info = serializers.JSONField()
    timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
