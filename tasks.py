import json, requests, sys, yaml
from bs4 import BeautifulSoup
from app import db, Job

def get_greenhouse_jobs(site_name):
  """
  Returns jobs from Greenhouse
  """
  results = []

  base_url = 'https://boards.greenhouse.io'
  url = f'{base_url}/{site_name}/'
  r = requests.get(url)

  soup = BeautifulSoup(r.content, 'html5lib')

  departments = soup.findAll('section', {'class': 'level-0'})
  for department in departments:
    department_name = department.find('h3').text
    jobs = department.findChildren('div', {'class': 'opening'}, recursive = False)
    for job in jobs:
      job_title = job.find('a').text

      job_link = job.find('a')['href']
      job_link = f'{base_url}{job_link}'

      job_location = job.find('span', {'class': 'location'}).text

      job_id = job_link.rsplit('/', 1)[-1]
      
      job_dict = {
          'id': job_id,
          'job_title': job_title,
          'job_url': job_link,
          'job_location': job_location, 
          'department1': department_name,
          'department2': ''
        }
      results.append(job_dict)

    sub_departments = department.findChildren('section', {'class': 'level-1'})
    for sub_department in sub_departments:
      sub_department_name = sub_department.find('h4').text
      jobs = sub_department.findChildren('div', {'class': 'opening'}, recursive = False)
      for job in jobs:
        job_title = job.find('a').text

        job_link = job.find('a')['href']
        job_link = f'{base_url}{job_link}'

        job_location = job.find('span', {'class': 'location'}).text

        job_id = job_link.rsplit('/', 1)[-1]

        job_dict = {
            'id': job_id,
            'job_title': job_title,
            'job_url': job_link,
            'job_location': job_location, 
            'department1': department_name,
            'department2': sub_department_name
          }
        results.append(job_dict)

  return json.dumps(results)

def get_zapier_jobs():
  """
  Returns zapier jobs
  """

  results = []

  url = 'https://zapier.com/jobs/feeds/latest/'
  r = requests.get(url)

  soup = BeautifulSoup(r.content, 'xml')

  jobs = soup.findAll('item')

  for job in jobs:
    job_id = job.find('guid').text
    job_title = job.find('title').text
    job_url = job.find('link').text

    job_dict = {
      'id': job_id,
      'job_title': job_title,
      'job_url': job_url,
      'job_location': 'Remote',
      'department1': '',
      'department2': ''
    }
    results.append(job_dict)

  return json.dumps(results)

def check_if_exists(employer_name, job):
  """
  Checks for an object existing
  """
  result = True
  exists = Job.query.filter_by(job_id = job['id'], employer_name = employer_name).first()
  if not exists:
    result = False
  return result

def load_job_to_database(employer_name, job):
  j = Job(
        employer_name = employer_name,
        job_id = job['id'],
        job_title = job['job_title'],
        job_url = job['job_url'],
        job_location = job['job_location'],
        department1 = job['department1'],
        department2 = job['department2']
      )
  if check_if_exists(employer, job):
    pass
  else:
    db.session.add(j)
  db.session.commit()

if __name__ == '__main__':
  current_module = sys.modules[__name__]
  with open('employers.yaml', 'r') as stream:
    try:
      y = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)

  for task_run in y:
    category_name = task_run['category']
    print(f'Loading jobs for {category_name}...')
    func = task_run['function']
    func = getattr(current_module, func)
    
    # If this is a category that has employers
    # run through them here
    if 'employers' in task_run:
      for employer in task_run['employers']:
        print(f'\tFinding jobs at {employer}...')
        jobs = func(employer)
        for job in json.loads(jobs):
          load_job_to_database(employer, job)

        with open(f'{employer}.json', 'w') as file:
          file.write(jobs)
    else: 
    # This is a section with no employers
    # so just pull it in as a one-off function
      jobs = func()
      with open(f'{category_name}.json', 'w') as file:
        file.write(jobs)

  