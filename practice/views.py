from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from typing import *


def function_annotation_1(request):
    str1 = func_1(1, 2, 3)
    str2 = func_2(-3)
    return JsonResponse(
        {"arg1": str1[0], "arg2": str1[1], "arg3": str1[2], "TrueOrFalse": str2}
    )


def func_1(arg1: str, arg2: 1 + 2, arg3: "this is annotation") -> str:
    print(f"print arg1 = {arg1}")
    print(f"print arg2 = {arg2}")
    print(f"print arg3 = {arg3}")
    return arg1, arg2, arg3


def func_2(arg1: int) -> bool:
    if arg1 < 0:
        return False
    return True


def exception_1(request):
    return JsonResponse()


def typing_1(request):
    return JsonResponse()


def call_1(request):
    return JsonResponse()


def inheritance_1(request):
    return JsonResponse()


def decorator_1(request):
    return JsonResponse()


def orm_1(request):
    return JsonResponse()


def middleware_1(request):
    return JsonResponse()


def log_1(request):
    return JsonResponse()
