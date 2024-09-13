from bs4 import BeautifulSoup
import requests

print("Enter skills you are unfamiliar with (separate with commas): ")
unfamiliar_skills = input('>').split(',')

# Trim spaces from each skill
unfamiliar_skills = [skill.strip().lower() for skill in unfamiliar_skills]
print(f"Filtering Skills: {unfamiliar_skills}")


html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text

soup=BeautifulSoup(html_text, 'lxml')
jobs=soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')
for job in jobs:
    Published_Date=job.find('span', class_ ='sim-posted').span.text
    # we have used if condition so that it should only display that post which copntians only "few' days not from a long time  
    if 'few' in Published_Date:
     company_name=job.find('h3', class_ ='joblist-comp-name').text.replace(' ', '')
    #we are only finding the company name that is conatined insibe the varibale we have created as job
     skills=job.find('span',class_='srp-skills').text.replace(' ','')
     More_Info=job.header.h2.a['href']
     if not any(skill in skills for skill in unfamiliar_skills):
        
    #we have created a nested link so that we can get more info about the job 
    # f is used so that it should display the name of the company to which company_name is reffering 
      print(f'COMPANY NAME: {company_name.strip()}')
      print(f'SKILLS:  {skills.strip()}')
      print(f'More Info: {More_Info}')
    
      print("")






