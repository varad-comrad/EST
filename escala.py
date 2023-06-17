from enum import Enum
import csv
from aluno import Aluno
from List import List
from error import ElementNotFoundError
from datetime import date, timedelta # now() and weekday()
import pandas as pd

class Posto(Enum):
    PLANTAO = 1
    CABO_DE_DIA = 2
    SARGENTO_DE_DIA = 3
    SENTINELA = 4
    CABO_DA_GUARDA = 5
    COMANDANTE_DA_GUARDA = 6
    ADJUNTO_DA_GUARDA = 7
    AUXILIAR_OF_DIA = 8
    PERMANENCIA = 9

class TipoEscala(Enum):
    VERMELHA = 1
    PRETA = 2

DEFAULT_VALUES: dict = {
    Posto.PLANTAO: 3,
    Posto.CABO_DE_DIA: 2,
    Posto.SARGENTO_DE_DIA: 2,
    Posto.SENTINELA: 6,
    Posto.CABO_DA_GUARDA: 1,
    Posto.COMANDANTE_DA_GUARDA: 1,
    Posto.ADJUNTO_DA_GUARDA: 1,
    Posto.AUXILIAR_OF_DIA: 1,
    Posto.PERMANENCIA: 1
}

class GeradorEscala:
    def __init__(self, filepath: str = '.alunos.csv') -> None:
        self.__lista = List([])
        # TODO: Implement a writing-from-xlsx method to generate the .alunos.csv file
        with open(filepath) as alunos:
            spam = csv.reader(alunos,delimiter=',')
            for line in spam:
                self.__lista.append(Aluno(*line))
        self.__default_values = DEFAULT_VALUES.copy()
        self.ler_ultimo_escalado()

    def __str__(self) -> str:
        # Use dataframe.__str__()
        return '\n'.join([f'{aux.nome} {aux.prioridade}' for aux in self.lista])
    
    def __repr__(self) -> str:
        return '\n'.join([aux.nome for aux in self.lista])

    @property
    def lista(self) -> list:
        return self.__lista

    @property
    def default_values(self) -> dict: #! name to be changed
        return self.__default_values

    @property
    def first_to_go(self) -> int: #! name to be changed
        return self.__first_to_go

    def gerar_escala(self, dias: int, posto: list[Posto], data_inicial: date | None = None) -> list[list[Aluno]]:
        aux: list[list[Aluno]] = []
        if data_inicial is None:
            data_inicial = date.today()
        for _ in range(dias):
            print([i.nome for i in self.__gerar_unico_dia_cpp([Posto.CABO_DE_DIA], data_inicial)])
            # aux.append(self.__gerar_unico_dia_cpp(posto, data_inicial))
            # data_inicial += timedelta(days=1)
        return []

    def __gerar_unico_dia_cpp(self, post: list[Posto], data: date) -> list[Aluno]:
        match post[0]:
            case CABO_DE_DIA:
                self.__first_to_go += self.default_values[CABO_DE_DIA]
                return self.lista[self.__first_to_go - self.default_values[CABO_DE_DIA]: self.__first_to_go]

    def find(self, aluno: str) -> Aluno:
        for element in self.lista:
            if element.nome == aluno:
                return element
        else:
            raise ElementNotFoundError("Aluno não existente")

    def sort_priority(self) -> None:
        self.lista.sort(reverse=True)

    def append(self,new: Aluno) -> None:
        if isinstance(new,Aluno):
            self.lista.append(new)
        else:
            raise TypeError("Tipo de dado inválido")

    def ler_ultimo_escalado(self) -> int:
        aux_flag: bool = True
        for i, element in enumerate(self.lista):
            if element.descanso and aux_flag:
                aux_flag = False
            elif not element.descanso and not aux_flag:
                self.__first_to_go = i
                return i
        else:
            raise ElementNotFoundError


if __name__ == '__main__':
    esc = GeradorEscala()
    esc.sort_priority()
    # esc.gerar_escala()
    print(esc)
    esc.gerar_escala(1, [Posto.CABO_DE_DIA])
    # print([aux.troca for aux in esc.lista])
