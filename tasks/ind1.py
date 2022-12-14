#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("file1.txt", "r", encoding="utf-8") as f1:
        file1 = f1.read()
    n = input("Введите слово для поиска: ")
    for j in file1.split("\n"):
        if j.count(n):
            print(j)
