def get_client_ip(request):
    # get client IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    return ip_address


class UserIPAddress:
    def __init__(self, get_response):
        self._get_response = get_response
    
    def __call__(self, request):
        response = self._get_response(request)

        message = {
            "ip_address": get_client_ip(request),
            "response": {
                "content": response.content
            },
            "request":{
                "method": request.method
            }
        }
        print(message)

        return response

