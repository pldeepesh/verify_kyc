from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


@api_view(['GET', 'POST'])
def do_get_pan_data(request):
    if request.method == "POST":
        return Response(json.dumps({'status': 200, 'message': 'Success'}))
    elif request.method == "GET":
        return Response(json.dumps({'status': 200, 'message': 'Success'}))
