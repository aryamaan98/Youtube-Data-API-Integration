import requests
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .validations import validate_request_data, validate_request_data_for_paginated_response
from .utils import get_videos_details_for_keyword, get_all_videos_details
from .config import SIZE_OF_PAGE, STARTING_PAGE


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


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


@api_view(['GET'])
def get_result_from_database(request):
    if request.method == 'GET':
        request_data = request.data
        validation_error = validate_request_data_for_paginated_response(
            request_data)
        if validation_error is not None:
            print('validation error: %s' % validation_error)
            return Response({'error': validation_error}, status=HTTP_400_BAD_REQUEST)

        videos_details = get_all_videos_details()

        paginator = Paginator(videos_details, SIZE_OF_PAGE)

        required_page = None
        try:
            if request_data.get('page_number'):
                required_page = paginator.page(request_data['page_number'])
        except EmptyPage:
            required_page = paginator.page(STARTING_PAGE)

        print('Page Response: ', required_page)

        if not required_page:  # if no starting page
            return Response({
                'error': 'page not found'
            }, status=HTTP_400_BAD_REQUEST)

        return Response({
            'message': 'API Hit!',
            'videos_details': list(required_page)
        }, status=HTTP_200_OK)
