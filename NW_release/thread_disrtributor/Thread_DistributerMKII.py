import time
import _thread
import hashlib

#[C]2018-2023 NICK SOFTWARE
Hash = input('Input your target hash[sha-256 suported]:')
guesS_List = ['I love you','32','f45be2db8a8571c270','fff45be2db8','60ab09e597b','1dceab','d6ba87632','906536','1c27060ab','1c2060ab','1c2706ab','69065366','1902784','1027844','19027844','65071381','9355822','88309797','32371267','71832627','43807232','me231212','emrmrm','nmnmnmn','mmmmm','qwerty','12345678','meme','qazxsw','qwerty123','Alex123']
threaD_Count = int(input('Input threads:'))
dicT_Len = len(guesS_List)
starT_Program = time.time()

if threaD_Count > dicT_Len:
    threaD_Count = dicT_Len

sperading = dicT_Len%threaD_Count

if sperading == 0:
    print('''objs could be divide average!''')
    avG_Sperad = int( ( dicT_Len - sperading ) / threaD_Count )
else:
    print('''objs couldn't sperate average,lefting %s'''%(sperading))
    avG_Sperad = int( ( dicT_Len - sperading ) / threaD_Count )
    print('''each thread will be distributed with %s tasks
number %s to %s thread will redivide'''%(avG_Sperad, dicT_Len - sperading+1, dicT_Len))

def cracK_Func(trY_Passwd):
    stR_Name = trY_Passwd
    trY_Passwd = hashlib.md5()
    trY_Passwd.update(stR_Name.encode('utf-8')) 
    result = trY_Passwd.hexdigest()
#    print(result) #This is an IO operation
    return result

finished = 0

geT_Passwd = ''

def threaD_Process(threaD_Name ,hEad ,eNd):
    locaL_Time = time.asctime( time.localtime(time.time()) )
    print('[INFO][Thread:%s]:%s' %(threaD_Name, locaL_Time))
    for trY_Passwd in guesS_List[hEad:eNd]:
        comPAre = cracK_Func(trY_Passwd)
        if comPAre == Hash:
            global finished
            global geT_Passwd
            print('Thread %s found passwd,which is %s'%(threaD_Name,trY_Passwd))
            geT_Passwd = trY_Passwd
            finished = 1

#creating thread process

print('cracking started with %s thread'%(threaD_Count))

cracK_Time = time.time()

if True:
    time.sleep(0.1)
    try:    
        for multiper in range(threaD_Count):
            hEad = multiper*avG_Sperad
            eNd = (multiper+1)*avG_Sperad
            print('thread %s @ [%s,%s]'%(multiper, multiper*avG_Sperad, (multiper+1)*avG_Sperad))
            _thread.start_new_thread(threaD_Process,(multiper ,hEad, eNd,))
    except:
        print('Unknown Thread ERROR Occured...')

#left Threads process

if finished != 1:
    _thread.start_new_thread(threaD_Process,('[SnglTrd]' ,dicT_Len - sperading+1, dicT_Len,))

time.sleep(1)

end = time.time()

if finished != 1:
    print('[WARN][MainProg]passwd not found')
else:
    print('[SUCCESS!][MainProg]passwd found:%s'%(geT_Passwd))

print('program executed in %s seconds,cracking used %s seconds'%(end-starT_Program-1,end-cracK_Time-1))

exit()