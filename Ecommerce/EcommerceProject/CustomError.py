
class MyCustomError(Exception):
 
    def __init__(self, mensagem: str ):
        self.mensagem = mensagem
 
        super().__init__(mensagem)