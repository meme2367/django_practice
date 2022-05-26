def square(x: int) -> int:
    return x * x


def my_map(func, *args) -> list:
    return [func(item) for item in args]


def first_class_func_1() -> None:
    func = square
    print(square(3))
    print(func(3))

    print(my_map(func, 1, 2, 3))


def logger(msg: str):
    def log_message() -> None:
        print("log_message : ", msg)

    return log_message


def outer_func(tag: str):
    tag = tag

    def inner_func(content: str) -> None:
        print("<{0}>{1}<{0}>".format(tag, content))

    return inner_func


def closure_1() -> None:
    log_hi = logger("Hi")
    print(log_hi)
    print(log_hi())

    h1_func = outer_func("h1")
    p_func = outer_func("p")

    h1_func("h1 태그의 안입니다")
    p_func("p 태그의 안입니다")


def decorator_outer_func(origin_func):
    def decorator_wrapper_func():
        print(f"{origin_func.__name__}함수 호출")
        return origin_func()

    return decorator_wrapper_func


def display_func_1() -> None:
    print("display_func_1함수 실행")


def display_func_2() -> None:
    print("display_func_2함수 실행")


def decorator_func_1() -> None:
    display_1 = decorator_outer_func(display_func_1)
    display_2 = decorator_outer_func(display_func_2)
    display_1()
    display_2()


def decorator_func_2() -> None:
    display()


def decorator_outer_func_2(origin_func):
    def decorator_wrapper_func():
        print(f"{origin_func.__name__}함수 호출")
        return origin_func()

    return decorator_wrapper_func


@decorator_outer_func_2
@decorator_outer_func
def display() -> None:
    print("display함수 호출")


def practice() -> None:
    first_class_func_1()
    closure_1()
    decorator_func_1()
    decorator_func_2()
