#coding=utf-8
import cv2
import os
import numpy
def Resize(pathFile,reSizeFile):
    for files in os.listdir(pathFile):
        imagePathFile=os.path.join(pathFile,files)
        img=cv2.imread(imagePathFile,0)
        try:
            imgResize=cv2.resize(img,(64,64),interpolation=cv2.INTER_CUBIC)
        except:
            continue
        reSizeDir=os.path.join(reSizeFile,files)
        cv2.imwrite(reSizeDir,imgResize)
        print(imagePathFile+' 调整大小成功，存放路径在： '+reSizeFile)   

def maketxtList(imageFile,pathFile):
    fobj=open(pathFile,'a')
    for files in os.listdir(imageFile):
        label = ""
        if(files[0:3] == 'cat'):
            label = '2'
        if(files[0:3] == 'dog'):
            label = '1'
        if(files[0:3] == 'pig'):
            label = '3'
        fobj.write('\n'+files+' '+label)
        print(files+' '+str(label)+' 写入成功！')
    fobj.close()  
maketxtList('./testset','./labelTest.txt') 
