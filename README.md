# Website

Website built with Django and django-CMS

## Installation

install and activate virtual environment

```bash
pip install virtualenv
virtualenv .env
```
in Linux:

```bash
source .env/bin/activate
```
in Windows:

```bash
.env\Scripts\activate
```
then
```bash
pip install -r requirements.txt

```
## running

first migrations and then running the server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

enjoy and feel free to leave a message <3
