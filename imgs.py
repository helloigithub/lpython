import urllib.request
import os

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    print(url)
    return html

def find_imgs(url):
    html = open_url(url).decode('utf-8')
    img_addrs = []
    a = html.find('src="https://ww')
    while a!=-1:
        b = html.find('.jpg',a,a+255)
        if b!=-1:
            img_addrs.append(html[a+5:b+4])
        else:
            b = a+5
        a = html.find('src="https://ww',b)

    for each in img_addrs:
        print(each)

    return img_addrs

def save_imags(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = open_url(each)
            f.write(img)
   
def meizi():
    folder = 'meizi1'
    os.mkdir(folder)
    os.chdir(folder)
    url = 'https://www.dbmeinv.com/dbgroup/show.htm?pager_offset='
    for i in range(10,20):
        url2 = url + str(i)
        img_addrs = find_imgs(url2)
        save_imags(folder,img_addrs)

if __name__ == '__main__':
    meizi()

        
