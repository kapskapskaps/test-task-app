# test-task-app
Решение тестового задания
## Описание
Тут вот описание какое-то крутое
## Как запустить

1. Сборка Docker образа
```bash
docker build -t my-web-app:latest .
```

2. Запуск Docker
```bash
docker run -d -p 8080:80 my-web-app:latest
```

3. Вариант запуска через Docker compose
```bash
docker run -d -p 8080:80 my-web-app:latest
```

4. Проверка работы - открой брайузер с адресом:
http://localhost:8080

## Вопрос для размышления

Гугл подсказал что можно смотировать образ через:
```bash
docker run -d -p 8080:80 -v $(pwd)/index.html:/usr/share/nginx/html/index.html my-web-app:latest
```


# Часть B

## B1
Я не стал создавать отдельный проект для части B, чтобы проверяющему было легче жить

Файл 'clean_old_logs.py' - это скрипт, который удаляет старые логи. Код слабый, но для тестового задания пойдет. Если делать его идеальным, то я бы добавил argparse, pathlib.Path, авто подсчет времени, добавить проверку директории, поделить на функции, поработать над ошибкой которая возникнет если нет прав у пользователя. 
С bash кодом мало опыта, по этому выбрал Python.

## B2


1. Сохранить изменения в стэш
2. Переключиться на ветку main
3. Добавить исправления и комитим багофикс
4. Вернуться в ветку featire/junior-tast
5. Востановить изменения из стэша
6. Разрешить перезапись конфликтов
7. Изменить коммит (как-будто это вопрос с подвохом, я точно это знаю, но не могу доказать)

```bash
git stash push -m "WIP: feature/junior-task"
git checkout main
git add .
git commit -m "Fix critical bug"
git checkout feature/junior-task
git stash pop
git commit --amend -m "Обновленный комит"
git push
```
