from django.test import TestCase
from .my_utils import decorator_practice


class MyTests(TestCase):
    def test_square_should_be_return_the_squared_value(self):
        func = decorator_practice.square
        self.assertEqual(1, func(1))
        self.assertEqual(4, func(2))
        self.assertEqual(9, func(3))

    def test_square_and_func_should_be_same(self):
        func = decorator_practice.square

        self.assertEqual(decorator_practice.square(3), func(3))

    def test_pass_the_function_called_square_as_an_argument(self):
        square = decorator_practice.square
        list = [1, 2, 3]
        ans = [decorator_practice.square(item) for item in list]

        self.assertEqual(ans, decorator_practice.my_map(square, *list))

    def test_free_variable_msg_should_be_referenced_even_when_logger_function_ends(
        self,
    ):
        msg = "Hi"
        logger_func = decorator_practice.logger(msg)

        logger_func()

    def test_closure_can_make_multiple_functions_from_single_function_called_outer_func(
        self,
    ):
        single_function = decorator_practice.outer_func
        func_1 = single_function("h1")
        func_2 = single_function("p")

        self.assertEqual("<h1>h1 태그의 안<h1>", func_1("h1 태그의 안"))
        self.assertEqual("<p>p 태그의 안<p>", func_2("p 태그의 안"))
