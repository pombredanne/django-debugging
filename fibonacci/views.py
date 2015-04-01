from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
import requests

def fibonaci_view(request, num):
    """
    http://localhost:8123/fibonacci/2
    """

    if request.method == 'GET':
        requestB = request.GET
        r = requests.get
    elif request.method == 'POST':
        requestB = request.POST
        r = requests.post
    else:
        return HttpResponseNotAllowed("Permitted methods are POST and GET")
    params = requestB.dict()

    if num < 3:
        response1 = response2 = 1
        return HttpResponse(2, content_type="text/plain")
    else:
        try:
            url1 = 'http://localhost:8123/fibonacci/%s' % (num - 1)
            url2 = 'http://localhost:8123/fibonacci/%s' % (num - 2)
            response1 = r(url1, params=params)
            response2 = r(url2, params=params)
        except requests.exceptions.ConnectionError as e:
            if e.message.args[1][0] == 111:
                return HttpResponse('Connection is refused. Server must be off.', status=500)

    response = int(response1.text) + int(response2.text)
    return HttpResponse(response, status=int(response1.status_code), content_type=response1.headers['content-type'])
