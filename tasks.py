import json, requests
from bs4 import BeautifulSoup

def get_greenhouse_jobs(site_name):
  """
  Returns jobs from Greenhouse
  """
  results = {}

  base_url = 'https://boards.greenhouse.io'
  url = f'{base_url}/{site_name}/'
  r = requests.get(url)

  soup = BeautifulSoup(r.content, 'html5lib')

  departments = soup.findAll('section', {'class': 'level-0'})
  for department in departments:
    department_name = department.find('h3').text
    results[department_name] = {'jobs': [], 'departments': {}}
    jobs = department.findChildren('div', {'class': 'opening'}, recursive = False)
    for job in jobs:
      job_title = job.find('a').text
      job_link = job.find('a')['href']
      job_link = f'{base_url}{job_link}'
      job_dict = {'job_title': job_title, 'job_link': job_link}
      if 'jobs' in results[department_name]:
        results[department_name]['jobs'].append(job_dict)
      else:
        results[department_name]['jobs'] = [job_dict]

    sub_departments = department.findChildren('section', {'class': 'level-1'})
    for sub_department in sub_departments:
      sub_department_name = sub_department.find('h4').text
      results[department_name]['departments'][sub_department_name] = {}
      jobs = sub_department.findChildren('div', {'class': 'opening'}, recursive = False)
      for job in jobs:
        job_title = job.find('a').text
        job_link = job.find('a')['href']
        job_link = f'{base_url}{job_link}'
        job_dict = {'job_title': job_title, 'job_link': job_link}

        if 'jobs' in results[department_name]['departments'][sub_department_name]:
          results[department_name]['departments'][sub_department_name]['jobs'].append(job_dict)
        else:
          results[department_name]['departments'][sub_department_name]['jobs'] = [job_dict]

  return json.dumps(results)

if __name__ == '__main__':
  site = 'twilio'
  f = get_greenhouse_jobs(site)
  print(f)