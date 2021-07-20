from django.shortcuts import render
from django.http import HttpResponse

# 여기에 보기를 만듭니다.
def index(request):
    return HttpResponse("헬로 월드")
