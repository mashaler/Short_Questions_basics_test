from rest_framework import status
from rest_framework import response
from rest_framework.decorators import api_view

@api_view(["GET"])
def get_params(request):
    firstname = request.GET.get("firstname", "")
    surname = request.GET.get("surname", "")
    content = {
        "firstname": firstname,
        "surname": surname
    }
    return response.Response(content, status=status.HTTP_200_OK)
 