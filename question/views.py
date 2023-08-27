from rest_framework import generics
from .serializers import QuestionSerializer, QuestionListSerializer, AnswerSerializer
from .models import Question, Answer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionListSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        answer = self.request.GET.get('is_answered')
        views = self.request.GET.get('views')
        if answer:
            queryset = queryset.filter(is_answered=True)
        if views:
            queryset = queryset.order_by('-views')
        return queryset


class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    lookup_field = 'pk'


class QuestionUpdateAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'pk'


class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'pk'


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class AnswerListAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetailAPIView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'pk'


class AnswerUpdateAPIView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'pk'
