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
     ├── tests/             Tests for project verification
     ├── venv/              Virtual environment directory
     ├── pragmatic/          <-- Project directory
     |   ├── courses/
     |   ├── lessons/
     |   ├── pragmatic/
     |   ├── db.sqlite3     Database file (might not exist)
     |   └── manage.py      
     ├── .gitignore         List of files and folders hidden from Git tracking 
     ├── db.json            <-- Fixtures for the database    
     ├── LICENSE            License   
     ├── pytest.ini         Tests configuration
     ├── README.md          Project description 
     ├── requirements.txt   Project dependency list
     └── setup.cfg          Tests setup
```

### Activation of the virtual environment
in the console, go to the root directory of the project *Dev/corp_django_course2/* and run this command:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Now all commands in the terminal will be preceded by the string `(venv)`.

💡 All further commands in the terminal should be executed with the activated virtual environment.

Refresh pip:

```bash
python -m pip install --upgrade pip
```

### Install the dependencies from the *requirements.txt* file
Run the following command while you are in the *Dev/corp_django_course2/* folder:

```bash
pip install -r requirements.txt
```

#### End of support for dependencies

The LTS versions of dependencies have been chosen.
For Django, the version 3.2 was selected. Its extended support
ends on April 1, 2024.

### Using migrations

    
In the directory with the "manage.py" file, run the command: 

```bash
python manage.py migrate
```

### Running the project in dev mode

    
In the directory with the "manage.py" file, run the command: 

```bash
python manage.py runserver
```

В ответ Django сообщит, что сервер запущен и проект доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


### Локальный запуск тестов
После выполнения задания необходимо локально запустить тесты. in the console, go to the root directory of the project *Dev/corp_django_course2/* and run this command:
```shell
pytest
```
Если все тесты пройдены успешно, то проект считается выполненным. В противном случае необходимо устранить моменты, которые не прошли проверку и повторно запустить тесты.
