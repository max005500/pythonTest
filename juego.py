import random

class Entity:
    def __init__(self, simbol):
        self.simbol = simbol
        
    def winnner(self, tab) -> bool:
        return ((self.simbol == tab[1] and self.simbol == tab[2] and self.simbol == tab[3]) or 
            (self.simbol == tab[1] and self.simbol == tab[5] and self.simbol == tab[9]) or
            (self.simbol == tab[1] and self.simbol == tab[4] and self.simbol  == tab[7]) or
            (self.simbol == tab[2] and self.simbol == tab[5] and self.simbol == tab[8]) or
            (self.simbol == tab[3] and self.simbol == tab[6] and self.simbol == tab[9]) or
            (self.simbol == tab[3] and self.simbol == tab[5] and self.simbol == tab[7]) or
            (self.simbol == tab[4] and self.simbol == tab[5] and self.simbol == tab[6]) or
            (self.simbol == tab[7] and self.simbol == tab[8] and self.simbol == tab[9]))

class Tablero:
    def __init__(self,tab):
        self.tab = tab

    #NOTE: Imprime el tablero
    def imprimir(self):
        print('   |   |')
        print(' ' + self.tab[7] + ' | ' + self.tab[8] + ' | ' + self.tab[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.tab[4] + ' | ' + self.tab[5] + ' | ' + self.tab[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.tab[1] + ' | ' + self.tab[2] + ' | ' + self.tab[3])
        
    def interface(self):
        print('   |   |')
        print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + '1' + ' | ' + '2' + ' | ' + '3')

    #NOTE: Retornar si es posible seguir jugando o no (define empate)
    def completeTab(self):
        for x in range(1,10):
            if self.__validMove(x):
                return False
        return True

    #NOTE: Elegir jugada en espacio vacio o que no este ocupado
    def __validMove(self,jug):
         return(self.tab[jug] == ' ')

    #NOTE: Elegir jugada random
    def __random(self, rango):

        posibleMoves = []

        for x in rango:
            if self.__validMove(x):
                posibleMoves.append(x)

        if len(posibleMoves) != 0: 
            return random.choice(posibleMoves)
        else:
            return None

    #NOTE: Define movimiento del jugador

    def copyTab(self,simb,move):
        if self.__validMove(move):
            self.tab[move] = simb
            return self.tab
        return None

    def __win(self,simb,tab):
        return ((simb == tab[1] and simb == tab[2] and simb == tab[3]) or 
                (simb == tab[1] and simb == tab[5] and simb == tab[9]) or
                (simb == tab[1] and simb == tab[4] and simb == tab[7]) or
                (simb == tab[2] and simb == tab[5] and simb == tab[8]) or
                (simb == tab[3] and simb == tab[6] and simb == tab[9]) or
                (simb == tab[3] and simb == tab[5] and simb == tab[7]) or
                (simb == tab[4] and simb == tab[5] and simb == tab[6]) or
                (simb == tab[7] and simb == tab[8] and simb == tab[9]))

    #NOTE: metodo que define el movimiento del bot en el tablero (pseudo IA)
    def botPlay(self, simb):

    #NOTE: forma en la que el bot reconoce su simbolo y el del jugador
        if simb == 'X':
            jugSimb = 'O'
        else: 
            jugSimb = 'X'

    #NOTE: La posicion en donde el bot realiza su jugada se define en base a prioridades:

    #NOTE: 1 primera prioridad: Blockear al jugador para que no gane

        for jug in range(1,10):
            copy = self.tab.copy()
            if self.__validMove(jug):
                copy[jug] = simb
                if self.__win(simb,copy):
                   print('gano')
                   self.tab[jug] = simb 
                   return self.tab

    #NOTE: 2 segunda prioridad: Hacer la jugada ganadora

        for jug in range(1,10):
            copy = self.tab.copy()
            if self.__validMove(jug):
                copy[jug] = jugSimb
                if self.__win(jugSimb,copy):
                    self.tab[jug] = simb 
                    return self.tab

    #NOTE: 3 tercera prioridad: Tomar las esquinas.

        jug = self.__random([1,3,7,9])
        if jug != None:
             self.tab[jug] = simb
             return self.tab

    #NOTE: 4 cuarta prioridad: Tomar el centro.
        if self.__validMove(5):
            self.tab[5] = simb
            return self.tab

    #NOTE: 5 quinta prioridad: Tomar los lados.
        jug=self.__random([2,4,8,6])
        if jug != None:
            self.tab[jug] = simb
            return self.tab

    #NOTE: En caso de que el juego termine en empate.

        return self.tab

#NOTE: Define el movimiento del jugador 
def move():
    print('Ingrese su jugada: ')
    while True:
        try:
           mov = int(input())
           if 9 < mov < 1 : 
               print('Ingrese un valor de 1 a 9: ')
           else: 
               return mov
        except:
            print('Ingrese un valor numerico: ')

#NOTE: Define el simbolo del jugador y el bot 

def simbol():
    val = ''
    while(not (val == 'X' or val == 'O')):
        print('Elige que quieres ser: X o O')
        val = input().upper()
        if val == 'X':
            return  ['X', 'O'] 
        elif val == 'O':
            return ['O','X']
        else:
           print('elige un valor real') 
    return ['X', 'O'] 


#NOTE: Define la salida del bucle del juego 
def playAgain():
    res = ''
    while (not(res == 'SI' or res == 'NO')):
        print('Quieres volver a jugar ? (si o no)')
        res = input().upper()
        if not (res == 'SI' or res == 'NO'):
           print('Ingrese una respuesta aceptable') 
    return res


#NOTE: Ejecucion del juego 
 
while True:

    play = True
    print('Bienvenido!!!')
    jug,pc = simbol()
    print('has elegido: ' + jug)

    tab = Tablero([' ']*10)
    player = Entity(jug)
    bot = Entity(pc)
    turn = random.randint(0,1)

    print('Relacion numeros y casillas')
    tab.interface()
    tab.imprimir()
    if turn == 0:
       print('Comienza el bot')
       tab.botPlay(bot.simbol)
       turn = 1
    else:
       print('Comienza el jugador')
       jug = move()
       tab.copyTab(player.simbol,jug)
       turn = 0
    tab.imprimir()
    while play: 
        if turn == 0:
            tab.botPlay(bot.simbol)
            print('Jugada del BOT')
            tab.imprimir()
            if bot.winnner(tab.tab):
                print('A ganado el bot')
                play = False
            elif tab.completeTab():
                print('Ambos estan bien torpes')
                play = False
            else:
                turn = 1
        else:
            mov = move()
            while tab.copyTab(player.simbol,mov) == None:
                print('Ingresa un espacio que este vacio')
                mov = move()
            tab.copyTab('x',mov)
            tab.imprimir()
            if player.winnner(tab.tab):
                print('Felicidades has ganado')
                play = False
            elif tab.completeTab():
                print('Ambos estan bien torpes')
                play = False
            else:
                turn = 0
    if playAgain() == 'NO':
        break







