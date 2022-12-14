#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == "__main__":
    n = input("Введите содержимое файла:\n")
    name = "".join([input("Сохранить под именем (Введите название файла): "), ".txt"])

    with open("newfile.txt", "w") as f:
        f.write(n)
        f.write("\nФайл изменен пользователем: ")
        f.write(os.getlogin())
    ch = os.path.exists(name)
    if not ch:
        os.rename("newfile.txt", name)
    else:
        print("Файл уже существует")
