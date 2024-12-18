# parser.py
import requests
from bs4 import BeautifulSoup

range = range(0, 828)
mytitles = []

f = open("c:\\Users\\bong\\Desktop\\code\\py_pjt\\bbk\\bbk\\name.txt", 'w')

for i in range:
    
# HTTP GET Request
    req = requests.get('https://sunnybong.tistory.com/' + str(i))
    
# HTML 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titleAsTag = soup.find('title')
    titleAsStr = (str(titleAsTag).replace('<title>', '')).replace('</title>', '')

    index = str(i)

    if len(index) == 2:
        index = '0' + index
    elif len(index) == 1:
        index = '00' + index
    else:
        index = index

    f.write(index + ' ' + titleAsStr + '\n')
    print(index + ' Passed')

f.close()
print('Completed')
