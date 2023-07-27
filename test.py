import json, re, requests, sys, yaml
from bs4 import BeautifulSoup

"""
Returns tech jobs for good jobs
"""
print('Finding jobs at ProPublica')

url = 'https://boards.greenhouse.io/embed/job_board?for=propublica'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

jobs = soup.find_all("div", {"class": "opening"})
print(jobs)
# for job in jobs:
#     job_url = job['href']
    
#     job_id_search = re.search('\/jobs\/(\d+)\/', job_url)
#     if job_id_search:
#         job_id = job_id_search.group(1)
#     else:
#         job_id = None
    
#     job_title = job.find_all('div')[0].text.strip()
#     job_url = url + job_id
#     job_employer = job.find_all('span', {"class": "company_name"})[0].text.strip()
#     job_location = job.find_all('span', {"class": "location"})[0].text.strip()
    
#     job_dict = {
#     'id': job_id,
#     'job_title': job_title,
#     'job_url': job_url,
#     'job_location': job_location,
#     'department1': '',
#     'department2': '',
#     }