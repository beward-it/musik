import pygame.mixer as player
import os
import random
"""from pyglet.window import mouse
import pyglet
wind = pyglet.window.Window()
width, height = wind.size
button1 = pyglet.shapes.Rectangle(0, 0 , 20, 20)
button2 = pyglet.shapes.Rectangle(20, 20 , 20, 20)
button3 = pyglet.shapes.Rectangle(40, 40 , 20, 20)
picked = button1
@wind.event
def on_mouse_press(x, y, button, modifiers):
    pass
@wind.event
def on_draw():
    button1.draw()
    button2.draw()
    button3.draw()
pyglet.app.run()"""
musik = os.listdir()
musik.remove('main.py')
musik.remove('.gitattributes')
musik.remove('README.md')
musik.remove('.git')
mode = int(input("Выбери режим 1 - повторение, 2 - проверка знаний, 3 - экзамен: "))
i = 0
print(len(musik))
random.shuffle(musik)
while True:
    if i == len(musik):
        random.shuffle(musik)
        print("Все 20 произведений прослушаны")
        i = 0
    player.init()
    sound = musik[i]
    print(sound)
    zvuk = player.Sound(sound)
    zvuk.play()
    number, autor, name = sound.split("_")
    if mode == 1:
        print(f"Это номер {number}, автор - {autor}, название - {name}.")
        input()
    elif mode == 2:
        if number == input("Номер произведения: "):
            print("Верно!")
        else:
            print(f"Неверно! Это номер {number}, автор - {autor}, название - {name}.")
    else:
        result = 0
        if number == input("Номер произведения: "):
            result += 1
        if i == 20:
            if 0.75 > result / 20 >= 0.5:
                grade = 3
            elif result / 20 < 0.5:
                grade = 2
            elif result / 20 >= 0.9:
                grade = 5
            else:
                grade = 4
            print(f"Ваш результат {result} / 20. Ваша оценка - {grade}.")
            break
    zvuk.stop()
    i += 1
"""@wind.event
def on_draw():
    pyglet.shapes.Rectangle(500, 500, 500, 500)
pyglet.app.run()"""