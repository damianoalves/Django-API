from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None and len(response.data) == 1:
        if 'detail' in response.data:
            response.data['code'] = response.data['detail'].code
        response.data['status_code'] = int(response.status_code)
    return response


ACTION_PERMISSION_DENIED = 'This user do not has permission to perform this action.'


class ObjectNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Object not found.'
    default_code = 'object_not_found'


class RequestBodyNotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'The body of this request is not found.'
    default_code = 'request_body_not_found'


class ViewPermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = ACTION_PERMISSION_DENIED
    default_code = 'view_permission_denied'


class CreatePermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = ACTION_PERMISSION_DENIED
    default_code = 'create_permission_denied'


class UpdatePermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = ACTION_PERMISSION_DENIED
    default_code = 'update_permission_denied'


class DestroyPermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = ACTION_PERMISSION_DENIED
    default_code = 'destroy_permission_denied'


class InvalidContentType(APIException):
    status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    default_detail = "Invalid Content Type"
    default_code = 'invalid_content_type'


class EmailVerificationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'E-mail is not verified. Verification E-mail will be resubmitted.'
    default_code = 'email_verification_failed'
