from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from typing import *


def functionAnnotation1(request):
    str1 = func1(1, 2, 3)
    str2 = func2(-3)
    return JsonResponse(
        {"arg1": str1[0], "arg2": str1[1], "arg3": str1[2], "TrueOrFalse": str2}
    )


def func1(arg1: str, arg2: 1 + 2, arg3: "this is annotation") -> str:
    print(f"print arg1 = {arg1}")
    print(f"print arg2 = {arg2}")
    print(f"print arg3 = {arg3}")
    return arg1, arg2, arg3


def func2(arg1: int) -> bool:
    if arg1 < 0:
        return False
    return True


def exception1(request):
    return JsonResponse()


def typing1(request):
    return JsonResponse()


def call1(request):
    return JsonResponse()


def inheritance1(request):
    return JsonResponse()


def decorator1(request):
    return JsonResponse()


def orm1(request):
    return JsonResponse()


def middleware1(request):
    return JsonResponse()


def log1(request):
    return JsonResponse()
