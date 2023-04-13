from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Music
from .forms import MusicForm
from .serializers import MusicSerializer

# Create your views here.
@api_view(['GET','POST'])
def music_list_create(request):
    if request.method == 'GET':
        # 모든 음악 리스트를 응답 (JSON 형식으로)
        all_music = Music.objects.all()  # 1. DB에서 데이터를 가져온다.
        # QuerySet으로 리턴되는 경우
        # 조회되는 데이터가 0개 이상인 경우 (many 설정 필수)
        # all(), filter()
        # 객체로 리턴되는 경우 .get() (many 설정 필요 없음)
        serializer = MusicSerializer(all_music, many=True)  # 2. 가져온 
        # serializer = MusicSerializer(instance=all_music)
        # 3. 작성된 시리얼라이져의 데이터를 응답으로 리턴한다.
        return Response(serializer.data)
    elif request.method == 'POST':  # 글 생성 로직
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


@api_view(['GET'])
def music_detail(request, music_pk):
    # music = Music.objects.get(pk=music_pk)
    music = get_object_or_404(Music, pk=music_pk)

    serializer = MusicSerializer(music)
    return Response(serializer.data)