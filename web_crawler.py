import requests
from bs4 import BeautifulSoup
import re
import time

TAG_RE = re.compile(r'<[^>]+>')

for i in range(10000,12000):
    page = requests.get("http://www.sgcarmart.com/new_cars/newcars_overview.php?CarCode=%s" % str(i),allow_redirects=False)
    if page.status_code == 200:
        txtfile = open('cardata.dat', 'a')
        txtfile.write("http://www.sgcarmart.com/new_cars/newcars_overview.php?CarCode=%s " % str(i))

        page = requests.get("http://www.sgcarmart.com/new_cars/newcars_photos.php?CarCode=%s" % str(i),allow_redirects=False)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            #for item in list(soup.children):
            if len(soup.find_all('td', class_='font_bold'))>0:
                for item in soup.find_all('td', class_='font_bold'):
                    txtfile.write(TAG_RE.sub('', ''.join(str(item).splitlines())))
            if len(soup.find_all('table', class_='font_bold'))>0:
                for item in soup.find_all('table', class_='font_bold'):
                    txtfile.write(TAG_RE.sub('', ''.join(str(item).splitlines())))

        page = requests.get("http://www.sgcarmart.com/new_cars/newcars_reviews.php?CarCode=%s" % str(i),allow_redirects=False)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            if len(soup.find_all('p'))>0:
                for item in soup.find_all('p'):
                    if item.find('strong'):
                        txtfile.write(TAG_RE.sub('', ''.join(str(item).splitlines())))

        page = requests.get("http://www.sgcarmart.com/new_cars/newcars_specs.php?CarCode=%s" % str(i),allow_redirects=False)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            if len(soup.find_all('table', id='submodel_spec'))>0:
                for item in soup.find_all('table', id='submodel_spec'):
                    txtfile.write(TAG_RE.sub('', ''.join(str(item).splitlines())))

        page = requests.get("http://www.sgcarmart.com/new_cars/newcars_features.php?CarCode=%s" % str(i),allow_redirects=False)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            if len(soup.find_all('table', id='submodel_spec'))>0:
                for item in soup.find_all('table', id='submodel_spec'):
                    txtfile.write(TAG_RE.sub('', ''.join(str(item).splitlines())))

        txtfile.write('\n')
        txtfile.close()
    else:
        continue