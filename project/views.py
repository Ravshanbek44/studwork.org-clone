from rest_framework.response import Response
from .models import WorkType, MyTakenWork, Work, FileWork, Comment, OtClick
from . import serializers
from rest_framework import generics, status
from question.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class WorkTypeListAPIView(generics.ListAPIView):
    queryset = WorkType.objects.all()
    serializer_class = serializers.WorkTypeSerializer


class WorkListAPIView(generics.ListAPIView):
    serializer_class = serializers.WorkListSerializer

    def get_queryset(self):
        queryset = Work.objects.all()
        return queryset


class WorkUpdateAPIView(generics.UpdateAPIView):
    queryset = Work.objects.all()
    serializer_class = serializers.WorkSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class WorkDetailAPIView(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = serializers.WorkSerializer
    lookup_field = 'pk'


class WorkDeleteAPIView(generics.DestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = serializers.WorkSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class WorkCreateAPIView(generics.CreateAPIView):
    queryset = Work.objects.all()
    serializer_class = serializers.WorkSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        try:
            file = self.request.data['files']
            for i in file:
                file = FileWork.objects.create(work_id=obj.id, file=i)
                file.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            pass
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class ClickCreateAPIView(generics.CreateAPIView):
    queryset = OtClick.objects.all()
    serializer_class = serializers.OtClickSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class OtClickListAPIView(generics.ListAPIView):
    serializer_class = serializers.OtClickSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = OtClick.objects.all()
        work = self.request.GET.get('work_id')
        user = self.request.user
        queryset = queryset.filter(work__user_id=user.id)
        if work:
            queryset = queryset.filter(work_id=work)
        return queryset


class MyWorksListAPIView(generics.ListAPIView):
    serializer_class = serializers.MyWorkSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = MyTakenWork.objects.all()
        user = self.request.user
        queryset = queryset.filter(doer=user)
        return queryset


class GiveWorkCreateAPIView(generics.CreateAPIView):
    queryset = MyTakenWork.objects.all()
    serializer_class = serializers.TakenWorkSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
