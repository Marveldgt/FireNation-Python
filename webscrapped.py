from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

def web_scrapped():
    #get the text source code from the website
    html_= requests.get('https://realpython.github.io/fake-jobs/').text
    
    soup= BeautifulSoup(html_,'lxml')
    #filter out each card 
    cards= soup.find_all('div', class_='card')
    
    L=[]
    #get info about  jobs in each card
    for card in cards:
        job= card.find('div',class_="media-content")
        job_title= job.h2.text
        comp_name= job.h3.text
        loc_header= card.find('div',class_='content')
        location= loc_header.p.text.strip()
        date= loc_header.find('p',class_='is-small has-text-grey').text.strip()
        
        #get links
        links=card.find('footer', class_='card-footer')
        link_sub=links.find_all('a',class_='card-footer-item')
        learn_link= link_sub[0]['href']
        description_link= link_sub[1]['href']
        
        #append all details to an empty list
        L.append([job_title,comp_name,location,date,learn_link,description_link])
        
    Data= pd.DataFrame(L,columns=['Job_title','Company_name','Location','Date_posted','Learn_link','Job_description_link'])
    
    #Parse dates using datetime module
    Data['Date_posted_parsed']= pd.to_datetime(Data['Date_posted'],format='%Y-%m-%d')
    
    del Data['Date_posted']
    Data.to_csv('data_from_webscrapped_page.csv')
    
    print('saved')
    
if __name__== '__main__':
    web_scrapped()
    
    
print(pd.read_csv('data_from_webscrapped_page.csv',index_col=0))
     
