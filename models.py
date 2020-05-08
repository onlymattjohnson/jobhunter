import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String


db_user = os.environ.get('JOBHUNTER_DB_USER', None)
db_pass = os.environ.get('JOBHUNTER_DB_PASS', None)
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_pass}@localhost/jobhunter', echo = True)

Base = declarative_base()

class Job(Base):
  __tablename__ = 'jobs'

  id = Column(Integer, primary_key = True)
  employer_name = Column(String)
  job_id = Column(String)
  job_title = Column(String)
  job_url = Column(String)
  job_location = Column(String)
  department1 = Column(String)
  department2 = Column(String)
  first_seen = Column(Date)
  last_seen = Column(Date)
  status = String(1)

def create_tables():
  Base.metadata.create_all(engine)

