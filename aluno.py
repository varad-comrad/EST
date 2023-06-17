from typing import Union,Optional
from functools import total_ordering

@total_ordering
class Aluno:
    def __init__(self, nome: str, numero: Union[int,str],
                    prioridade: int,
                    tucmd: Optional[str] = None,
                    baixado: Optional[str] = None,
                    descanso: Optional[str] = None,
                    troca: Optional[str] = None) -> None:
        self.__nome: str = nome
        if numero:
            self.__numero: int = int(numero)
        else:
            self.__numero = 0
        self.__tucmd: bool = bool(tucmd)
        self.__baixado: bool = bool(baixado)
        self.__descanso: bool = bool(descanso)
        self.__troca: str | None = troca
        self.__prioridade: int = int(prioridade) 
        
    def __str__(self) -> str:
        return self.__nome
    
    def __eq__(self, __value) -> bool:
        return (self.prioridade, self.nome) == (__value.prioridade, __value.nome)
    
    def __lt__(self, __value) -> bool:
        return (self.prioridade, self.nome) < (__value.prioridade, __value.nome)
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def numero(self) -> int:
        return self.__numero
    
    @property
    def tucmd(self) -> bool:
        return self.__tucmd
    
    @property
    def baixado(self) -> bool:
        return self.__baixado
    
    @property
    def troca(self) -> str | None:
        return self.__troca
    
    @property
    def descanso(self) -> bool:
        return self.__descanso
    
    @property
    def prioridade(self) -> int:
        return self.__prioridade
    
if __name__ == '__main__':
    from List import List
    a1 = Aluno('a1','21064',1) 
    a2 = Aluno('a2','22064',2)
    a3 = Aluno('a4','22064',4)
    a4 = Aluno('a3','22064',3)
    l = List([a1,a2,a3,a4])
    l.sort(reverse=True)
    print([i.nome for i in l])
    # print((3,11) > (2,12))