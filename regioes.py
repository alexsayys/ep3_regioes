# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
# ------------------------------------------------------------------

'''

    Nome: Alex Dos Santos Nascimento
    NUSP: 14612990

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

import numpy as np


#########################################################################
#
# Classe Regioes
#

class Regioes:
    '''
    Estrutura que organiza o algoritmo recursivo de construção
    de regiões conexas de uma imagem representada por um ndarray. 
    '''

    # ------------------------------------------------------------
    def __init__(self, img):
        ''' (Regioes, array) -> None
        O construtor de Regioes cria as estruturas para segmentar as 
        regiões conexas de cada pixel de img. Você pode incluir
        outros atributos caso desejar.
        '''
        self.regioes = []
        self.img = img

    # ------------------------------------------------------------
    def __str__(self):
        ''' (Regioes) -> str
        Retorna uma string com as regiões numeradas.

        Exemplo:
        0: [(0,0), (0,1)]
        1: [(1,0), (1,1)]

        Esse método já está pronto, você não deve alterá-lo.
        '''
        retorno = ""
        for i in range(len(self.regioes)):
            lista = self.regioes[i]
            retorno += "%d: %s\n" % (i, str(lista))

        return retorno

    # ------------------------------------------------------------
    def segmente_regiao(self, lin, col, indice):
        ''' (Regioes, int, int, int) -> None
        Marca o pixel como visitado e visita os vizinhos de mesma cor que ainda não
        tenham sido segmentados. Considere conectividade 4.
        '''
        elemento = self.img[lin, col]
        self.img[lin, col] = -1  # Marca o pixel como visitado, mudando seu valor para -1
        indice.append((lin, col))  # Adiciona a posição à variável regiao

        # Verifica os elementos vizinhos (conexão 4)
        vizinhos = [(lin - 1, col), (lin + 1, col), (lin, col - 1), (lin, col + 1)]

        for vizin in vizinhos:
            l, c = vizin
            if (0 <= l < self.img.shape[0] and 0 <= c < self.img.shape[1]  # verifica se l e c estão na dimensão da matriz
                    and self.img[l, c] == elemento  # verifica o valor do elemento
                    and not self.pixel_visitado(l, c)):

                # Usa a recursividade para verificar os vizinhos
                self.segmente_regiao(l, c, indice)


    # ------------------------------------------------------------
    def segmente(self):
        ''' (Regioes) -> None
        Percorre a imagem em self.img e monta a lista com todas as regioes
        conexas por 4 em self.regioes.
        '''
        # for valor in self.valor_unico:
        for i in range(len(self.img)):
            for j in range(len(self.img[0])):
                if not self.pixel_visitado(i, j):
                    regiao = []
                    self.regioes.append(regiao)
                    self.segmente_regiao(i, j, regiao)

    def pixel_visitado(self, lin, col):
        '''
        :param lin: int
        :param col: int
        :return: bool
        Verifica se o pixel foi visitado e retorna True ou False
        '''
        return self.img[lin, col] == -1

#########################################################################
#
#   FUNÇÕES
#
#########################################################################


def pinte_regioes(reg, palete):
    ''' (Regioes, list) -> imagem (ndarray)

    Recebe um objeto do tipo Regioes e uma lista de cores e cria e 
    retorna uma nova imagem (ndarray) com as regiões coloridas com 
    as cores da palete (uma lista de cores). 
    
    Sua função deve varrer a lista de regiões e pintar os pixeis 
    dessa região com a cor correspondente da palete. Ou seja, a 
    primeira região é pintada com a primeira cor, a segunda região 
    com a segunda cor, etc. 
    
    No entanto, o número de cores não precisa ser o mesmo número 
    de regiões. Nesse caso, considere que a palete é uma lista 
    circular, ou seja, se n é o tamanho da palete, ao chegar ao 
    final da palete (índice n-1), a próxima cor a ser usada está 
    no índice 0 da palete.
    '''

    # Criar uma cópia da matriz original para pintar
    imagem_p = np.copy(reg.img)

    # for i, regiao in enumerate(reg.regioes):
    #     indice = (indice + 1) % len(palete)
    #     cor = palete[indice]
    #     for pixel in regiao:
    #         lin, col = pixel
    #         imagem_pintada[lin, :] = cor

    # for linha, regiao in zip(imagem_pintada, reg.regioes):
    #     # Selecionar a cor da palete usando aritmética modular
    #     cor = palete[len(regiao) % len(palete)]
    #
    #     # Pintar toda a linha da matriz com a cor correspondente
    #     linha[:] = cor

    for i, regiao in enumerate(reg.regioes):
        cor = i % len(palete)
        for pixel in regiao:
            lin, col = pixel
            imagem_p[lin, col] = cor

    return imagem_p



#########################################################################
def pause():
    '''
    '''
    input(">>> Aperte 'enter' para continuar...")


EXEMPLO = [
    [1, 8, 7, 3, 3, 3],
    [1, 8, 1, 1, 1, 3],
    [1, 2, 2, 1, 3, 3],
    [1, 1, 1, 1, 2, 3],
    [9, 9, 1, 2, 1, 1],
    [9, 9, 9, 2, 1, 0],
]

if __name__ == "__main__":
    img = np.array(EXEMPLO)
    lins, cols = img.shape

    print(f"Carreguei a image que tem {lins} linhas e {cols} colunas")
    print("Imagem:\n", img)
    pause()

    # Carregas as regiões e imprime
    reg = Regioes(img)
    reg.segmente()
    print(f"Regiões:\n {reg}")


    # testes da função pinte_regioes
    # Palete de cores
    palete_cores = [0, 128, 255]  # Tons de cinza

    # Pintar as regiões
    imagem_pintada = pinte_regioes(reg, palete_cores)

    # Mostrar a imagem pintada
    print(imagem_pintada)
    # coloque seus testes aqui
