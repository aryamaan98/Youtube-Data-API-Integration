def validate_request_data(data):
    if not data.get('search_keyword'):
        return 'search keyword not found'
    return None


def validate_request_data_for_paginated_response(data):
    if data.get('page_number') and type(data['page_number']) is not int:
        return 'page number should be integer'
    if data.get('page_number') and data['page_number'] <= 0:
        return 'page number should be greater than or equal to 1'
    return None
