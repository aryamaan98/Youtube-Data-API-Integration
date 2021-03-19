import requests
from django.http import HttpResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .validations import validate_request_data
from .utils import get_videos_details_for_keyword


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET'])
def search(request):
    if request.method == 'GET':
        request_data = request.data
        print('request: %s' % request_data)

        validation_error = validate_request_data(request_data)

        if validation_error is not None:
            print('validation error: %s' % validation_error)
            return Response({'error': validation_error}, status=HTTP_400_BAD_REQUEST)

        videos_details = get_videos_details_for_keyword(
            request_data['search_keyword'])

        return Response({
            'message': 'API Hit!',
            'videos_details': videos_details
        }, status=HTTP_200_OK)