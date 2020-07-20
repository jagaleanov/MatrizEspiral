#Dada una matriz, retornar una lista de sus valores leidos en forma de espiral 
#en sentido horario empezando desde la posición (x,y)=(0,0)

def head(lista):
  return lista[0]

def tail(lista):
  return lista[1:]

def transpose(matriz):
    if(len(matriz[0])==0):
        return []
    else:
        return [list(map(head, matriz))] + transpose(list(map(tail, matriz)))

def spiralList(matriz):
    if len(matriz)==1:
        return matriz[0]
    else:
        return matriz[0] + spiralList(list(reversed(transpose(matriz[1:]))))

#print("spiralList([[1,2],[3,4]])")
#print(spiralList([[1,2],[3,4]]))
#print("spiralList([[1,2],[3,4],[5,6]])")
#print(spiralList([[1,2],[3,4],[5,6]]))
#print("spiralList([[1,2,3],[4,5,6],[7,8,9]])")
#print(spiralList([[1,2,3],[4,5,6],[7,8,9]]))
#print("spiralList([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])")
#print(spiralList([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
#print("spiralList([[1,2,3,4],[5,6,7,8],[9,10,11,12]])")
#print(spiralList([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
#print("spiralList([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])")
#print(spiralList([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))