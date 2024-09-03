from pytamaro import Graphic, Color, circular_sector
from pytamaro import (
    Graphic,
    Color,
    rgb_color,
    rectangle,
    pin,
    above,
    compose,
    rotate,
    show_graphic,
    bottom_right,
    bottom_left,
)

LOVE_RED = rgb_color(222, 0, 0)


def semicircle(diameter: float, color: Color) -> Graphic:
    return circular_sector(diameter / 2, 180, color)


def heart(size: float, color: Color) -> Graphic:
    atrium = semicircle(size, color)
    ventricles = rectangle(size, size, color)
    rotated_heart = compose(
        pin(bottom_right, above(atrium, ventricles)),
        pin(bottom_left, rotate(-90, atrium)),
    )
    return rotate(45, rotated_heart)


show_graphic(heart(200, LOVE_RED))
