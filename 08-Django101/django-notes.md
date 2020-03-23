### Some notes for setting up Django and getting a project up and running
These notes are specific to a Windows 10 and VSCode setup -- ymmv!

#### To allow PowerShell to run scripts (run this in an admin session:
```
set-executionpolicy remotesigned
```

#### To create and activate a virtual environment (in the PowerShell window of VSCode):
```
python -m venv <folder_name>
cd <folder_name>
scripts/Activate.ps1
```

#### To de-activate your virtual environment:
```
deactivate
```

#### To install Django:
```
python -m pip install Django
```

#### To create a Django project (from the root folder, i.e. where your environment is based):
```
django-admin startproject <project_name>
```

#### To create a Django app within a project (from the project root folder):
```
python manage.py startapp <app_name>
```

#### To run the project:
```
python manage.py runserver
```
