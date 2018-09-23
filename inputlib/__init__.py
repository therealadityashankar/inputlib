"""
make python inputs easier!
"""
import typing


class PInputInputNotEnteredExeception(Exception):
    pass


class PInput:
    """creates a parsable input class
    example:
    >>> import inputlib
    >>>
    >>> def foo():
    ...     print("bar :)")
    ...
    >>>
    >>> inp = inputlib.PInput()
    >>> inp.add_keyword("foo", foo)
    >>>
    >>> inp.ask()
    ::>>> foo
    bar :)
    >>>

    error example: (cotd from prev code...)
    >>> inp.ask()
    ::>>> fooi
    bad keyword: fooi
    retry

    available keywords:
    foo
    ::>>> foo
    bar :)
    >>>

    changing the input starting chars example (cotd..):
    >>> ainp = inputlib.PInput("#> ")
    >>> ainp.add_keyword("bar", foo)
    >>>
    >>> ainp.ask()
    #> bar
    bar :)
    >>>
    """
    def __init__(self, foretext="::>>> "):
        """initializes the pInput class
           see class help for an example
        """
        self.keywords = []

        # self.functions is a *dict* with
        # key: keyword, value: (function, args, kwargs)
        self.functions = {}

        self.foretext = foretext
        self.input_asked = False
        self.retrieved_input = None

    def add_keyword(self,
                    keyword: str,
                    keyword_callback: typing.Callable = None,
                    callback_args: tuple = (),
                    callback_kwargs: dict = {}):
        """adds a matchable keyword to be used when the ask function
           called
           see module help for an example
           """

        self.keywords.append(keyword)

        if keyword_callback is not None:
            self.functions[keyword] = (keyword_callback,
                                       callback_args,
                                       callback_kwargs)

    def ask(self):
        """asks for an argument
           see module class for an example
        """
        keyword = input(self.foretext)

        self.input_asked = True

        if keyword in self.keywords:
            if keyword in self.functions:
                function, args, kwargs = self.functions[keyword]
                return function(*args, **kwargs)

            else:
                return keyword
        else:
            return self.fallback(keyword)

    def fallback(self, kw):
        """fallback in case ask does not return anything"""
        print(self.fallback_text.format(kw))
        return self.ask()

    @property
    def fallback_text(self):
        """text to be displayed on fallback"""
        text = ""
        text += "bad keyword {}" + "\n"
        text += "retry" + "\n"
        text += "\n"
        text += "available functions"

        for keyword in self.functions:
            text += f'{keyword}\n'

        return text

    def get_input(self):
        """returns if user has input an input, raises an error otherwise"""
        if self.input_asked:
            return self.retrieved_input()
        else:
            raise PInputInputNotEnteredExeception()


def get_confirmation():
    """
    returns True if the user type in yes, False if the user types in No
    """
    inp = PInput("#> ")

    inp.add_keyword("yes")
    inp.add_keyword("no")

    ans = inp.get_input()

    if ans == "yes":
        return True
    else:
        return False
