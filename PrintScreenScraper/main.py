import requests
import random
from bs4 import BeautifulSoup
import string
import sys
import os
from time import sleep

logo = '''
 _____      _       _       _____                              _____                                   _                     _____ _    _ _ _     
|  __ \    (_)     | |     / ____|                            / ____|                                 | |                   / ____| |  (_) | |    
| |__) | __ _ _ __ | |_   | (___   ___ _ __ ___  ___ _ __    | (___   ___ _ __ __ _ _ __   ___ _ __   | |__  _   _         | (___ | | ___| | |    
|  ___/ '__| | '_ \| __|   \___ \ / __| '__/ _ \/ _ \ '_ \    \___ \ / __| '__/ _` | '_ \ / _ \ '__|  | '_ \| | | |         \___ \| |/ / | | |    
| |   | |  | | | | | |_    ____) | (__| | |  __/  __/ | | |   ____) | (__| | | (_| | |_) |  __/ |     | |_) | |_| |         ____) |   <| | | |    
|_|   |_|  |_|_| |_|\__|  |_____/ \___|_|  \___|\___|_| |_|  |_____/ \___|_|  \__,_| .__/ \___|_|     |_.__/ \__, |        |_____/|_|\_\_|_|_|    
                                                                                   | |                        __/ |    ______              ______ 
                                                                                   |_|                       |___/    |______|            |______|'''              
print(logo)


desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
def random_headers():
    return {'User-Agent': random.choice(desktop_agents),'Accept':'*/*', 'Accept-Encoding':None}

def random_url():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for m in range(3))

def random_name():
    return ''.join(random.choice(string.ascii_letters) for m in range(15))

def url(new):
    base_url = 'https://prnt.sc/'+new
    url = base_url+random_url()
    return url

def get_html(final_url):
    r = requests.get(final_url, headers = random_headers())
    return r.content

def get_url(html):
    soup = BeautifulSoup(html, 'lxml')
    url_photo = soup.find('div', {'class':'image-container image__pic js-image-pic'}).find('img').get('src')
    if url_photo == '//st.prntscr.com/2018/10/13/2048/img/0_173a7b_211be8ff.png':
        a = ''
    else:
        return url_photo

def download(path, url_photo, n):
    try:
        r = requests.get(url_photo, headers = random_headers())
        if r.status_code == 200:
            with open(path+random_name()+'.jpg', 'wb') as f:
                f.write(r.content)
                print('['+str(n)+']'+'[Success] Url: '+url_photo)
                sleep(0.01)
    except:
        print('[Error] Non image')
        sleep(0.01)

def main():
    n = 1
    new = input('\nFirst three characters in url: ')
    path = input('Path to save: ')
    number = int(input('Number of pictures: '))
    for i in range(number):
        final_url = url(new)
        html = get_html(final_url)
        url_photo = get_url(html)
        path = os.path.abspath(r''.join(path)).replace('\\', '/')+'/'
        download(path, url_photo, n)
        n += 1
    print('Completed')
    input()
if __name__=='__main__':
    main()
