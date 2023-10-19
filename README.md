# corp_django_course2

## How to Work With the Repository
To start the task, you need to copy the URL of your repository and clone it (please note that you are cloning your own repository, not the original template!).  
  ![image](https://user-images.githubusercontent.com/14962819/235600053-de6be309-56d5-4c5f-adc3-d466887962f6.png)
  
### Create a virtual environment

1. Launch the Visual Studio Code editor, and through the "*File" / "Open Directory"* menu, open the *Dev/corp_django_course2/* folder. 
2. Launch the terminal in VS Code and make sure you work from the *corp_django_course2/* directory. If you use Windows, make sure Git Bash runs in the terminal and not through anything else, like PowerShell. Run this command:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
The virtual environment will be deployed in the *corp_django_course2/* directory. The `venv` folder will be there too and will store all the project dependencies. The file structure will look like this:

```
Dev/
 └── corp_django_course2/
     ├── .github/    Folder with repository configs (hidden)   
     ├── .vscode/    Folder of the code editor (optional, hidden)
     ├── .git/       Git system information (hidden)
     ├── tests/             Тесты для проверки проекта
     ├── venv/              Директория виртуального окружения
     ├── pragmatic/          <-- Директория проекта
     |   ├── courses/
     |   ├── lessons/
     |   ├── pragmatic/
     |   ├── db.sqlite3     Файл базы данных (может и не быть)
     |   └── manage.py      
     ├── .gitignore         Список файлов и папок, скрытых от отслеживания Git (скрытый) 
     ├── db.json            <-- Фикстуры для базы данных    
     ├── LICENSE            Лицензия   
     ├── pytest.ini         Конфигурация тестов
     ├── README.md          Описание проекта 
     ├── requirements.txt   Список зависимостей проекта
     └── setup.cfg          Настройки тестов
```

### Активация виртуального окружения
в терминале перейдите в корневую директорию проекта *Dev/corp_django_course2/* и выполните команду:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Теперь все команды в терминале будут предваряться строкой `(venv)`.

💡 Все дальнейшие команды в терминале надо выполнять с активированным виртуальным окружением.

Обновите pip:

```bash
python -m pip install --upgrade pip
```

### Установка зависимостей из файла *requirements.txt*:
Находясь в папке *Dev/corp_django_course2/*, выполните команду:

```bash
pip install -r requirements.txt
```

#### End of Support зависимостей

Среди зависимостей выбраны LTS-версии зависимостей.
Для Django выбрана версия 3.2, extended support которой
заканчивается 1 апреля 2024 года.

### Применение миграций

    
В директории с файлом manage.py выполните команду: 

```bash
python manage.py migrate
```

### Запуск проекта в dev-режиме

    
В директории с файлом manage.py выполните команду: 

```bash
python manage.py runserver
```

В ответ Django сообщит, что сервер запущен и проект доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


### Локальный запуск тестов
После выполнения задания необходимо локально запустить тесты. В терминале перейдите в корневую директорию проекта *Dev/corp_django_course2/* и выполните команду:
```shell
pytest
```
Если все тесты пройдены успешно, то проект считается выполненным. В противном случае необходимо устранить моменты, которые не прошли проверку и повторно запустить тесты.
