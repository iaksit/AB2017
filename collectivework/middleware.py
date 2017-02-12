#Fonksiyon olarak MiddleWare
def simple_middleware(get_response):
    # Inner function
    def middleware(request):
        #View calistirilmadan once cagirilacak kod blogu
        response = get_response(request)

        #View calistirildiktan sonra calisacak kod
        return response

    return  middleware

class SimpleMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        #tek seferlik yapılandırma parametreleri

    def __call__(self, request):
        response = self.get_response(request)
        return response