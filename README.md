# CIS598
Welcome to my senior project. To set up the environment you will need:
1. Python, https://www.python.org/
2. Xampp, https://www.apachefriends.org/index.html

Set up a virtual environment on your PC to run a django application.
Libraries you will need in your virtual environment:
1.Pandas - pip install pandas
2.MySQLClient - I have the mysqlclient wheels file included if you get an error for C++ not installed. pip install mysqlclient-1.4.4-cp38-cp38-win_amd64.whl
 while inside the folder with the mysqlclient file.
3.Django - pip install django
4.Django-cors-header (at least for this senior project) - pip install django-cors-headers

When you set up your Xampp, you will need to set your localhost password to 12345. This password is what the django application will use.
To do this start Xampp by activating xampp-control in your xampp folder. Start the Apache and MySQL services.
Go to: localhost/phpmyadmin/
Go to User Accounts and set the password of localhost to 12345.
Now when you want to access localhost/phpmyadmin again you will be unable to because of bad credentials. Don't freak out.
Go to your Xampp folder->phpMyAdmin->config.inc.php, in this file set your 'user' to root and 'password' to 12345:
  $cfg['Servers'][$i]['user'] = 'root'
  $cfg['Servers'][$i]['password'] = '12345'
  
Create a database in php my admin called "filetransferproject"
  
 With the xampp server running and before you issue the command "python manage.py runserver", issue the command "python manage.py migrate"
 This will set up your database table. Now you can issue the command "python manage.py runserver"
 Go to this link to see the website application: http://127.0.0.1:8000/storetransfer/
 
 I also included two csv file with test data that you can use for this application
 Have fun,
 Victor Ramos
