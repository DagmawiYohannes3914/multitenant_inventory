from rest_framework.views import APIView
from rest_framework.response import Response


class GatewayAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "API Gateway is working!"})
