## Cервис YaCut

Проект YaCut — это сервис укорачивания ссылок. 
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, 
которую предлагает сам пользователь или предоставляет сервис.

###


Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Запустить приложение 

```
flask run -p 5000
```
Пример POST запроса на http://127.0.0.1:5000/api/id/

Запрос

```
{
   "url": "https://https://practicum.yandex.ru/learn/python-developer-plus/courses/0d476f74-b799-4579d/sprints//",
   "custom_id": "ddd4Fs" 
}
```

Ответ

```
{
    "short_link": "http://127.0.0.1:5000/ddd4Fs",
    "url": "https://https://practicum.yandex.ru/learn/python-developer-plus/courses/0d476f74-b799-4579d/sprints//"
}
```

Пример GET запроса на http://127.0.0.1:500/api/id/ddd4Fs/

Ответ

```
{
    "url": "https://https://practicum.yandex.ru/learn/python-developer-plus/courses/0d476f74-b799-4579d/sprints//"
}
```

### Автор
Намистюк Анжела


