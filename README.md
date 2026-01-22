# test-task-app
Решение тестового задания
## Описание
Тут вот описание какое-то крутое
## Как запустить

1. Сборка Docker образа
```bash
docker build -t test-task-app:latest .
```

2. Запуск Docker
```bash
docker run -d -p 8080:80 test-task-app:latest
```

3. Вариант запуска через Docker compose
```bash
docker run -d -p 8080:80 test-task-app:latest
```

4. Проверка работы - открой брайузер с адресом:
http://localhost:8080

## Вопрос для размышления

Гугл подсказал что можно смотировать образ через:
```bash
docker run -d -p 8080:80 -v $(pwd)/index.html:/usr/share/nginx/html/index.html test-task-app:latest
```
