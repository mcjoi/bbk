# parser.py
import requests
from bs4 import BeautifulSoup

range = range(0, 828)
mytitles = []

f = open("c:\\Users\\bong\\Desktop\\code\\py_pjt\\bbk\\bbk\\url.txt", 'w')

for i in range:
    
# HTTP GET Request
    url = 'https://sunnybong.tistory.com/' + str(i)
    
    response = requests.get(url)
    status_code = response.status_code
    
    if status_code < 300 and status_code >= 200 :
        f.write(url + '\n')
        print(url + ' Passed')

f.close()
print('Completed')
