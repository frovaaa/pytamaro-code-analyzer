from pytamaro.it import *


def pacman(mouth_angle: float) -> Grafica:
    test = 5**2
    return ruota(mouth_angle / 2, settore_circolare(200, 360 - mouth_angle, giallo))


visualizza_grafica(pacman(65))
