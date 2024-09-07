from portal.base import BaseAPIView
from portal.constants import POST, PUT, DELETE, GET, GETALL
from .models import Shayaries
from .serializers import ShayariesGetSerializer,ShayariesPostSerializer

class AdminSubscriptionAPIView(BaseAPIView):
    model = Shayaries
    serializer_class = ShayariesGetSerializer
    post_serializer = ShayariesPostSerializer
    allowed_methods = [GET, GETALL, POST, PUT, DELETE]
    lookup_field = 'id'
    order = '-created_on'
    related_models = None