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
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
there are 5 templates :
``` text
about.html
blog.html
home.html
media.html
portfolio.html
```
if you want to make About Us page then it's slug must be ```/about``` . you can change its template in ``` comment/about.html```

```home.html``` is for Homepage and three others can use aldryn_newsblog app with different configurations.

you can use search placeholder with article_search plugin in ```blog``` and ```media``` pages.


enjoy and feel free to leave a message <3
