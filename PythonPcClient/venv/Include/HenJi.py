from __future__ import print_function
import os, sys ,ctypes
from pathlib import Path
class Mi:
    def __init__(self,sss):
        self.a = sss
        self.mess = "sfaasf"
    def prr(self,ss):
        print(self.a)
        print(self.mess)
        print(ss)



class ManageFiles:

    mktSp = ''
    wkSp = ''
    prsnSp = {}
    myFiles = {}
    myDirs = {}

    def __init__(self,mktSp,userName):
        self.mktSp = mktSp
        self.wkSp = "c:\\" + userName
        self.prsnSp = {'_日记': self.wkSp+"\\_备忘\\_日记",'_笔记':self.wkSp+"\\_备忘\\_笔记",'_见闻':self.wkSp+"\\_备忘\\_见闻",
                       '_业内': self.wkSp+"\\_资料\\_业内",'_兴趣':self.wkSp+"\\_资料\\_兴趣",'_文哲':self.wkSp+"\\_资料\\_文哲",
                       '_竞赛': self.wkSp+"\\_研究\\_竞赛",'_编程':self.wkSp+"\\_研究\\_编程",'_奇思':self.wkSp+"\\_研究\\_奇思",
                       '_照片': self.wkSp+"\\_日常\\_照片",'_视频':self.wkSp+"\\_日常\\_视频",'_其它':self.wkSp+"\\_日常\\_其它",
                       '_网页': self.wkSp+"\\_收藏\\_网页",'_软件':self.wkSp+"\\_收藏\\_软件",'_杂项':self.wkSp+"\\_收藏\\_杂项",
                       '_备忘': self.wkSp+"\\_备忘",'_资料':self.wkSp+"\\_资料",'_研究':self.wkSp+"\\_研究",
                       '_日常': self.wkSp+"\\_日常",'_收藏':self.wkSp+"\\_收藏",}

    def creatSp(self,WkPath = wkSp,prsnPath = prsnSp):
        print("开始创建工作区及必要文件夹")
        if not Path(WkPath).exists():
            print("工作文件夹并未创建！")
            os.makedirs(WkPath)
            for p in prsnPath:
                if p == "_备忘":
                    break
                os.makedirs(prsnPath.get(p))

    def loadFiles(self,mktPath):
        mktPath = self.mktSp
        print("开始将目标文件夹载入、储存文件夹内文件的详细信息,并以元组的形式返回其中的文件夹和文档")
        # 调用函数返回文件夹内的文件名列表
        dirs = os.listdir(mktPath)
        # 输出所有文件和文件夹
        for file in dirs:
            # print (file)
            filePath = mktPath + "\\" + file
            path = Path(filePath)
            # 如果是文件夹的话就跳过
            if path.is_dir():
                dirinfo = os.stat(filePath)
                att = {'path': filePath, 'size': dirinfo.st_size, 'ctime': dirinfo.st_mtime,
                          'type': 'file', 'exist': True}
                self.myDirs[file] = att
                continue
            # 否则打开该文件
            fd = os.open(filePath, os.O_RDWR | os.O_CREAT)
            # 提取文件的 stat 信息
            stinfo = os.fstat(fd)
            os.close(fd)
            # 字典当中分别储存文件路径，文件大小，最后访问时间，文件类型，是否依旧存在
            att = {'path': filePath, 'size': stinfo.st_size, 'ctime': stinfo.st_mtime,
                   'type': os.path.splitext(file)[1], 'exist': True}
            # 将字典和对应的文件名存进新的字典
            self.myFiles[file] = att
        return (self.myFiles,self.myDirs)


    def writefiles(self,filePaths = myFiles,dirPaths = myDirs,mktSp = mktSp):
        print("开始创建文件快捷方式")
        nSpace = wSpace + "\\" + mktSp.split("\\")[-1]
        if not Path(nSpace).exists():
            os.makedirs(nSpace)
        if is_admin():
            # 判断若果有系统权限就开始执行创建软件连接文件的操作
            for f in filePaths:
                file = files.get(f)
                cPath = nSpace + "\\" + f
                if not os.path.exists(cPath):
                    os.symlink(file.get('path'), cPath)
            for d in dirPaths:
                myDir = cDirs.get(d)
                myPyth = nSpace + "\\" + d
                if not os.path.exists(myPyth):
                    os.symlink(myDir.get('path'), myPyth)
        else:
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            else:  # in python2.x
                ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

def is_admin():
    print("判断是否具有管理员权限")
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    # myFileManger = ManageFiles("F:\\PythonTest","userNoma")
    # myFileManger.creatSp()
    # myFileManger.loadFiles()
    # myFileManger.writefiles()
    name = "_日常_hfioahh阿红i恶化覅和安文丰hi.ppt"
    print(name.split("_"))