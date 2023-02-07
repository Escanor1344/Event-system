from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Event, EventType
from .serializers import EventSerializer


class EventView(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        # Check if 'event_type' field is already in model.EventType.
        # If not --> add. Then create Event object with it.
        if EventType.objects.filter(name=request.data['event_type']).exists() is False:
            EventType(name=request.data['event_type']).save()
        return self.create(request, *args, **kwargs)
