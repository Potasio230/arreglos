#los arreglos tienen que tener si o si corchetes
#siempre parten en cero

playlistdelcurso = [
    "Este.mp3" ,
    "otro.mp3" ,
    "aquello.mp3" ,
    "hiolaaaaaaaaaaa"
]

print(playlistdelcurso)
print(playlistdelcurso[2])

#tamaño de arreglo = a la cantidad de elementos 
print("tamaño del arreglo")

#len se encarga de calcular el tamaño a algo
#es una función
tamañoLista = len(playlistdelcurso)
print(tamañoLista)

#para saber cual es la ultima cancion si no sabemos la cantidad de cosas que tiene un arreglo:
print("#########---la ultima cancion es:")
print(playlistdelcurso[tamañoLista - 1])


print("imprimir todas las letras de una palabra")
#palindromo es una palabra que se lee igual alrevés:
nuevaPalabra = "GIRAFARIG"

#manera bruta, aca contamos cuantas veces tiene se tiene que iterar
for i in range(len(nuevaPalabra)):
    print(nuevaPalabra[i])