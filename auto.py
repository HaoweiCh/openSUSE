#! /usr/bin/python3.4
#
import os
import subprocess
savepath = '/home/Che/Projects/openSUSE/.backup/'
paths = [
'~/.themes/',
'~/.fonts/',
'~/.icons/',
'~/.conky/',
'~/.conkyrc',
'~/vimwiki/',
#############
#'/usr/share/icons'
]

def paths_():
    global paths
    cmd = 'cd  && pwd'
    (status, output) = subprocess.getstatusoutput(cmd)
    pwd = output
    if (not pwd.endswith('/')):pwd = pwd +'/'
    #print (pwd)
    temp=[]
    for path in paths:
        if (path.startswith('~/')):
            path = pwd + path[2:]
        temp.append (path)
    paths = temp
paths_()

def backup():


    temp=[]
    for path in paths:
        if (not os.path.exists(path)):next
        isfile = os.path.isfile(path)
        isdir = os.path.isdir(path)

        if (isfile):
            filename = path.split('/')[-1]
            #print ('check file {0}|{1}'.format(filename,path))
            #subprocess.Popen('cp -u {0} {1}'.format(path,savepath+filename),shell=True).wait()
            cmd = 'cp -u {0} {1}'.format(path,savepath)
            (status, output) = subprocess.getstatusoutput(cmd)
            if (not status):
                print('succeeded\t copy file:\t{0}'.format(filename))
            else:
                print('failed   \t copy file:\t{0}'.format(filename))
        elif(isdir):
            dirname = os.path.dirname(path).split('/')[-1]
            #subprocess.Popen('cp -urv {0} {1}'.format(path,savepath+dirname),shell=True).wait()
            cmd ='cp -urv {0} {1}'.format(path,savepath)
            (status, output) = subprocess.getstatusoutput(cmd)
            if (not status):
                print('succeeded\t copy dir:\t{0}'.format(dirname))
            else:
                print('failed    \t copy  dir:\t{0}'.format(dirnme))
        else:
            print ('path:{0} \tignored'.format(path))
def recovery():
    pass
if __name__ == '__main__':
    import sys
    if ( sys.argv[-1]=='-b'):
        backup()
    elif (sys.argv[-1]=='-r'):
        recovery()
    else:
        print ('''--------------------------------
Auto backup the important data_
usage: ./auto.py [arguments]

Arguments:
    -b              backup,means to backup all the data_
    -r              recovery ,means to recovery data_
        ''')
