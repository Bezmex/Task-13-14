from menu_functions import f1, f2, f3
from functions_for_work import is_int
import threading
import time

def menu():
    array_palindromes = []  # массив палиндромов
    is_text_input = False
    is_algoritm_done = False

    while True:
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста \n"
              "2. Выполнение алгоритма по поиску палиндромов в тексте\n"
              "3. Вывод результата\n"
              "4. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)

        if choice == 1:
            text_input_thread = threading.Thread(target=f1)
            text_input_thread.start()
            text_input_thread.join()
            is_text_input = True

        elif choice == 2:
            if is_text_input:
                algorithm_thread = threading.Thread(target=lambda: f2(array_palindromes))
                algorithm_thread.start()
                algorithm_thread.join()
                is_algoritm_done = True
            else:
                print("Ошибка!\nСначала введите текст\n\n")

        elif choice == 3:
            if is_algoritm_done:
                if is_text_input:
                    result_thread = threading.Thread(target=f3, args=(array_palindromes,))
                    result_thread.start()
                    result_thread.join()
            else:
                print("\nСначала выполните алгоритм\n")

        elif choice == 4:
            break
        else:
            print('error')

if __name__ == "__main__":
    menu()



"""
1) threading.Thread создает новый поток (передаем в target функцию и в args аргументы)
2) После создания потока его нужно запустить с помощью метода start().
3) Чтобы основной поток дождался завершения выполнения нового потока, используется метод join().
"""