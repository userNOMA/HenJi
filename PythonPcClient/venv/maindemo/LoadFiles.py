# -*- coding:utf-8 -*-
from __future__ import print_function
import os, sys ,ctypes
import shutil
from pathlib import Path
from os.path import join, getsize
import numpy as np
import json


class LoadFiles:
    userName = ""
    mktSp = ""
    wkSp = ""
    prsnSp = {}
    myFiles = {}
    myDirs = {}
    myPrsnFiles = {}
    size = {'files': 0, 'dirs': 0, 'prsnFiles': 0}

    def load(self,mktSp,userName = "henji"):
        self.userName = userName
        self.mktSp = mktSp
        self.wkSp = "c:\\" + userName
        self.prsnSp = {'_日记': self.wkSp + "\\_备忘\\_日记", '_笔记': self.wkSp + "\\_备忘\\_笔记",
                       '_见闻': self.wkSp + "\\_备忘\\_见闻",
                       '_业内': self.wkSp + "\\_资料\\_业内", '_兴趣': self.wkSp + "\\_资料\\_兴趣",
                       '_文哲': self.wkSp + "\\_资料\\_文哲",
                       '_竞赛': self.wkSp + "\\_研究\\_竞赛", '_编程': self.wkSp + "\\_研究\\_编程",
                       '_奇思': self.wkSp + "\\_研究\\_奇思",
                       '_照片': self.wkSp + "\\_日常\\_照片", '_视频': self.wkSp + "\\_日常\\_视频",
                       '_其它': self.wkSp + "\\_日常\\_其它",
                       '_网页': self.wkSp + "\\_收藏\\_网页", '_软件': self.wkSp + "\\_收藏\\_软件",
                       '_杂项': self.wkSp + "\\_收藏\\_杂项",
                       '_备忘': self.wkSp + "\\_备忘", '_资料': self.wkSp + "\\_资料", '_研究': self.wkSp + "\\_研究",
                       '_日常': self.wkSp + "\\_日常", '_收藏': self.wkSp + "\\_收藏", }
        # 判断工作文件夹的状态
        self.creatSp()
        # 载入文件并创建软连接
        self.loadFiles()
        self.loadPrsnFiles()
        self.countSize()

    def creatSp(self):
        wkPath = self.wkSp
        prsnPath = self.prsnSp
        copyPath = wkPath + "\\" + self.mktSp.split("\\")[-1]
        if not Path(copyPath).exists():
            os.makedirs(copyPath)
        print("开始创建工作区及必要文件夹")
        if not Path(wkPath).exists():
            print("工作文件夹并未创建！")
            os.makedirs(wkPath)
            for p in prsnPath:
                if p == "_备忘":
                    break
                os.makedirs(prsnPath.get(p))

    def getdirsize(self,dir):
        print('遍历求文件夹大小')
        size = 0
        for root, dirs, files in os.walk(dir):
            size += sum([getsize(join(root, name)) for name in files])
        return size

    def loadFiles(self):
        mktPath = self.mktSp
        print("开始将目标文件夹载入、储存文件夹内文件的详细信息,并以元组的形式返回其中的文件夹和文档")
        # 调用函数返回文件夹内的文件名列表
        dirs = os.listdir(mktPath)
        # print(dirs)
        # 输出所有文件和文件夹
        for file in dirs:
            # print (file)
            filePath = mktPath + "\\" + file
            path = Path(filePath)
            # 如果是文件夹的话就跳过
            if path.is_dir():
                dirinfo = os.stat(filePath)
                size = self.getdirsize(filePath)
                att = {'path': filePath, 'size': size, 'ctime': dirinfo.st_mtime,
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

    def loadPrsnFiles(self):
        mktPath = self.mktSp
        print("开始将个人文档载入")
        # 调用函数返回文件夹内的文件名列表
        nDirs = os.listdir(mktPath)
        # 输出所有文件和文件夹
        for file in nDirs:
            # print (file)
            filePath = mktPath + "\\" + file
            path = Path(filePath)
            # 如果是文件夹的话就跳过
            if path.is_dir():
                continue
            if not file.__contains__('_'):
                continue
            head = '_' + file.split("_")[1]
            heads = self.prsnSp.keys()
            if not heads.__contains__(head):
                continue
            # 否则打开该文件
            fd = os.open(filePath, os.O_RDWR | os.O_CREAT)
            # 提取文件的 stat 信息
            stinfo = os.fstat(fd)
            os.close(fd)
            # 字典当中分别储存文件路径，文件大小，最后访问时间，文件类型，是否依旧存在
            att = {'path': filePath, 'size': stinfo.st_size, 'ctime': stinfo.st_mtime,
                   'type': os.path.splitext(file)[1], 'exist': True,'head':head}
            # 将字典和对应的文件名存进新的字典
            self.myPrsnFiles[file] = att
        return self.myPrsnFiles

    def countSize(self):
        print('开始统计文件大小')
        size = 0
        for x in self.myFiles:
            size += self.myFiles.get(x).get('size')
            self.size['files'] = size
        size = 0
        for y in self.myDirs:
            size += self.myDirs.get(y).get('size')
            self.size['dirs'] = size
        size = 0
        for x in self.myPrsnFiles:
            size += self.myPrsnFiles.get(x).get('size')
            self.size['prsnFiles'] = size
        return self.size

class IntilizeData:
    # 写入程序信息，其基本格式如下所示
    # 第一行：用户名称
    # 第二行：工作文件夹的路径
    # 第三行：目标文件夹的个数
    # 第四行：目标文件夹的路径字典
    # 第五行：历史转移文件的大小字典
    # 第六行："###"
    # 第七行：目标文件夹路径在路径字典当中的标号
    # 第八行：目标文件夹下的文件字典
    # 第九行：目标文件夹下的文件夹字典
    # 第十行：上一次执行操作时产生的数据量
    # 第十一行："###"
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = {}
    line_5 = {}
    js_4 = ""
    js_5 = ""
    line_6 = "###\n"

    def __init__(self,userName = "henji"):
        self.line_1 = userName  + '\n'
        self.line_2 = "c:\\" + 'henji\n'

    def loadMainData(self):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if not Path(dataPath).is_file():
            return False
        else:
            data = open(dataPath, "r",encoding='utf8')
            self.line_3 = data.readline(2)
            self.line_4 = data.readline(3)
            self.line_5 = data.readline(4)
            data.close()
            return True

    def creatData(self,userName,markNum,path,size):
        self.line_1 = userName  + '\n'
        self.line_3 = markNum + '\n'
        self.line_4 = path
        self.line_5 = size
        self.js_4 = json.dumps(path,ensure_ascii=False) + '\n'
        self.js_5 = json.dumps(size,ensure_ascii=False) + '\n'
        self.crateWorkPlace()
        self.writeHeadData()

    def crateWorkPlace(self):
        if not Path(self.line_2.rstrip("\n")).exists():
            os.makedirs(self.line_2.rstrip("\n"))
            return True
        return False

    def writeHeadData(self):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if Path(dataPath).is_file():
            oldData = open(dataPath, 'r+',encoding='utf-8')
            lines = oldData.readlines()
            oldData.close()
            newData = open(dataPath, 'w+',encoding='utf-8')
            if not lines:
                data = open(dataPath, 'w+',encoding='utf-8')
                data.write(self.line_1)
                data.write(self.line_2)
                data.write(self.line_3)
                data.write(self.js_4)
                data.write(self.js_5)
                data.write(self.line_6 )
                data.close()
                return
            if self.line_1 != lines[0]:
                lines[0] = self.line_1
            if self.line_2 != lines[1]:
                lines[1] = self.line_2
            if self.line_3 != lines[2]:
                lines[2] = self.line_3
            if self.js_4 != lines[3]:
                lines[3] = self.js_4
            if self.js_5 != lines[4]:
                lines[4] = self.js_5
            for line in lines:
                newData.write(line)
                if line == "\n":
                    break
            newData.close()
        else:
            data = open(dataPath, 'w+',encoding='utf-8')
            data.write(self.line_1)
            data.write(self.line_2)
            data.write(self.line_3)
            data.write(self.js_4 )
            data.write(self.js_5)
            data.write(self.line_6)
            data.close()

    def updateHeadData(self,userName,num,path,size):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if Path(dataPath).is_file():
            oldData = open(dataPath, 'r+',encoding='utf-8')
            lines = oldData.readlines()
            oldData.close()
            if lines:
                newData = open(dataPath, mode='w+', encoding='utf-8')
                lines[0] = userName + "\n"
                lines[2] = num + "\n"
                lines[3] = json.dumps(path,ensure_ascii=False) + "\n"
                lines[4] = json.dumps(size,ensure_ascii=False) + "\n"
                for l in lines:
                    newData.write(l)
                newData.close()
            else:
                newData = open(dataPath, mode='w+', encoding='utf-8')
                newData.write(userName + "\n")
                newData.write("c:\\henji")
                newData.write(num + "\n")
                newData.write(json.dumps(path,ensure_ascii=False) + "\n")
                newData.write(json.dumps(size,ensure_ascii=False) + "\n")
                newData.write("###\n")
                newData.close()
        else:
            print("文件被删除！")

    def addDtedData(self, num, files, dirs, size):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if Path(dataPath).is_file():
            oldData = open(dataPath, 'a',encoding='utf-8')
            lines = []
            lines.append(num + "\n")
            lines.append(json.dumps(files,ensure_ascii=False) + "\n")
            lines.append(json.dumps(dirs,ensure_ascii=False) + "\n")
            lines.append(json.dumps(size,ensure_ascii=False) + "\n")
            lines.append("###\n")
            for l in lines:
                oldData.write(l)
            oldData.close()
        else:
            print("文件被删除！")

    def updateDtedData(self,num,files,dirs,size):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if Path(dataPath).is_file():
            oldData = open(dataPath, 'r+',encoding='utf-8')
            lines = oldData.readlines()
            oldData.close()
            newData = open(dataPath, 'w+',encoding='utf-8')
            start = 6
            for line in lines:
                if num + "\n" == line:
                    start = lines.index(line)
                    print(start)
            lines[start] = num + "\n"
            lines[start+1] = json.dumps(files,ensure_ascii=False) + "\n"
            lines[start+2] = json.dumps(dirs,ensure_ascii=False) + "\n"
            lines[start+3] = json.dumps(size,ensure_ascii=False) + "\n"
            lines[start+4] = "###\n"
            for l in lines:
                newData.write(l)
            newData.close()
        else:
            print("文件被删除！")

    def getData(self,num):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if Path(dataPath).is_file():
            oldData = open(dataPath, 'r',encoding='utf-8')
            lines = oldData.readlines()
            oldData.close()
            start = 6
            for line in lines:
                if num + "\n" == line:
                    start = lines.index(line)
                    print(start)
            rslt = lines[start:start+4]
            i = 0
            for r in rslt:
                rslt[i] = r.rstrip("\n")
                i +=1
            return rslt
        else:
            print("文件被删除！")

class WriteFiles:

    def __init__(self):
        print("初始化操作")
        self.wkSp = "c:\\henji"
        self.prsnSp = {'_日记': self.wkSp + "\\_备忘\\_日记", '_笔记': self.wkSp + "\\_备忘\\_笔记",
                       '_见闻': self.wkSp + "\\_备忘\\_见闻",
                       '_业内': self.wkSp + "\\_资料\\_业内", '_兴趣': self.wkSp + "\\_资料\\_兴趣",
                       '_文哲': self.wkSp + "\\_资料\\_文哲",
                       '_竞赛': self.wkSp + "\\_研究\\_竞赛", '_编程': self.wkSp + "\\_研究\\_编程",
                       '_奇思': self.wkSp + "\\_研究\\_奇思",
                       '_照片': self.wkSp + "\\_日常\\_照片", '_视频': self.wkSp + "\\_日常\\_视频",
                       '_其它': self.wkSp + "\\_日常\\_其它",
                       '_网页': self.wkSp + "\\_收藏\\_网页", '_软件': self.wkSp + "\\_收藏\\_软件",
                       '_杂项': self.wkSp + "\\_收藏\\_杂项",
                       '_备忘': self.wkSp + "\\_备忘", '_资料': self.wkSp + "\\_资料", '_研究': self.wkSp + "\\_研究",
                       '_日常': self.wkSp + "\\_日常", '_收藏': self.wkSp + "\\_收藏", }

    def cutPrsnFiles(self,prsnFiles):
        print("开始转移个人文件")
        if not prsnFiles:
            return
        for p in prsnFiles:
            head = psonPaths.get(p).get('head')
            shutil.move(psonPaths.get(p).get('path'),self.prsnSp.get(head))

    def writeFiles(self,myFiles):
        print("开始创建文件快捷方式")
        for f in myFiles:
            print(f)
            fileInfo = myFiles.get(f)
            newPath = self.wkSp + "\\" + fileInfo.get('path').split("\\")[-2] + "\\" + f
            print(newPath)
            if not os.path.exists(newPath):
                print(newPath)
                os.symlink(fileInfo.get('path'), newPath)

if __name__ == "__main__":
    # myFileManger = ManageFiles("F:\\PythonTest","userNoma")
    # myFileManger.creatSp()
    # myFileManger.loadFiles()
    # myFileManger.writeFiles()
    # myFileManger.loadPrsnFiles()
    # myFileManger.countSize()
    # myFileManger.cutPrsnFiles()
    # myFileManger.writeInfo()
    # # myFileManger.readInfo()
    # print(myFileManger.myFiles)
    # print(myFileManger.myDirs)
    # print(myFileManger.myPrsnFiles)
    # print('总共创建文件链接数据量：',round(myFileManger.size.get('files')/(1024*1024),2),'M')
    # print('总共创建文件夹链接数据量：', round(myFileManger.size.get('dirs')/(1024*1024),2),'M')
    # print('总共转移文件数据量：', round(myFileManger.size.get('prsnFiles')/(1024*1024),2),'M')
    # fileManger = ManageFiles("F:\\PythonTest")
    # print(fileManger.myFiles)
    # print(fileManger.myDirs)
    # print(fileManger.myPrsnFiles)
    # print(fileManger.size)
    filel = open("F:\\PythonTest\\mm.txt",'w',encoding='utf-8')

    filel.write("你是谁？\n")
    filel.write(json.dumps({111:"你是谁？"},ensure_ascii=False))