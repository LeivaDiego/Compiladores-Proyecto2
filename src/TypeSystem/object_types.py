class ObjectType():
    """
    Base class for all object types.

    Attributes:
        - object_type: The name of the object type.
    """
    def __init__(self, name):
        self.object_type = name
        self.id = None

    def __str__(self):
        return self.object_type
    

class VariableType(ObjectType):
    def __init__(self):
        super().__init__("variable")
        self.data_type = None
        self.initialized = False
        self.class_instance = False
        self.function_instance = False


class FunctionType(ObjectType):
    def __init__(self):
        super().__init__("function")
        self.return_type = None
        self.parameters = []
        self.is_anon = False


class ClassType(ObjectType):
    def __init__(self):
        super().__init__("class")
        self.parent = None
        self.attributes = []
        self.methods = []