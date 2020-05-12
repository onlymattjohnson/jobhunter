import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_user = os.environ.get('JOBHUNTER_DB_USER', None)
db_pass = os.environ.get('JOBHUNTER_DB_PASS', None)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user}:{db_pass}@localhost/jobhunter'
db = SQLAlchemy(app)

class Job(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  employer_name = db.Column(db.String)
  job_id = db.Column(db.String)
  job_title = db.Column(db.String)
  job_url = db.Column(db.String)
  job_location = db.Column(db.String)
  department1 = db.Column(db.String)
  department2 = db.Column(db.String)
  first_seen = db.Column(db.Date)
  last_seen = db.Column(db.Date)
  status = db.String(1)

  def __repr__(self):
    return f'<Job Posting {self.employer_name} ({self.job_id}) : {self.job_title}'

@app.route('/')
def index():
  return '<h1>Hello world</h1>'

if __name__ == '__main__':
  app.run()

