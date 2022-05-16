from typing import List, Dict, Set, Union, Callable, Tuple, Optional


def typing_1():
    list_nums: List[int] = [1, 2, 3]

    dict_countries: Dict[str, str] = {"KR": "South Korea", "US": "United States"}

    set_alphabets: Set[int] = {1, 2, 3, 4, 3}

    tuple_user: Tuple[int] = (1, 2, 3)

    union_num1: Union[int, float] = 3.0
    union_num2: Union[int, float] = 3

    print(union_num1)
    print(union_num2)

    print(union_typing(2.0))
    print(union_typing(2))

    print(optional_typing("message1"))
    print(optional_typing("message2", 3))


def union_typing(num: Union[int, float]) -> str:
    return str(num)


def optional_typing(msg: str, times: Optional[int] = None) -> list:
    if times is None:
        return list(msg)
    return list(msg) * times


def print_name(name: str) -> str:
    return "내 이름은 " + name + "!"


def callable_typing(func: Callable[[str], str], name: str, times: int = 1):
    for i in range(times):
        print(func(name))


def make_name_list(*args) -> list:
    res = list()
    for item in args:
        res.append(item)
    return res


def callable_typing_using_ellipsis(func: Callable[..., list], *args, times: int = 1):
    for i in range(times):
        print(func(args))


def test_callable_typing():
    callable_typing(print_name, "다연")
    callable_typing(print_name, "구우", 3)

    args = ["다연", "구우"]
    callable_typing_using_ellipsis(make_name_list, args)
    callable_typing_using_ellipsis(make_name_list, args, times=3)
