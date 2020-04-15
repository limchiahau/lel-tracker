#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request as request
from bs4 import BeautifulSoup
import operator
import time
import os
import datetime
import sys
import pathlib


# In[2]:


TRACK_FILE = pathlib.Path('lel.track')


# In[3]:


get_text = operator.methodcaller('get_text')


# In[4]:


class Day:
    def __init__(self, date, events):
        self.date = date
        self.events = events
        
    @classmethod
    def from_soup(cls, soup):
        date = soup.find(class_='trace__date')
        date = cls.date_str(date)
        
        times = soup.find_all(class_ ='.trace__time')
        times = map(get_text, times)
        
        actions = soup.find_all(class_='trace__event-value')
        actions = map(get_text, actions)
        
        events = [Event(time,action) for time, action in zip(times,actions)]
        
        return cls(date,events)
    
    
    def __str__(self):
        output =  f'{self.date}\n\n'
        output += '\n'.join(map(str,self.events))
        return output
    
    @staticmethod
    def date_str(html_element):
        remove_linebreak = operator.methodcaller('replace', '\n', '')
        remove_tab = operator.methodcaller('replace',' ','')

        return remove_tab(remove_linebreak(get_text(html_element)))


# In[5]:


class Event:
    def __init__(self, time, action):
        self.time = time
        self.action = action
        
    def __str__(self):
        return f'{self.time}: {self.action}'


# In[6]:


def get_days(soup):
    days = soup.find_all(class_='trace__date_row')
    return map(Day.from_soup, days)


# In[7]:


def minutes(n):
    return 60 * n


# In[8]:


def show_tracking_data(tracking_number):
    req = request.Request(f'https://tracker.lel.asia/tracker?trackingNumber={tracking_number}&lang=en-US')
    response = request.urlopen(req)
    soup = BeautifulSoup(response,features='html.parser')
    days = get_days(soup)

    print('\n\n'.join(map(str,days)))


# In[9]:


def main():
    tracking_number = get_tracking_number()
    
    while True:
        os.system('clear')
    
        print(f'Showing tracking data for: {tracking_number}\n\n\n')
        show_tracking_data(tracking_number)
    
        print('\n\n')
        print(f'Updated: {datetime.datetime.now()}')
    
        time.sleep(minutes(5))    


# In[10]:


def get_tracking_number():
    # passed in as an argument
    try:
        tracking_number = sys.argv[1] if '-f' not in sys.argv[1] else None #allow this script to be runned properly in jupyter.
    except:
        tracking_number = None
    
    #if there is a track file
    if not tracking_number and TRACK_FILE.is_file():
        #check if there is a tracking number in the track file
        tracking_number = TRACK_FILE.read_text()
    
    #if there is an argument passed in to this script
    #or there is a non-empty track file.
    if not tracking_number:
        #ask user for tracking number
        tracking_number = input('Please provide a tracking number:\n')
    
    return tracking_number


# In[ ]:


main()


# In[ ]:




