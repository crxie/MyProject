# coding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time 
from datetime import datetime
from collections import OrderedDict
import re
import requests
'''
def get_creator(project,type_='URL'):
#    header={
#        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
#        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#    }
    if type_=='project':
        URL='https://www.kickstarter.com/projects/'+project
    else:
        URL=project
    response=requests.get(URL)
    s=BeautifulSoup(response.content)
    soup=s.find('a',attrs={'data-modal-title':"About the creator"})
    creator=soup.get('href').split('/')[2]
    return creator

browser = webdriver.Chrome(r'/Users/xiechangrun/Downloads/chromedriver')

scraped_data = []
personal_data = []
now = datetime.now()
counter = 1

#browser.get('https://www.kickstarter.com/profile/ryangrepper')

for i in range(200):
    search_page ="https://www.kickstarter.com/discover/advanced?sort=end_date&seed=2431658&page=" +str(i)
    browser.get(search_page)
    
    projects = []
    proj_temp2 = []
    for project_link in browser.find_elements_by_class_name('project-title'):
        projects.append(project_link.find_element_by_tag_name('a').get_attribute('href'))
    
    for project in projects:
        time.sleep(1)
        print(str(counter)+': '+project+'\nStatus: Started.')
        project_dict = OrderedDict()
        personal_dict = OrderedDict()
        project_dict['Url'] = project
        #project_dict['Category'] = category[0]
        browser.get(project)
        soup = BeautifulSoup(browser.page_source)

        try:        
            project_dict['Name'] = browser.find_elements_by_class_name('green-dark')[0].text
        except:
            project_dict['Name'] = ''  
        try:
            mo_place = soup.find("a",{"class":"remote_modal_dialog green-dark"})
            creator = mo_place.find(text=True)
            project_dict['creator'] = creator
        except:
            mo_place = soup.find("a",{"class":"green-dark"})
            creator = mo_place.find(text=True)
            project_dict['creator'] = creator
            
        try:
            try:
                project_dict['Num_Of_Backers'] = int(browser.find_element_by_id('backers_count').text.replace(',',''))
            except:
                project_dict['Num_Of_Backers'] = int(browser.find_element_by_class_name('num h1 bold').get_attribute('data-backers-count'))            
        except:
            project_dict['Num_Of_Backers'] = int(browser.find_element_by_class_name('NS_projects__spotlight_stats').find_element_by_tag_name('b').text.replace(',','').split(' ')[0])
            
        try:
            project_dict['Currency'] = str(browser.find_element_by_id('pledged').text[0])
        except:
            project_dict['Currency'] = 'euro'
            
            #str(re.sub(',','',browser.find_element_by_class_name('money').text[0]))

        try:
            try:
                project_dict['Amount-Pledged'] = float(browser.find_element_by_id('pledged').text[1:].replace(',',''))
            except:
                project_dict['Amount-Pledged'] = str(browser.find_elements_by_class_name('mb1')[-1].text[1:].replace(',',''))
        except:
            project_dict['Amount-Pledged'] = 'NaN'
            
        try:
            try:
                project_dict['Goal'] = float(browser.find_elements_by_class_name('money')[1].text[1:].replace(',',''))
            except:
                project_dict['Goal'] = float(browser.find_elements_by_class_name('h5')[8].find_element_by_class_name('money').text[1:].replace(',',''))
        except:
            project_dict['Goal'] = 1
            
        project_dict['Success'] = int(project_dict['Amount-Pledged'] >= project_dict['Goal'])
        #project_dict['Funded Percent'] = float(project_dict['Amount-Pledged'] / project_dict['Goal'])

        try:
            project_dict['Time_Remaining'] = (browser.find_element_by_class_name('ksr_page_timer').find_element_by_class_name('num').text,
                                          browser.find_element_by_class_name('ksr_page_timer').find_element_by_class_name('text').text.split(' ')[0]) 
        except:
            project_dict['Time_Remaining'] = 0
            
        try:        
            backed_num = browser.find_element_by_xpath("//span[2]/a").text
            project_dict['backed_case_num'] = int(str(backed_num).split('b')[0])
        except:
            project_dict['backed_case_num'] = 0

        project_dict['About'] = '\n'.join([a.text for a in browser.find_elements_by_tag_name('p')[5:-3]])
        project_dict['Location'] = browser.find_elements_by_class_name('grey-dark')[1].text
        project_dict['Reward_Levels'] = '\n'.join([b.text for b in browser.find_elements_by_tag_name('h2')[5:]])
        project_dict['Num_Of_Comments'] = re.search('\d+',browser.find_elements_by_class_name('js-load-project-content')[3].text).group()
        project_dict['Num_Of_Updates'] = re.search('\d+',browser.find_elements_by_class_name('js-load-project-content')[2].text).group()
        
        #browser.find_element_by_xpath('//a[4]').click()
        #browser.find_element_by_css_selector("a.author.green-dark").click()
        #browser.find_element_by_css_selector("a.remote_modal_dialog > img.avatar-small.circle").click()    
        #browser.find_element_by_css_selector("img.avatar.circle").click()
        
        slice1 = get_creator(project) 
        personal_url = 'https://www.kickstarter.com/profile/'+str(slice1)
        browser.get(personal_url)
        copy=browser.find_elements_by_class_name("copy")
        if len(copy)>0:
            #往下滾動
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            proj_temp=browser.find_elements_by_css_selector("a.project_item.block")
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            proj_temp2=browser.find_elements_by_css_selector("a.project_item.block")
            while len(proj_temp2)>len(proj_temp):
                proj_temp=proj_temp2
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                proj_temp2=browser.find_elements_by_css_selector("a.project_item.block")

        backed_source=proj_temp2
        
        backeds=[url.get_attribute('href') for url in backed_source]
        personal_dict['backed_url'] = backeds
        personal_dict['name'] = project_dict['creator']

        

        print('Status: Done.')
        counter+=1
        scraped_data.append(project_dict)
        personal_data.append(personal_dict)

later = datetime.now()
diff = later - now

print('The scraping took '+str(round(diff.seconds/60.0,2))+' minutes, and scraped '+str(len(scraped_data))+' projects.')

print(scraped_data)
'''
df = pd.DataFrame(scraped_data)
df2 = pd.DataFrame(personal_data)
df.to_csv('kickstarter-datasss.csv',encoding='utf-8')
df2.to_csv('kickstarter-s.csv',encoding='utf-8')


