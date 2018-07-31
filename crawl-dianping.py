import urllib
import re
import os
import shutil
import sys
import importlib
importlib.reload(sys)
host = 'http://www.dianping.com'
#define UA headers
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
headers = {'User-Agent':user_agent}
key_word = '南坪'                                      #keyword search in the website
city_num = str(9)                                     #Chonqing's city code is 9, others can be found in dianping's URL
directory = city_num + '\\' + key_word       #create directory
if os.path.exists(directory):
    shutil.rmtree(directory)
    os.makedirs(directory)  #delect existed directory
    print ('delete existed directory successfully')
else:
    os.makedirs(directory)
    print ('create directory successfully')
url = host + '/search/keyword/' + city_num  # write URL as patterned
def getDocument(page):
    page = str(page)
    path_name = directory + '\\page_' + page + '.txt'
    file = open(path_name, 'w+',encoding='utf-8'); #create file
    #need to transcode as the key is Chinese
    real_url = url + '/' + '0_' + urllib.request.pathname2url(key_word) + '/p' + page
    request = urllib.request.Request(real_url, headers = headers)                               #send request
    response = urllib.request.urlopen(request)                                                  #get response
    document = response.read().decode('utf-8')                                         #decode the website using utf-8
    items_name = re.findall(r'data-hippo-type="shop"\stitle="([^"]+)"', document, re.S)  #using regex to match the name of shop
    items_address = re.findall(r'<span\sclass="addr">([^\s]+)</span>', document, re.S)   #using regex to match the address of shop
    result = ''
    for index in range(len(items_name)):
        result += items_name[index] + '\n'
    file.write(result)                                                                   #save the result to file
    file.close()
    print ('Complete!')
def start_crawl():
    for index in range(0, 15):
        getDocument(index)         #set the number of page want to crawl
start_crawl() 
