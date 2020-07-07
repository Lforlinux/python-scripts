#This is custom error raising
class Mycustomerror(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


raise Mycustomerror('error by custome method', 500)