import random

def cargar_palabras(ruta):
    '''
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res

def elegir_palabra(palabras):
    return random.choice(palabras)

def enmascarar_palabra(palabra, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    letras = []
    for i in range(0, len(palabra)):
        if palabra[i] in set(letras_probadas):
            letras.append(palabra[i])
        else:
            letras.append("_")
    print(str(" ".join(letras)))
    return " ".join(letras)

def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''
    letra = str((input("Adivina una letra:"))).lower()
    while letra in letras_probadas:
        letra = str(input("Ya ha probado esa letra, introduzca otra distinta:")).lower()
    return letra

def comprobar_letra(palabra_secreta, letra):
    if letra in palabra_secreta:
        print("¡Bien hecho! Esa letra estaba en la palabra secreta")
        return True
    else:
        print("Lo siento, esa letra no está en la palabra")
        return False

def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    '''
    Completada = []
    for i in range(0, len(palabra_secreta)):
        if palabra_secreta[i] in letras_probadas:
            Completada.append("Verdad")
        else:
            Completada.append("Mentira")   
    if set(Completada) == {"Verdad"}:
        return True
    else:
        return False
    
def ejecutar_turno(palabra_secreta, letras_probadas):
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Añadir la letra al conjunto de letras probadas
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla
    '''
    enmascarar_palabra(palabra_secreta, letras_probadas)
    letra = pedir_letra(letras_probadas)
    comprobar_letra(palabra_secreta, letra)
    letras = [letras_probadas]
    letras.append(letra)
    if comprobar_letra:
        return True
    elif comprobar_letra == False:
        return False

def jugar(max_intentos, palabras):
    '''
    Completar una partida hasta que el jugador gane o pierda:
    - Mostrar mensaje de bienvenida
    - Elegir la palabra secreta a adivinar
    - Inicializar las variables del juego (letras probadas e intentos fallidos)
    - Ejecutar los turnos de juego necesarios hasta finalizar la partida, y en cada turno:
      > Averiguar si ha habido acierto o fallo
      > Actualizar el contador de fallos si es necesario
      > Comprobar si se ha superado el número de fallos máximo
      > Comprobar si se ha completado la palabra
      > Mostrar el mensaje de fin adecuado si procede o el número de intentos restantes
    '''
    print("¡Bienvenido al ahorcado!")
    secreta = elegir_palabra(palabras)
    letras = []
    intentos = max_intentos
    i = 0
    while i <= max_intentos:
        print("Este es su intento número " + str(i + 1) + " de " + str(max_intentos))
        ejecutar_turno(secreta, letras)
        if ejecutar_turno:
            i += 1
        comprobar_palabra_completa(secreta, letras)
        if comprobar_palabra_completa:
            print("Has ganado! La palabra era:" + str(secreta))
            pass






# Iniciar el juego
if __name__ == "__main__":
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(6, palabras)