import os
import re 

dir='C:\\mypy\\nmap_scan\\ok'


file_list=os.listdir(dir)


print (file_list)

for i in file_list:
    #result=re.findall(r'((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)',i)
    #result=re.findall(r'\D(?:\d{1,3}\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\D',i)
    result=re.findall(r'\d+\.\d+\.\d+\.\d+',i)
    
    for j in result:
        print (j)