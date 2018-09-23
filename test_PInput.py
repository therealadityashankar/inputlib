import inputlib


def mock_input(ret_val, assert_rule=None):
    """overrides the input function to mock it!,
       assert_rule checks if """
    def _input(input_foretext):
        if assert_rule is not None:
            assert assert_rule == input_foretext
        return ret_val
    return _input


def mock_function_foo(arg1=1, arg2=2):
    """mock function for testing"""
    return (arg1, arg2)


class TestClass:

    def test_PInput_1(self):
        """basic test"""
        inp = inputlib.PInput()
        inp.add_keyword("mock_inp_1", mock_function_foo)
        inputlib.input = mock_input("mock_inp_1")
        assert inp.ask() == (1, 2)

    def test_PInput_2(self):
        """PInput parameter check"""
        inp = inputlib.PInput(")>")
        inp.add_keyword("mock_inp_1", mock_function_foo)
        inputlib.input = mock_input("mock_inp_1", ")>")
        assert inp.ask() == (1, 2)

    def teardown_method(self):
        inputlib.input = input
        print("toredown")
