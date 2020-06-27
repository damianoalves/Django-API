from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None and len(response.data) == 1:
        if 'detail' in response.data:
            response.data['code'] = response.data['detail'].code
        response.data['status_code'] = int(response.status_code)
    return response
