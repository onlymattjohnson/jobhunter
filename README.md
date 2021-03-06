```
       _       __    __                __           
      (_)___  / /_  / /_  __  ______  / /____  _____
     / / __ \/ __ \/ __ \/ / / / __ \/ __/ _ \/ ___/
    / / /_/ / /_/ / / / / /_/ / / / / /_/  __/ /    
 __/ /\____/_.___/_/ /_/\__,_/_/ /_/\__/\___/_/     
/___/                                               
```

![A dog found a job](img/dog_found_job.png)

*jobhunter* is a tool to find jobs that I am specifically looking for.

This tool is free to use and modify. If you get some use out of it, or if you have any questions, I'd love to know. You can find me on [twitter](https://www.twitter.com/onlymattjohnson) or on the [web](http://onlymattjohnson.com).

## Setup

1. Clone the repo

```
git clone git@github.com:onlymattjohnson/jobhunter.git
```

2. Initialize pipenv

```
cd jobhunter
pipenv --python 3.8
pipenv install
```

## Database Setup

This application uses postgresql by default. To set up the database:

1. Open Postgres Command Line

```bash
psql
```

2. Create the database

```sql
CREATE DATABASE jobhunter;
```

3. Create a username and password for the database 

```
createuser --interactive --pwprompt
```

and follow the instructions on screen.

4. Add the new user to the jobhunter database:

```bash
psql

GRANT ALL ON DATABASE jobhunter TO {db_user};

\q
```

5. Add the username and password to a .env file:

```
JOBHUNTER_DB_USER=database_user_name
JOBHUNTER_DB_PASS=database_password
```

6. Exit and reload your environment

```bash
exit
pipenv shell
```

7. Open the python shell and create the database tables 

```python
python

from app import db 
db.create_all()
```

## Refresh jobs

1. Run the tasks app to load new jobs

```bash
pipenv run python tasks.py
```

## Launch Development Web Page

1. Launch the webserver

```bash
pipenv run python app.py
```

2. View site at `http://127.0.0.1:5000/` in a browser.