#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os
url = "https://github.com/Leonezz/maoxuan/blob/master/src/"
readme = "# 毛泽东选集\n"
readme+="## 第一卷 国内革命战争时期\n"
readme+="### 第一次国内革命战争时期\n"
for i,j,fileNameList in os.walk("./src"):
    fileNameList.sort(reverse=False,key=lambda elem:int(elem.split('.')[0]))
    cnt=1
    for fileName in fileNameList:
        if cnt==3:
            readme+="### 第二次国内革命战争时期"
        elif cnt==19:
            readme+="## 第二卷 抗日战争时期（上）"
        elif cnt==59:
            readme+="## 第三卷 抗日战争时期（下）"
        elif cnt==91:
            readme+="## 第四卷 第三次国内革命战争时期"
        elif cnt==160:
            readme+="## 第五卷 社会主义革命和社会主义建设时期（一）"
        elif cnt==230:
            readme+="## 第六卷 社会主义革命和社会主义建设时期（二）"
        elif cnt==305:
            readme+="## 第七卷 文化大革命时期"
        readme+="\n"
        articleName = fileName.split('.')[1]
        readme+=str(cnt)+'. ['+articleName+']('+url+fileName+")\n"
        cnt+=1
readmeFile = open('./README.md','w+')
readmeFile.write(readme)
readmeFile.close()