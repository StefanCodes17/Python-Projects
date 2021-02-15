from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', {"class": 'clearfix job-bx wht-shd-bx'})
i = 0
for job in jobs:
    comp_title = soup.find(
        'h3', {"class": 'joblist-comp-name'}).getText().strip()
    key_skills_arr = soup.find(
        'span', {"class": 'srp-skills'}).getText().strip().split(' ')
    key_skills = [skill for skill in key_skills_arr if (
        skill != '' and skill != ',' and skill != '/')]
    print(comp_title)
    print(key_skills)
