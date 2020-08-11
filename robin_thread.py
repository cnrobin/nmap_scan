
#coding:utf-8
import threading
import time
import os

class myThread(threading.Thread):
    def __init__(self,threadID,ok_dir,temp_dir,cmd):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.okdir=ok_dir
        self.tempdir=temp_dir
        self.cmd=cmd      
    def run(self):
        print ("start job: processid "+ str(self.threadID))
        fr=open('iplist'+str(self.threadID),'r')
        mylines=fr.readlines()
        fr.close()
        for l in mylines:
            timestr=time.strftime("%Y%m%d%H%M%S", time.localtime())
            file_temp_name=(str(self.threadID)+'_nmap_'+timestr+'_'+l.strip('\n')+'.txt')
            file_ok_name=self.okdir+file_temp_name
            file_temp_name=self.tempdir+file_temp_name

            fw=open(file_temp_name,'w')
            command='nmap -T4 -Pn '+l.strip('\n')
            result=os.popen(command).readlines()
            for one_line in result:
                fw.write(one_line)
            fw.close()
            os.rename(file_temp_name,file_ok_name)