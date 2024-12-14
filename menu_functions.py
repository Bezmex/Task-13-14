from functions_for_work import *
import re

def f1():
    global message
    print("Выберите тип ввода:\n1. Ввод текста с клавиатуры\n2. Случайная генерация")
    type = input()

    if is_int(type):
        type = int(type)
    if type == 1:
        message = input_text()
        print(f"Вы ввели следующий текст: {message} ")
    elif type == 2:
        message = random_text()
        print(f"Сгенерированный текст: {message}")
    else:
        print('error')
    return True

def f2(array_palindromes):
    text = message.lower()
    text = re.sub(r'[^\w\s]', '', text)

    words = text.split()

    palindromes = []

    # Проверка слова на палиндром
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)
    print("Алгоритм выполнен\n")
    array_palindromes.extend(palindromes)

def f3(palindromes):
    if len(palindromes) == 0:
        print("Палиндромов в тексте нет")
    else:
        print("Список палиндромов: ")
        for i in palindromes:
            print(i)
