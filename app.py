import os
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
load_dotenv()

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
  created_on = db.Column(db.DateTime, server_default = db.func.now())
  updated_on = db.Column(db.DateTime, server_default = db.func.now())
  job_status = db.Column(db.String(1))

  def __init__( self, 
               employer_name = None, 
               job_id = None, 
               job_title = None,
               job_url = None,
               job_location = None,
               department1 = None,
               department2 = None,
               job_status = 'A'
              ):
    self.employer_name = employer_name
    self.job_id = job_id
    self.job_title = job_title
    self.job_url = job_url
    self.job_location = job_location
    self.department1 = department1
    self.department2 = department2
    self.job_status = job_status

  def __repr__(self):
    return f'<Job Posting {self.employer_name} ({self.job_id}) : {self.job_title}'

@app.route('/')
def index():
  active_jobs = Job.query.filter_by(job_status = 'A').order_by(Job.created_on.desc()).all()
  return render_template('recent_jobs.html', jobs = active_jobs)

if __name__ == '__main__':
  app.run()

