from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are familiar with')
familiar_skill = input('>')
print(f'filtering {familiar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        time_posted = job.find('span',class_ = 'sim-posted').span.text
        if 'few' in time_posted:
            company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if familiar_skill in skills:
                with open(f'posted/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Skill: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                    f.write('')
                print(f'File Saved: {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting time: {time_wait} minutes...')
        time.sleep(time_wait * 60)
        