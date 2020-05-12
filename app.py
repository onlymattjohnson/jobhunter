import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_user = os.environ.get('JOBHUNTER_DB_USER', None)
db_pass = os.environ.get('JOBHUNTER_DB_PASS', None)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user}:{db_pass}@localhost/jobhunter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
  created_on = db.Column(db.Date, server_default = db.func.now())
  updated_on = db.Column(db.Date, server_default = db.func.now())
  status = db.String(1)

  def __init__( self, 
               employer_name = None, 
               job_id = None, 
               job_title = None,
               job_url = None,
               job_location = None,
               department1 = None,
               department2 = None,
               status = 'A'
              ):
    self.employer_name = employer_name
    self.job_id = job_id
    self.job_title = job_title
    self.job_url = job_url
    self.job_location = job_location
    self.department1 = department1
    self.department2 = department2
    self.status = status

  def __repr__(self):
    return f'<Job Posting {self.employer_name} ({self.job_id}) : {self.job_title}'

@app.route('/')
def index():
  return '<h1>Hello world</h1>'

if __name__ == '__main__':
  app.run()

