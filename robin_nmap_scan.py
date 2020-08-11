#!/usr/bin/python3

import configparser
import time
import os
from robin_thread import myThread
import re

config=configparser.ConfigParser()
config.read('properties.conf')
lists_header=config.sections()
print(lists_header)
ip_file=str(config['scan']['ip_file'])
temp_dir=str(config['scan']['temp_dir'])
ok_dir=str(config['scan']['ok_dir'])
sub_max_process=int(config['scan']['max_sub_process'])
cmd=(config['scan']['cmd'])

fr=open(ip_file,'r')
mylines=fr.readlines()
fr.close()



file_list=os.listdir(ok_dir)


print (file_list)

for i in file_list:
    #result=re.findall(r'((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)',i)
    #result=re.findall(r'\D(?:\d{1,3}\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\D',i)
    result=re.findall(r'\d+\.\d+\.\d+\.\d+',i)
    for j in result:
        try:
            mylines.remove(j)
        except:
            pass

        



index=0;


n=int(len(mylines)/(sub_max_process))
for i in range(0,len(mylines),n):
    sub=mylines[i:i+n]
    index=index+1
    fw=open('iplist'+str(index),'w')
    for j in sub:
        fw.write(j)
    fw.close()



threads=[]

for i in range(sub_max_process):
    t=myThread(i+1,ok_dir,temp_dir,cmd)
    t.start()
    threads.append(t)

for t in threads:
    t.join()


print ('finish job')

