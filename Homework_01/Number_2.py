# This Python file uses the following encoding: utf-8
# Написать функцию для нахождения одинаковых элементов в двух списках.

def comp_elements(a: list, b: list):
    for elemA in a:
        for elemB in b:
            if elemA == elemB:
                print(elemA)


list_1 = input("Введите первый список: ").split()
list_2 = input("Введите второй список: ").split()

comp_elements(list_1, list_2)
