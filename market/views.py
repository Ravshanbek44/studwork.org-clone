from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from question.permissions import IsOwnerOrReadOnly
from .models import Market, MarketFileDemo, MarketFileDone
from .serializers import MarketFileDoneSerializer, MarketFileDemoSerializer, MarketSerializer, MarketListSerializer
from rest_framework.permissions import IsAuthenticated

class MarketListAPIView(generics.ListAPIView):
    serializer_class = MarketListSerializer

    def get_queryset(self):
        queryset = Market.objects.all()
        is_top = self.request.GET.get('is_top')
        views = self.request.GET.get('popular')
        if is_top:
            queryset = queryset.filter(is_top=True)
        if views:
            queryset = queryset.order_by('-views')
        return queryset


class MarketDetailAPIView(generics.RetrieveAPIView):
    serializer_class = MarketListSerializer
    queryset = Market.objects.all()


class MarketDeleteAPIView(generics.DestroyAPIView):
    serializer_class = MarketListSerializer
    queryset = Market.objects.all()
    permission_classes = IsOwnerOrReadOnly
    authentication_classes = [TokenAuthentication]


class MarketUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MarketListSerializer
    queryset = Market.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]


class MarketCreateAPIView(generics.CreateAPIView):
    serializer_class = MarketSerializer
    queryset = Market.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MarketFileDemoCreateAPIView(generics.CreateAPIView):
    serializer_class = MarketFileDemoSerializer
    queryset = MarketFileDemo.objects.all()


class MarketFileDoneCreateAPIView(generics.CreateAPIView):
    serializer_class = MarketFileDoneSerializer
    queryset = MarketFileDone.objects.all()


class MarketCreateView(generics.CreateAPIView):
    serializer_class = MarketListSerializer
    queryset = Market.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

