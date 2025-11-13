****Migration***

# Git clone method:- git clone repo_name.git

1.	node-app-  https://github.com/nvlinh99/simple-todo-app


# Windows:
-	Clone the repository
-	NodeJs installation – through windows powershell winget install OpenJS.NodeJS
-	Check for node and npm versions 
o	node -v
o	npm -v
-	Open proj in vs and navigate to the app folder through cmd
-	npm init -y
-	npm install express
-	node app.js
-	localhost: 3000


# Ubuntu:
-	sudo apt update
-	sudo apt install -y nodejs npm
-	node -v
-	npm -v
-	navigate to project through cmd
-	npm install
-	npm install express
-	node app.js



2.	Simple python app- number guessing game--

# Windows
# Clone the repository
- git clone https://github.com/Python-World/python-mini-projects.git

# Navigate to projects
- cd python-mini-projects\projects

# Find a simple game (like number guessing)
- cd number_guessing_game

# Install Python (if not installed)
# Download from python.org

# Run the game directly
- python main.py                            


# Ubuntu setup
# Navigate to directory
- cd /home/student/docker_lab6

# Install Python (if not installed)
- sudo apt update
- sudo apt install -y python3

# Make Python files executable
- chmod +x main.py

# Run the applications 
- python3 main.py



3.	Python flask app
# Windows:
Create a folder and inside it create a file app.py(paste the above code in it)
-	Cd to the app folder
-	Then install flask pip install flask
-	Python app.py
-	Test the app on localhost: 5000
      Ubuntu:
-	sudo apt update
-	sudp apt install -y python3 python3-pip
-	pip install flask / pip3 install flask
-	python3 app.py

App.py-

from flask import Flask, request, redirect

app = Flask(__name__)

# Simple list to store todos (in memory)
todos = []

@app.route('/')
def home():
    # Simple HTML as string - no templates needed
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Todo App</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { color: #333; }
            form { margin-bottom: 20px; }
            input[type="text"] { padding: 10px; width: 300px; }
            button { padding: 10px 15px; background: #28a745; color: white; border: none; cursor: pointer; }
            .todo-item { background: #f8f9fa; padding: 10px; margin: 5px 0; border-left: 4px solid #007bff; }
            .completed { text-decoration: line-through; color: #6c757d; border-left-color: #6c757d; }
            .actions { margin-top: 5px; }
            .actions a { margin-right: 10px; padding: 5px 10px; text-decoration: none; border-radius: 3px; }
            .complete { background: #007bff; color: white; }
            .delete { background: #dc3545; color: white; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✅ Simple Todo App</h1>
            
            <form method="POST" action="/add">
                <input type="text" name="task" placeholder="Enter a new task" required>
                <button type="submit">Add Task</button>
            </form>
            
            <h3>Your Tasks:</h3>
    """
    
    # Add todos to HTML
    if not todos:
        html += "<p>No tasks yet. Add your first task above!</p>"
    else:
        for i, todo in enumerate(todos):
            status = "completed" if todo['done'] else ""
            html += f"""
            <div class="todo-item {status}">
                <div>{todo['task']}</div>
                <div class="actions">
                    <a class="complete" href="/toggle/{i}">{"Undo" if todo['done'] else "Complete"}</a>
                    <a class="delete" href="/delete/{i}">Delete</a>
                </div>
            </div>
            """
    
    html += """
        </div>
    </body>
    </html>
    """
    return html

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        todos.append({'task': task, 'done': False})
    return redirect('/')

@app.route('/toggle/<int:index>')
def toggle_todo(index):
    if 0 <= index < len(todos):
        todos[index]['done'] = not todos[index]['done']
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


4.	Python Django-blog app
# Windows 
# Clone the repository
-	git clone https://github.com/bradtraversy/djangocrashcourse.git
-	cd djangocrashcourse
# Create virtual environment
-	python -m venv venv

# Activate virtual environment
-	venv\Scripts\activate

# Upgrade pip 
-	python -m pip install --upgrade pip

# Install dependencies
-	pip install django
-	pip install django mysqlclient
--------------------------------------------------------------------------------------------
-	Fix Settings (IMPORTANT)
-	Edit djangoproject/settings.py:
-	python
-	# Remove or comment out this line if it exists:
-	# import pymysql
-	
-	# Ensure DATABASES section has correct password:
-	DATABASES = {
-	    'default': {
-	        'ENGINE': 'django.db.backends.mysql',
-	        'NAME': 'djangoproject',
-	        'USER': 'root',
-	        'PASSWORD': 'root',  # Your MySQL password
-	        'HOST': 'localhost',
-	        'PORT': '3306'
-	    }
-	}
-	--------------------------------------------------------------------------------------------
-	mysql -u root -p
-	enter your mysql password- “root”
sql> create database djamgoproject
sql> exit

-	python manage.py migrate
-	Create super user python manage.py createsuperuser
-	Enter credentials 
	Username: admin
	Email: admin@eg.com
	Password: admin@123
-	Python manage.py runserver
-	Localhost: 8080
Settings.py –
"""
Django settings for djangoproject project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

- Edit settings.py -
-----------------------------------------
import os
# import pymysql
# pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j&2ib&(a&)t)^%pw*u0ym8@2v3*i4du)l5pdw!q-xdpurg4fhn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'posts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoproject.wsgi.application'
-----------------------------------------

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoproject',
        'USER': 'root',
        'PASSWORD': 'Asq4l6f@5dZy004',  # ← Change this to the password you just used
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'






# Ubuntu:
          # Update system
-	sudo apt update
-	sudo apt upgrade -y
-	
# Install Python, pip, virtual environment
-	sudo apt install -y python3 python3-pip python3-venv

           # Install MySQL server and client
-	sudo apt install -y mysql-server mysql-client
-	
# Install MySQL development libraries (required for mysqlclient)
-	sudo apt install -y python3-dev default-libmysqlclient-dev build-essential

# Secure MySQL installation (set root password)
sudo mysql_secure_installation

# Login to MySQL and create database
sudo mysql -u root -p

CREATE DATABASE djangoproject;
EXIT;

# Navigate to project directory
cd /home/student/python_lab18/djangocrashcourse

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install django mysqlclient
	
# Edit djangoproject/settings.py on Ubuntu:
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoproject',
        'USER': 'root',
        'PASSWORD': 'your_mysql_root_password',  # Password you set in mysql_secure_installation
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
# Run migrations
python3 manage.py migrate

# Create superuser
python3 manage.py createsuperuser

# Run server (accessible from network)
python3 manage.py runserver 0.0.0.0:8000













5.	PHP Projects:

***PHP Projects****

- Git Repositories
Simple PHP Project: https://github.com/banago/simple-php-website

- Backend Form PHP Project: https://github.com/chapagain/crud-php-simple

# Windows Setup
Xampp Installation:

- Download Xampp: https://www.apachefriends.org/download.html

- If error occurred saying "Port 3306 is used" then End Task for Mysqld.exe from Task Manager

Search for Xampp on windows and start the Xampp Control Panel

Click on Start button to start services of Apache & Mysql (Both should be in green color)

Project Setup:

Extract the projects in C:\Xampp\htdocs

Copy the name of simple PHP project application

Open Browser type localhost/simple-php-website then hit enter to run the project

Backend Project Setup:

Repeat step 2 for the Backend project

It will show error in file dbConnection.php

Open crud-php-simple project in VS code, open dbConnection.php file

Enter your databasePassword = ''

Open database.sql file from that project and copy the command of create table users

Open Xampp Control Panel, click on the admin button to open phpMyAdmin page

Inside Test DB click SQL, paste that query and click GO Button (Bottom Right Corner)

It will create users table inside test db

Now open Browser type localhost/crud-php-simple then hit enter to run the project

# Ubuntu Setup

## Simple Form app

1. sudo apt update
2. sudo apt install openssh-server
3. sudo apt install php
4. php --version
5. sudo apt install apache2
6. sudo apt install libapache2-mod-php
7. sudo cp -r /home/imcc/PHP-MySQL-User_Login_System(project name)    /var/www/html/
8. sudo mv /var/www/html/index.html  /var/www/html/index.back
9. sudo cp /home/imcc/project_complete_path/index.php  /var/www/html/

## Crud app
## Linux (Terminal):
bash
Copy
- sudo apt update && sudo apt install apache2 mysql-server php libapache2-mod-php php-mysql gi

- sudo mysql_secure_installation


# Set root pass: root123
- sudo mysql -u root -p
> CREATE DATABASE student_db;
> CREATE USER 'phpuser'@'localhost' IDENTIFIED BY 'php123';
> GRANT ALL ON student_db.* TO 'phpuser'@'localhost';
> EXIT;

- cd /home/student

- mkdir php_app_lab2 && cd php_app_lab2
- git clone https://github.com/php-lab/simple-php-crud-app.git
- sudo cp /var/www/html/
- sudo nano /var/www/html/config.php # - Update DB creds

- mysql -u phpuser -p student_db < database/student_db.sql
- sudo chown -R www-data:www-data/var/www/html/
→ Open http://localhost
 

6.	Java Project Expenses Tracker

# Windows:

1. Open the URL - http://192.168.23.239:9000/
2. Download Expenses-Tracker-WebApp to your local PC
OR Git clone : https://github.com/mohamed0sawy/Expenses-Tracker-WebApp#
3. On VSCode open the file src/main/resources/application.properties
4. Change the mysql username password to you PC's mysql username password. (college username and password: root, root)
5. Open Command Prompt and ensure Java is install using the command "java -version"
6. Download and install Apache Maven from this URL : https://medium.com/@gauravshah97/how-to-install-maven-on-windows-39ff317e40cf
	i. add path of maven into system variables -> click on new -> variable name = MAVEN_HOME, and variable value = path -> ok
	ii. click on path in system variables -> add new path -> %MAVEN_HOME%\bin -> ok -> ok -> ok
7. Create a database called "expenses_tracker" in your mysql DB
8. Go to your projects directory and Run the command "mvn clean install"
9. Run the command "java -jar target/expenses-tracker.jar" -> The jav file name could be different on your machine, please update the name accordingly.
10. Open http://localhost:8080 to see the app deployed.
11. Install Filezilla on Windows if its not installed yet.

# Ubuntu:
12. Start Ubuntu on virtualbox
13. Stop your Windows java application by Ctrl+z
15. On Windows find your IP address for the windows machine using ipconfig command. It should be "192.168.xxx.xxx"
16. Open the application.properties file again and replace the DB hostname from localhost to this ipaddress from step 15
17. Rebuild the application from Windows using the command "mvn clean install"
18. Run the command "java -jar target/expenses-tracker.jar"
18. See if the application is still accessible from localhost:8080
19. Install openssh-server on Ubuntu with the command "sudo apt install openssh-server".
	I. Password for openssh-server- imcc@123
Ubuntu IP address command "ip addr"
i.	Go to filezilla on the top add -> host: ip of ubuntu machine, username: imcc, password: imcc@123, port: 22
ii.	Click on Quick connect.
iii.	Drag and drop your project folder from local site to remote site.
14. Move the project folder from Windows to Ubuntu using filezilla /
Copy the generated new generated jar file from targets folder to the Ubuntu machine using filezilla 

20. Install Java on Ubuntu using the command "sudo apt install openjdk-21-jdk"
21. Now from the folder where you jar is copied on Ubuntu, run the command "java -jar filename.jar"
20. Run command sudo apt install mysql-server
21. create database expences_tracker; 
22. On ubuntu start mysql using the command "sudo mysql -u root"
23. Create a new mysql user using the following commands
CREATE USER 'admin'@'%' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
24. Note: If there is any error with db- change the username and password to “admin” in ubuntu application.properties file.
24. Go to the folder where you have copied the application.
25. Run the command "sudo apt install maven"
26. mvn --version
28. mvn clean install
29. java -jar target/appfile-name.jar

🪟 WINDOWS Setup (Step-by-Step)

1. Install Ruby
•	Download Ruby installer (with DevKit) from:
👉 https://rubyinstaller.org/downloads/
•	Example: Choose  Ruby+Devkit 3.4.7-1 (x64) 

•	During installation:
o	✅ Check “Add Ruby executables to your PATH”
o	✅ Let it run ridk install at the end — choose option 3 (to install MSYS2 and development tools).
________________________________________
2. Verify Ruby & Gem
ruby -v
gem -v
You should see Ruby and gem versions.
________________________________________
3. Install Bundler
gem install bundler
________________________________________
4. Clone the Repository
cd C:\cloud_migration
mkdir ruby_sinatra_microServices
cd ruby_sinatra_microServices
git clone https://github.com/JHero23/ruby-sinatra-starter-app.git
cd ruby-sinatra-starter-app
________________________________________
5. Install Dependencies
gem install sinatra
gem install rack
gem install thin
gem install sinatra-contrib
gem install rackup
gem install puma
bundle install
💡 If bundle install gives an error like missing Gemfile, you can skip it — this repo might not have one.
________________________________________
6. Run the App
ruby app.rb
If everything is correct, you should see:
== Sinatra (v4.x.x) has taken the stage on 4567 for development
Then open your browser and go to:
👉 http://localhost:4567
________________________________________

🐧 UBUNTU Setup (Step-by-Step)
Now for your Ubuntu EC2 or local Ubuntu 22.04 system:
1. Update Packages
sudo apt update -y
sudo apt upgrade -y
________________________________________
2. Install Ruby and Git
sudo apt install ruby-full git -y
________________________________________
3. Check Versions
ruby -v
gem -v
________________________________________
4. Install Bundler
sudo gem install bundler

________________________________________
6. Install Required Gems
sudo gem install sinatra
sudo gem install rack
sudo gem install thin
sudo gem install sinatra-contrib
sudo gem install rackup
sudo gem install puma
bundle install
________________________________________
7. Run the App
ruby app.rb
If the app runs successfully, you’ll see output like:
== Sinatra (v4.x.x) has taken the stage on 4567 for development
Access from browser (if running locally):
👉 http://localhost:4567


