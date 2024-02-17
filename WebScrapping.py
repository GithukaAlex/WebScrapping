#!/usr/bin/env python
# coding: utf-8

# In[7]:


from bs4 import BeautifulSoup as bs
import requests
import pandas

'https://books.toscrape.com/catalogue/page-46.html'

'https://books.toscrape.com/'


# In[61]:


html_page = requests.get('https://books.toscrape.com/')
soup = bs(html_page.content, 'html.parser')


# In[62]:


soup.prettify


# In[13]:


type(soup.find_all('li', {'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}))


# In[40]:


# All elements:
all = soup.find_all('li', {'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
all


# In[17]:


# To show the first item
f = soup.find_all('li', {'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})[0]
f


# In[23]:


f.find_all('a')


# In[20]:


f.find('a')


# In[19]:


# to get the URL, Title, Price , Instock and the rating

#URL
f.find('a')['href']


# In[22]:


# TO find the title
f.find('h3').find('a')['title']


# In[26]:


# to find the price
f.find('p', {'class': 'price_color'}).text


# In[29]:


# Find instock

f.find('p',{'class': 'instock availability'}).text


# In[31]:


# TO find the rating

import re
regex  = re.compile('star-rating (.*)')
f.find('p', {'class' : regex})


# In[33]:


f.find('p',{'class': regex})['class'][-1] 


# In[38]:


def cleaning(book):
    info = {}
    info['title'] = book.find('h3').find('a')['title']
    info['price'] = book.find('p', {'class': 'price_color'}).text
    if 'In stock' in f.find('p',{'class': 'instock availability'}).text:
        info['instock'] = True
    else:
        info['instock'] = False
    info['stars'] = book.find('p',{'class': regex})['class'][--1]
    info['url'] = 'http://books.toscrape.com/' + book.find('a')['href']
    return info


# In[41]:


cleaning(f)


# In[45]:


all_dict = [cleaning(book) for book in all]
all_dict


# In[46]:


pd.DataFrame(all_dict)


# # Scraping multiple pages (Pagination!)

# In[48]:


url = 'https://books.toscrape.com/catalogue/page-2.html'


# In[50]:


# Urls for all the other pages
urls = ['https://books.toscrape.com/catalogue/page-{}.html'.format(i) for i in range (1,51)]
urls


# In[66]:


# To get the 20 books for each page

def get_20_books(url):
    html_page = requests.get(url)
    soup = bs(html_page.content, 'html.parser')
    
    raw = soup.find_all ('li' ,{'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
    to_dicts = [cleaning(book) for book in raw]
    
    return to_dicts
    


# In[67]:


get_20_books('https://books.toscrape.com/')


# In[68]:


all_dicts = []

for url in urls:
    all_dicts.extend(get_20_books(url))
    
all_dicts    


# In[69]:


df = pd.DataFrame(all_dicts)

df.head()

