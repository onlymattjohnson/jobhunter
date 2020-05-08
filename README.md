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

3. Connect to the database 

```bash
\c jobhunter
```

4. Run the SQL to create the base table [jobhunter_schema.sql](jobhunter_schema.sql)

```sql
CREATE TABLE jobs (
   id UUID PRIMARY KEY,
   employer VARCHAR(500),
   job_id VARCHAR(100),
   job_title VARCHAR(500),
   job_url VARCHAR(500),
   job_location VARCHAR(500),
   department1 VARCHAR(500),
   department2 VARCHAR(500),
   first_seen DATE DEFAULT CURRENT_DATE,
   last_seen DATE DEFAULT CURRENT_DATE,
   post_status VARCHAR(1)
);
```

5. Exit from the database

```bash
\q
```