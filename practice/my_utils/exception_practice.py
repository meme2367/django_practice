def exception_1(arg1: int) -> int:
    try:
        is_positive_number = func(arg1)
        if not is_positive_number:
            print(f"{arg1} is negative number")
            raise my_exception
    except Exception as e:
        print(e)
    else:
        print("예외가 발생하지 않았습니다.")
    return arg1


def func(arg1: int) -> bool:
    return arg1 >= 0


class Myexception(Exception):
    def __init__(self):
        super().__init__("Exception을 상속받은 내가 만든 예외입니다.")
