from rest_framework import renderers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny


@api_view(('GET',))
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response({
        'Version 1': reverse('api:v1:api-root', request=request, format=format)
    })

