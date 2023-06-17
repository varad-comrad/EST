class ElementNotFoundError(Exception):
    def __init__(self, message='') -> None:
        msg=f'Elemento não encontrado'
        super(ElementNotFoundError,self).__init__(message or msg)


if __name__ == '__main__':
    pass