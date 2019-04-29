#coding=utf-8
import requests
import json
import urllib
def getSogouImag(category,length,path,name):
    for n in range(1,3):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        url = 'https://pic.sogou.com/pics?query='+category+'&mode=1&start='+str(480+n*48)+'&reqType=ajax&reqFrom=result&tn=0'
        print(url)
        imgs = requests.get(url,headers)
        jd = json.loads(imgs.text)
        jd = jd['items']
        imgs_url = []
        for j in jd:
            imgs_url.append(j['ori_pic_url'])
        m = 0
        for img_url in imgs_url:
            try:
                print(img_url)
                print('***** '+str(m+(n-1)*48)+'.jpg *****'+'   Downloading...')
                urllib.request.urlretrieve(img_url,path+name+str(m+(n-1)*48)+'.jpg')
                m = m + 1
            except:
                pass
    print('Download complete!')


getSogouImag('猪',100,'./pigTest/',"pig")
# Resize('./pigTest','./pigTestR')
