## TORNEIO 1

"""

Defina uma função que, dada uma lista de strings, retorne
essa lista ordenada por ordem decrescente do número de 
caracteres diferentes nela contidos.
Caso duas strings tenham o mesmo número de caracteres
diferentes a mais pequena em ordem lexicográfica deve
aparecer primeiro na lista retornada.

"""

## 90%

def diferentes(frases):
    dic = {}
    for x in frases :
        letras = []
        contador = 0
        for l in x :
            if l not in letras:
                contador += 1
                letras.append(l)
        dic[x] = (len(letras))
    lista = [(x,y) for x,y in dic.items()]
    lista.sort(key = lambda x:x[0])
    lista.sort(key = lambda x:x[1],reverse = True)
    ret =  [x[0] for x in lista]
    return ret

"""

Implemente uma função que, dada uma lista com registos de instantes de tempo e nome de piloto, 
descrevendo os tempos de passagem pela meta dos varios pilotos numa corrida de F1, 
devolva a lista com os nomes dos pilotos com a volta mais rápida ordenada por ordem alfabética. 
Assuma que todos os pilotos iniciaram a prova no instante 0.

"""

## 90%

def formula1(log):
    dic = {}
    log.sort(key = lambda x:x[0])
    for x in log :
        if x[1] not in dic:
            dic[x[1]] = (x[0],x[0])
        else:
            melhor_tempo = dic[x[1]][1]
            tempo_atual = dic[x[1]][0]
            diferenca_atual = x[0]- tempo_atual
            if (diferenca_atual <  melhor_tempo):
                melhor_tempo = diferenca_atual
            dic[x[1]] = (x[0], melhor_tempo)
    lista = [(x,y[1]) for x,y in dic.items ()]
    lista.sort(key = lambda x:(x[1],x[0]) )
    melhor = lista[0][1]
    new_lista = []
    for x in lista :
        if x[1] == melhor :
            new_lista.append(x[0])
    return new_lista



