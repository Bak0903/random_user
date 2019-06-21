Как запустить проект.

В Windows:pip install virtualenv

Linux и Mac OS:
sudo pip install virtualenv

После установки проверьте версию виртуального окружения:
virtualenv --version

В папке проекта пропишите в консоли команду для установки виртуального окружения:
virtualenv -p python3 venv

После установки можно будет активировать виртуальное окружение: 

Windows:
venv\Scripts\activate

Linux и Mac OS:
. venv/bin/activate

Чтобы отключить (деактивировать) виртуальное окружение, в корневой папке используйте команду deactivate:
корневая папка проекта  > deactivate

Установите Django REST Framework:
pip install djangorestframework

Склонируйте проект:
git clone https://github.com/Bak0903/random_user.git

После установки перейдите в папку с файлом manage.py и проведите миграции:
python3 manage.py migrate

Создайте супер юзера:
python3 manage.py createsuperuser

pip install -r requirements.txt
В папке с manage.py запустите проект:

Запустите сервер
python3 manage.py runserver
