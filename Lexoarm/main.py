#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor  # Legger til TouchSensor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait

# Opprett EV3 og motorer
ev3 = EV3Brick()

# Oppretter motorene på port A og B
motor1 = Motor(Port.A)
motor2 = Motor(Port.B)

# Oppretter touchSensorer på port S1 og S2
ned_sensor = TouchSensor(Port.S1)   # Kjør opp / utover
opp_sensor = TouchSensor(Port.S2)   # Kjør ned / innover

# Definerer Hastigheter
RASK = 120    # Hastighet for Konsentrisk (rask innover)
SAKTE = 120   # Hastighet for Eksentrisk (sakte utover)

# Funksjon som stopper begge motorene og holder posisjonen
def stopp():
    motor1.stop(Stop.HOLD)
    motor2.stop(Stop.HOLD)

# Funksjon som kjører motorene innover (negativ hastighet)
def kjor_innover():
    motor1.run(-RASK)
    motor2.run(-RASK) 

# Funksjon som kjører motorene utover (positiv hastighet)
def kjor_utover():
    motor1.run(SAKTE)
    motor2.run(SAKTE)

# Hovedprogram
# Skriver instruksjoner på EV3-skjermen Hovedprogram
ev3.screen.print("Trykk knappen rød for å kjøre inn")
ev3.screen.print("Trykk knappen grønn for å kjøre ut")

# Hovedløkka som kjører kontinuerlig
while True:
    
    # Hvis ned-sensoren trykkes → kjør motorene innover
    if ned_sensor.pressed():
        ev3.screen.print("Kjører INN")
        kjor_innover()

     # Hvis opp-sensoren trykkes → kjør motorene utover
    elif opp_sensor.pressed():
        ev3.screen.print("Kjører UT")
        kjor_utover()
    
    # Hvis ingen sensor trykkes → stopp motorene
    else:
        stopp()

    # Liten pause for å unngå overbelastning av prosessoren
    wait(10)