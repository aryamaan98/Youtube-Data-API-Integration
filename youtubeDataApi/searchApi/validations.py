def validate_request_data(data):
    if not data.get('search_keyword'):
        return 'search keyword not found'
    return None