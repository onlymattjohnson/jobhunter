import json, requests
from bs4 import BeautifulSoup

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
          'job_link': job_link,
          'department_1': department_name,
          'department_2': ''
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
            'job_link': job_link,
            'department_1': department_name,
            'department_2': sub_department_name
          }
        results.append(job_dict)

  return json.dumps(results)

if __name__ == '__main__':
  site = 'twilio'
  f = get_greenhouse_jobs(site)
  print(f)