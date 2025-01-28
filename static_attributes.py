class SomeDynamicClass:
    """
    The ``__static_attributes__`` attribute lists the attributes that are
    statically set on class instances by methods.

    https://docs.python.org/3/reference/datamodel.html#type.__static_attributes__
    """
    def __init__(self):
        self.foo = "foo"

    def set_bar(self):
        self.bar = "bar"

    def set_with_setattr(self):
        setattr(self, "with_setattr", "with_setattr")


print("SomeDynamicClass.__static_attributes__:", SomeDynamicClass.__static_attributes__)
