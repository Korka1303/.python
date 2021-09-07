# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.tiyle =title

    def draw(self):
        print('Начни рисовать!')


class Pen(Stationery):
    def draw(self):
        print('Начни рисовать ручкой!')


class Pencil(Stationery):
    def draw(self):
        print("Начни рисовать карандашом!")


class Handle(Stationery):
    def draw(self):
        print("Начни рисовать маркером!")


pen = Pen('A')
pencil = Pencil('B')
handle = Handle('C')
for s in (pen, pencil, handle):
    s.draw()