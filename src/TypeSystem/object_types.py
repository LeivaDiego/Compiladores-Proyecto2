class ObjectType():
    """
    Base class for all object types.

    Attributes:
        - object_type: The name of the object type.
    """
    def __init__(self, name):
        self.object_type = name

    def __str__(self):
        return self.object_type
    

class VariableType(ObjectType):
    def __init__(self):
        super().__init__("variable")


class FunctionType(ObjectType):
    def __init__(self):
        super().__init__("function")


class ClassType(ObjectType):
    def __init__(self):
        super().__init__("class")