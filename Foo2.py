"""
Python class
============
"""

class Foo2:
    """Docstring for class Foo. Seems that it cannot have a title?"""

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5   #: Doc comment for Foo.flox. One line only.

    baz = 2
    """Docstring for class attribute Foo.baz."""

    def __init__(self):
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""
    
    def test1(self, bar):
        """A test function"""
        self.bar = bar