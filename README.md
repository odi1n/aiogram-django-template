# Aiogram-Django Template

## Documentation lib
1. [Aerich](readme/aerich.md)
2. [Tortoise](readme/tortoises.md)

## Installation

#### 1. Clone the Template:
   * `git clone https://github.com/MaximZayats/aiogram-django-template`

#### 2. Install Requirements 
   * `pip install -r requirements.txt`

#### 3. Change Config:
   * Go to the `application/`
   * Rename `.env.dist` to `.env`
   * Insert your values

#### 4. Make migrations:
   * Go to the `application/`
   * Run `python manage.py makemigrations`
   * Run `python manage.py migrate`
   
#### 5. Run bot:
   * `python manage.py runbot`

#### 6. Run server (Django):
   * Collect static: `python manage.py collectstatic`
   * Run server: `python manage.py runserver`

#### 7. Run app _(Bot + Server)_:
   * `python manage.py runapp` or `python app.py`

## Usage

#### 1. Create new app
   * `python manage.py startapp APP_NAME`
      * Apps are created using a template: `application/config/app_template`
      * You can use your template: `python manage.py startapp APP_NAME --template TEMPLATE_PATH`
   
#### 2. Register app
   * Import and Add app to `INSTALLED_APPS` in `config/apps.py`
   * Register (include) app urls in `config/web/urls.py`   

#### 3. Check your app
   * Run bot
   * Type `/apps`:
      * You should get a list of all your apps
   * Type `/APP_NAME`:
      * You should get a message from your app
