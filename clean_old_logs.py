#!/usr/bin/env python3
import os
import sys
import time

if len(sys.argv) < 3:
    print("Для использование программы укажите директорию и кол-во дней, пример: python3 clean_old_logs.py <директория> <кол-во дней>")
    sys.exit(1)

directory = sys.argv[1]
days = int(sys.argv[2])
seconds = days * 24 * 60 * 60

old_logs = []
for filename in os.listdir(directory):
    if filename.endswith(".log"):
        filepath = os.path.join(directory, filename)
        mtime = os.path.getmtime(filepath)
        if time.time() - mtime > seconds:
            old_logs.append(filepath)

if not old_logs:
    print(f"Файлов старше {days} дней не найдено.")
    sys.exit(0)

print("Найдены следующие файлы:")
for f in old_logs:
    print(f)

choice = input("Удалить эти файлы? (y/n) ").strip().lower()
if choice == "y":
    for f in old_logs:
        os.remove(f)
    print("Файлы удалены.")
else:
    print("Удаление отменено.")
