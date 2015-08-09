#! /usr/bin/python3.4
#
import os,sys
import subprocess

cmd = 'cd  && pwd';(status, output) = subprocess.getstatusoutput(cmd);pwdu = output
if (not pwdu.endswith('/')):pwdu = pwdu +'/'
pwd = os.path.abspath('')
if (not pwd.endswith('/')):pwd = pwd +'/'
del cmd,status,output

savepath = '/home/Che/Projects/openSUSE/.backup/'
def savepath_():
    global savepath
    savepath = pwd + '.backup/'
savepath_();#print(savepath)

paths = [
#(originpath,savedpath)
('~/.themes/',      savepath),
('~/.fonts/',       savepath),
('~/.icons/',       savepath),
('~/.conky/',       savepath),
('~/.conkyrc',      savepath),
('~/vimwiki/',      savepath),
#############
('/usr/share/icons/',    savepath + 'usr/share/'),
('/usr/share/themes/',  savepath + 'usr/share/')
]
def paths_():
    global paths
    global pwdu
    #print (pwdu)

    temp=[]
    for (opath,spath) in paths:
        if (opath.startswith('~/')):
            opath = pwdu + opath[2:]
        temp.append ((opath,spath))
    paths = temp;#print (paths,'\n',temp)
paths_()
###


###
def backup():
    for (opath,spath) in paths:
        if (not os.path.exists(opath)):next
        if (not os.path.exists(spath)):cmd = 'mkdir -p '+spath;subprocess.getstatusoutput(cmd)
        isfile = os.path.isfile(opath)
        if (isfile):filename = opath.split('/')[-1]
        isdir = os.path.isdir(opath)
        if(isdir):dirname = os.path.dirname(opath).split('/')[-1]

        if (isfile):
            #print ('check file {0}|{1}'.format(filename,path))
            #subprocess.Popen('cp -u {0} {1}'.format(path,savepath+filename),shell=True).wait()
            cmd = 'cp -u {0} {1}'.format(opath,spath)
            (status, output) = subprocess.getstatusoutput(cmd)
            print ('status: %-3s dir: %-6s'%(status,filename))
            if (status):print (' '*3,output)
            #if (not status):
            #    print('succeeded\t copy file:\t{0}'.format(filename))
            #else:
            #    print('failed   \t copy file:\t{0}'.format(filename))
            #
        elif(isdir):

            #subprocess.Popen('cp -urv {0} {1}'.format(path,savepath+dirname),shell=True).wait()
            cmd ='cp -urv {0} {1}'.format(opath,spath)
            (status, output) = subprocess.getstatusoutput(cmd)
            print ('status: %-3s dir: %-8s'%(status,dirname))
            if (status):print (' '*3,output)
            #if (not status):
            #    print('succeeded\t copy dir:\t{0}'.format(dirname))
            #else:
            #    print('failed    \t copy  dir:\t{0}'.format(dirnme))
        else:
            #print ('path:{0} \tignored'.format(opath))
            print ( 'ignored \t %s' % (opath) )
def recovery():
    for (opath,spath) in paths:
        if (opath.endswith('/')):
            dirname = os.path.abspath(opath)
            dirname =os.path.abspath(dirname)
        else:
            dirname = os.path.abspath(opath)
        name = dirname.split('/')[-1]
        #print(name,dirname)

        if (not os.path.exists(spath + name)):
            print ('ignored \t%s'%(dirname))
            next

        cmd = 'sudo cp -ru {0} {1}'.format(spath + name,os.path.dirname(dirname));#print(cmd)
        status = subprocess.Popen(cmd,shell = True).wait()
        print ('status: %-3s dir: %-6s'%(status,dirname))




###
def test():
    for (opath,spath) in paths:
        cmd = 'sudo rm -rf %s'%(opath)
        if(not subprocess.Popen(cmd,shell=True).wait()):
            print ('Succeeded')
        else:
            print ('Failed')
    return ''

def defi(a = '', b =[]):
    for arg in b:
        if(a==arg):
            return True
if __name__ == '__main__':
    if (defi(sys.argv[-1],['-b','b','--back'])):
        backup()
    elif ( defi(sys.argv[-1],['-r','r','--recovery']) ):
        recovery();#print('called reconvery')
    elif(sys.argv[-1] == 'test'):
        test()
    else:
        print ('''--------------------------------
Auto backup the important data_
usage: ./auto.py [arguments]

Arguments:
    -b              backup,means to backup all the data_
    -r              recovery ,means to recovery data_
        ''')
