# ToDo-WebApplication

### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
$ https://github.com/amitsaini4556/ToDo-WebApplication.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide
```bash
# Additional Requirments
pip install validate_email
pip install django-q

```
Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
$ python manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
$ python manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
$ python manage.py runserver
```

```bash
# For start the scheduled tasks run below command in new Command Promt
$ python manage.py qcluster
```
Once the server is hosted, head over to http://127.0.0.1:8000 for the App.
```bash
# List of features in ToDo List
- Add Task
- Edit Task
- Done Task
- Delete Task
# User Management
- SignIn
- SignOut
- SignUp
- Forget Password
# Task Schedular
- Email send for each due tasks
```
#### Main Screen
<img src="https://user-images.githubusercontent.com/54165387/120109997-7a366e80-c189-11eb-923a-48d2be910bbf.png" alt="android" width="500" height="500"/>
