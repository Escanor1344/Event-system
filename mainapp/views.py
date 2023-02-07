from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Event, EventType
from .serializers import EventSerializer


class EventView(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        # If JSON length > expected --> response with warning.
        expected_keys = ['event_type', 'info', 'timestamp']
        if len(request.data.keys()) > len(expected_keys):
            return Response({'detail': 'You need to send data only with such keys: ' + str(expected_keys)})
        # Check if 'event_type' field is already in model.EventType.
        # If not --> add. Then create Event object with it.
        if EventType.objects.filter(name=request.data['event_type']).exists() is False:
            EventType(name=request.data['event_type']).save()
        return self.create(request, *args, **kwargs)
