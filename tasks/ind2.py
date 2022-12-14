#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
отображает последние десять строк
содержимого файла, имя которого передается в качестве аргумента командной строки.
Реализуйте программу, которая будет делать то же самое. В случае отсутствия файла,
указанного пользователем, или аргумента командной строки вам нужно вывести
соответствующее сообщение.
"""

import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(
            "Передайте имя файла в качестве аргумента командной строки: ",
            sys.argv,
            len(sys.argv),
        )
        quit()

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            sentences = f.readlines()

            for i, sentence in enumerate(sentences):
                print(sentence)
                if i >= 9:
                    break

    except IOError:
        # Отображаем ошибку, если с чтением из файла возникли проблемы
        print("Ошибка при доступе к файлу.")