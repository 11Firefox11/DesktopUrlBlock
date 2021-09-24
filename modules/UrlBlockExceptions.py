class DefaultUrlBlockException(Exception):
    def __init__(self, object, objecttype="object", message=f"object error", errorname="UrlBlockError"):
        self.objecttype = objecttype
        self.object = object
        self.message = message
        self.errorname = errorname
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.errorname}: {self.objecttype}: '{self.object}' -> {self.message}."

class PermissionNotGranted(DefaultUrlBlockException):
    def __init__(self, path, objecttype="host file", message="Permission did not granted, can't access the host file"):
        super().__init__(path, objecttype=objecttype, message=message, errorname=self.__class__.__name__)
class DoesNotExists(DefaultUrlBlockException):
    def __init__(self, o, objecttype, message):
        super().__init__(o, objecttype=objecttype, message=message, errorname=self.__class__.__name__)

class AlreadyExists(DefaultUrlBlockException):
    def __init__(self, o, objecttype, message):
        super().__init__(o, objecttype=objecttype, message=message, errorname=self.__class__.__name__)