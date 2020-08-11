fr=open('deal_hz_ip_zhuanxian_fping_alive_20200801.txt','r')
mylines=fr.readlines()
fr.close()
n_process=10
index=0;
n=int(len(mylines)/n_process)
for i in range(0,len(mylines),n):
    sub=mylines[i:i+n]
    index=index+1
    fw=open('iplist'+str(index),'w')
    for j in sub:
        fw.write(j)
    fw.close()
