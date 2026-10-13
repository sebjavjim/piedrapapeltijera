#Solicito a los jugadores que ingresen su nombre
nombre1 = input ("Ingrese nombre del primer participante: ")
nombre2 = input ("Ingrese nombre del segundo participante: ")

#Solicita a los jugadores que hagan su elección
jugador1 = input ("Elige Piedra (PI), Papel (PA), o Tijera (T) para " + nombre1 + ": ")
jugador2 = input ("Elige Piedra (PI), Papel (PA), o Tijera (T) para " + nombre2 + ": ")

if jugador1 == jugador2:
    print ("Empate")
elif ((jugador1.upper=="PI" and jugador2.upper == "T") 
      or (jugador1.upper=="PA" and jugador2.upper == "PI")
      or (jugador1.upper=="T" and jugador2.upper == "PA")):
    print (nombre1,"gana!")
else: 
    print (nombre2, "gana!")