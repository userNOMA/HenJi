# 在命令行运行的时候要把文件夹的名字去掉
import os, sys ,ctypes
from LoadFiles import (LoadFiles,IntilizeData,WriteFiles)

def is_admined():
    print("判断是否具有管理员权限")
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def countAllSize(sizes):
    fileSize = 0
    dirSize = 0
    psonSize = 0
    for si in sizes:
        fileSize += si.get('files')
        dirSize += si.get('dirs')
        psonSize += si.get('prsnFiles')
    return {'files':round(fileSize/1024/1024,2),'dirs':round(dirSize/1024/1024,2),'prsnFiles':round(psonSize/1024/1024,2)}

fileManger = LoadFiles()
fileManger.load("F:\\PythonTest")
# fileManger_1 = ManageFiles("F:\\360安全浏览器下载")
writeFiles = WriteFiles()
allFiles = {}
allFiles.update(fileManger.myFiles)
allFiles.update(fileManger.myDirs)
print(allFiles)
if is_admined():
    print("已经获得系统权限，开始创建软连接")
    writeFiles.writeFiles(allFiles)
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:  # in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

print(fileManger.myFiles)
loadData = IntilizeData()
if loadData.loadMainData():
    loadData.updateHeadData("userNoma","1",{0:"F:\\PythonTest"},countAllSize([fileManger.size,fileManger.size]))
    print("文件加载成功")
else:
    loadData.creatData("userNoma","1",{0:"F:\\PythonTest"},countAllSize([fileManger.size,fileManger.size]))