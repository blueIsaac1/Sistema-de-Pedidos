class ConfirmEmail(Exception):
    def __init__(self, message = "E-mail ja cadastrado"):
        super().__init__(message)