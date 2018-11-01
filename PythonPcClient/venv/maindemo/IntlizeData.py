from pathlib import Path
import os
import re,json

class Intilize:
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
        self.line_2 = "c:\\" + userName + '\n'

    def loadMainData(self):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if not Path(dataPath).is_file():
            return False
        else:
            data = open(dataPath, "r")
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
        self.js_4 = json.dumps(path) + '\n'
        self.js_5 = json.dumps(size) + '\n'
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
            oldData = open(dataPath, 'r+')
            lines = oldData.readlines()
            oldData.close()
            newData = open(dataPath, 'w+')
            if not lines:
                data = open(dataPath, 'w+')
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
            data = open(dataPath, 'w+')
            data.write(self.line_1)
            data.write(self.line_2)
            data.write(self.line_3)
            data.write(self.js_4 )
            data.write(self.js_5)
            data.write(self.line_6)
            data.close()

    def addDtedData(self, num, files, dirs, size):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if Path(dataPath).is_file():
            oldData = open(dataPath, 'a')
            lines = []
            lines.append(num + "\n")
            lines.append(json.dumps(files) + "\n")
            lines.append(json.dumps(dirs) + "\n")
            lines.append(json.dumps(size) + "\n")
            lines.append("###\n")
            for l in lines:
                oldData.write(l)
            oldData.close()
        else:
            print("文件被删除！")

    def updateDtedData(self,num,files,dirs,size):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if Path(dataPath).is_file():
            oldData = open(dataPath, 'r+')
            lines = oldData.readlines()
            oldData.close()
            newData = open(dataPath, 'w+')
            start = 6
            for line in lines:
                if num + "\n" == line:
                    start = lines.index(line)
                    print(start)
            lines[start] = num + "\n"
            lines[start+1] = json.dumps(files) + "\n"
            lines[start+2] = json.dumps(dirs) + "\n"
            lines[start+3] = json.dumps(size) + "\n"
            lines[start+4] = "###\n"
            for l in lines:
                newData.write(l)
            newData.close()
        else:
            print("文件被删除！")

    def getData(self,num):
        dataPath = self.line_2.rstrip("\n") + "\\userInfo.npy"
        if Path(dataPath).is_file():
            oldData = open(dataPath, 'r')
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


if __name__ == "__main__":
    p = {0:"aaa",1:"bbb",2:"ccc"}
    s = {"files": 23447877, "dirs": 4655092, "prsnFiles": 0}
    ntli = Intilize()
    ntli.updateData("userN","3",p,s)
    ntli.addDtedData("2",{"asdf":"adf"},{"aaa":"aaa"},{"faw":"afsf"})
    # ntli.updateDtedData("2", {"aaaaaasdf": "adf"}, {"aaaaaaaa": "aaa"}, {"faw": "afsf"})
    print(ntli.getData("2"))
    ntli.loadMainData()
    # print(ntli.line_3)