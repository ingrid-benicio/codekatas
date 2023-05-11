def teste_funcao(numero):
    lista_numero = list(str(numero))
    lista_numero.sort(reverse= True, key=int)
    lista_string = int(''.join(lista_numero))
    
    
    return lista_string
    


print(teste_funcao('5544265984894651654611'))