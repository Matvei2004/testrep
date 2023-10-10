import random
import os
import time

hangman = [["           ", "           ", "           ", "           ", "           ", "           "],
           ["           ", "           ", "           ", "           ", "           ", "_______/|\_"],
           ["           ", "        |  ", "        |  ", "        |  ", "        |  ", "_______/|\_"],
           ["   +----+  ", "        |  ", "        |  ", "        |  ", "        |  ", "_______/|\_"],
           ["   +----+  ", "   |    |  ", "   o    |  ", "        |  ", "        |  ", "_______/|\_"],
           ["   +----+  ", "   |    |  ", "   o    |  ", "  /|\   |  ", "        |  ", "_______/|\_"],
           ["   +----+  ", "   |    |  ", "   o    |  ", "  /|\   |  ", "  / \   |  ", "_______/|\_"]]

dictinary = ["автобус", "конь", "парта", "пенал"]

"""Необходимые ГЛОБАЛЬНЫЕ переменные"""
health_points = 6
random_words = dictinary[random.randint(0, len(dictinary) - 1)]
random_words_in_game = "_" * len(random_words)
wrong_letters = ""

hight = int(input("Введите высоту игрвого поля, но не меньше 9: ")) + 2
width = int(input("Введите ширину игрвого поля, но не меньше 11: ")) + 2
snake = ["right", [5, 5], [4, 5], [3, 5], [2, 5]]
field = []

"""Функция создания игрового поля (Высота, Ширина)"""
def Creat_Field(hight, width):
    for i in range(hight):
        field.append([])
        for k in range(width):
            if (i == 0 or i == hight - 1) and (k == 0 or k == width - 1):
                field[i].append("+")
            if (i == 0 or i == hight - 1) and (k != 0 and k != width - 1):
                field[i].append("-")
            if (i != 0 and i != hight - 1) and (k == 0 or k == width - 1):
                field[i].append("|")
            if (i != 0 and i != hight - 1) and (k != 0 and k != width - 1):
                field[i].append(" ")

"""Функция создания случайных букв на поле"""
def Creat_Letter_on_Field(snake, random_words, random_words_in_game):

    """Создаем массив букв для распределения по полю"""
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    letters = [0, 0, 0]
    for i in range(0, len(random_words_in_game)):
        random_words = random_words.replace(random_words_in_game[i], "")
    letters[0] = random_words[random.randint(0, len(random_words) - 1)]
    for i in range(0, len(random_words)):
        alphabet = alphabet.replace(random_words[i], "")
    letters[1] = alphabet[random.randint(0, len(alphabet) - 1)]
    alphabet = alphabet.replace(letters[1], "")
    letters[2] = alphabet[random.randint(0, len(alphabet) - 1)]

    """Распределяем буквы по полю"""
    while len(letters) != 0:
        i = random.randint(1, len(field) - 2)
        k = random.randint(1, len(field[i]) - 2)
        if not([k, i] in snake):
            field[i][k] = letters[len(letters) - 1]
            letters.pop(len(letters) - 1)

"""Функция отрисовки змеи на поле"""
def Snake_on_Field():
    for i in range(1, len(snake)):
        if i == 1:
            field[snake[i][1]][snake[i][0]] = "@"
        else:
            field[snake[i][1]][snake[i][0]] = "#"

"""Фунция вывода готового кадра"""
def Print_Game_Skrin(random_words_in_game, wrong_letters):

    hang_skrin = hangman[6 - health_points]
    hang_skrin.append("")
    hang_skrin.append("Загаданное слово: " + random_words_in_game)
    hang_skrin.append("Неправильные буквы: " + wrong_letters)

    for i in range(len(field)):
        for k in range(len(field[i])):
            print(field[i][k], end="")
        if i <= 8:
            print("      ", end="")
            print(hang_skrin[i], end="")
        print("\n", end="")

"""Функция очистки поля от букв"""
def Clear_Letters():
    for i in range(len(field)):
        for k in range(len(field[i])):
            if field[i][k] != "+" and field[i][k] != "-" and field[i][k] != "|" and field[i][k] != "@"\
                    and field[i][k] != "#" and field[i][k] != " ":
                field[i][k] = " "

"""Фунция проползания"""
def Crowl_Snake():

    global health_points

    """Ползок вправо"""
    if snake[0] == "right":
        if field[snake[1][1]][snake[1][0] + 1] != "#" and field[snake[1][1]][snake[1][0] + 1] != "-" and\
                field[snake[1][1]][snake[1][0] + 1] != "|":

            letter = field[snake[1][1]][snake[1][0] + 1]

            field[snake[1][1]][snake[1][0]] = "#"
            field[snake[1][1]][snake[1][0] + 1] = "@"

            if letter == " ":
                field[snake[-1][1]][snake[-1][0]] = " "
                for i in range(len(snake) - 1, 1, -1):
                    snake[i][0] = snake[i - 1][0]
                    snake[i][1] = snake[i - 1][1]
                snake[1][0] = snake[2][0] + 1
            else:
                snake.insert(1, [snake[1][0] + 1, snake[1][1]])
                Hang_Man(letter)
        else:
            health_points = 0


    """Ползок вверх"""
    if snake[0] == "up":
        if field[snake[1][1] - 1][snake[1][0]] != "#" and field[snake[1][1] - 1][snake[1][0]] != "-" and \
                field[snake[1][1] - 1][snake[1][0]] != "|":

            letter = field[snake[1][1] - 1][snake[1][0]]

            field[snake[1][1]][snake[1][0]] = "#"
            field[snake[1][1] - 1][snake[1][0]] = "@"

            if letter == " ":
                field[snake[-1][1]][snake[-1][0]] = " "
                for i in range(len(snake) - 1, 1, -1):
                    snake[i][0] = snake[i - 1][0]
                    snake[i][1] = snake[i - 1][1]
                snake[1][1] = snake[2][1] - 1
            else:
                snake.insert(1, [snake[1][0], snake[1][1] - 1])
                Hang_Man(letter)
        else:
            health_points = 0

    """Ползок влево"""
    if snake[0] == "left":
        if field[snake[1][1]][snake[1][0] - 1] != "#" and field[snake[1][1]][snake[1][0] - 1] != "-" and \
                field[snake[1][1]][snake[1][0] - 1] != "|":

            letter = field[snake[1][1]][snake[1][0] - 1]

            field[snake[1][1]][snake[1][0]] = "#"
            field[snake[1][1]][snake[1][0] - 1] = "@"

            if letter == " ":
                field[snake[-1][1]][snake[-1][0]] = " "
                for i in range(len(snake) - 1, 1, -1):
                    snake[i][0] = snake[i - 1][0]
                    snake[i][1] = snake[i - 1][1]
                snake[1][0] = snake[2][0] - 1
            else:
                snake.insert(1, [snake[1][0] - 1, snake[1][1]])
                Hang_Man(letter)
        else:
            health_points = 0

    """Ползок вниз"""
    if snake[0] == "down":
        if field[snake[1][1] + 1][snake[1][0]] != "#" and field[snake[1][1] + 1][snake[1][0]] != "-" and \
                field[snake[1][1] + 1][snake[1][0]] != "|":

            letter = field[snake[1][1] + 1][snake[1][0]]

            field[snake[1][1]][snake[1][0]] = "#"
            field[snake[1][1] + 1][snake[1][0]] = "@"

            if letter == " ":
                field[snake[-1][1]][snake[-1][0]] = " "
                for i in range(len(snake) - 1, 1, -1):
                    snake[i][0] = snake[i - 1][0]
                    snake[i][1] = snake[i - 1][1]
                snake[1][1] = snake[2][1] + 1
            else:
                snake.insert(1, [snake[1][0], snake[1][1] + 1])
                Hang_Man(letter)
        else:
            health_points = 0


"""Игра в висилицу"""
def Hang_Man(letter):

    global health_points
    global random_words_in_game
    global wrong_letters

    if health_points == 0:
        health_points -= 1
    if letter in random_words:
        for i in range(len(random_words)):
            if random_words[i] == letter:
                random_words_in_game = random_words_in_game[:i] + letter + random_words_in_game[i + 1:1000]
    else:
        wrong_letters = wrong_letters + letter
        health_points -= 1
    if ("_" in random_words_in_game) == 0:
        print("Ура!")


"""Тест проги!"""
Creat_Field(hight, width)
Snake_on_Field()
Creat_Letter_on_Field(snake, random_words, random_words_in_game)
os.system('cls||clear')

field[5][6] = "а"




for i in ["right", "right", "right", "up", "up", "up", "left", "left", "left", "down", "down", "down"] * 1:
    snake[0] = i
    Crowl_Snake()
    print(random_words_in_game)
    Print_Game_Skrin(random_words_in_game, wrong_letters)
    #print(random_words_in_game)
    print(wrong_letters)
    time.sleep(0.07)
    os.system('cls||clear')
