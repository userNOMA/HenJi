from __future__ import print_function
import os, sys
from pathlib import Path

# 重写判断程序是否具有管理员权限的函数
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# 打开文件
cSpace = ("F:\\PythonTest","PythonTest")
wSpace = "C:\\userNoma"
pSpace = {'_日记': "C:\\userNoma\\_备忘\\_日记",'_笔记':"C:\\userNoma\\_备忘\\_笔记",'_见闻':"C:\\userNoma\\_备忘\\_见闻",
          '_业内': "C:\\userNoma\\_资料\\_业内",'_兴趣':"C:\\userNoma\\_资料\\_兴趣",'_文哲':"C:\\userNoma\\_资料\\_文哲",
          '_竞赛': "C:\\userNoma\\_研究\\_竞赛",'_编程':"C:\\userNoma\\_研究\\_编程",'_奇思':"C:\\userNoma\\_研究\\_奇思",
          '_照片': "C:\\userNoma\\_日常\\_照片",'_视频':"C:\\userNoma\\_日常\\_视频",'_其它':"C:\\userNoma\\_日常\\_其它",
          '_网页': "C:\\userNoma\\_收藏\\_网页",'_软件':"C:\\userNoma\\_收藏\\_软件",'_杂项':"C:\\userNoma\\_收藏\\_杂项",
          '_备忘': "C:\\userNoma\\_备忘",'_资料':"C:\\userNoma\\_资料",'_研究':"C:\\userNoma\\_研究",
          '_日常': "C:\\userNoma\\_日常",'_收藏':"C:\\userNoma\\_收藏",}
if not Path(wSpace).exists():
    print("工作文件夹并未创建！")
    os.makedirs(wSpace)
    for s in pSpace:
        if s == "_备忘":
            break
        os.makedirs(pSpace.get(s))

# 调用函数返回文件夹内的文件名列表
dirs = os.listdir( cSpace[0] )
files = {}
cDirs = {}
# 输出所有文件和文件夹
for file in dirs:
    # print (file)
    filePath = cSpace[0] + "\\" + file
    path = Path(filePath)
    # 如果是文件夹的话就跳过
    if path.is_dir():
        dirinfo = os.stat(filePath)
        diratt = {'path': filePath, 'size': dirinfo.st_size, 'ctime': dirinfo.st_mtime,
                     'type': 'file', 'exist': True}
        cDirs[file] = diratt
        continue
    # 否则打开该文件
    fd = os.open(filePath, os.O_RDWR | os.O_CREAT)
    # 提取文件的 stat 信息
    stinfo = os.fstat(fd)
    os.close(fd)
    # 使用 os.stat 来接收文件的访问时间和大小
    # print( file + " 的修改时间: %s" % stinfo.st_mtime)
    # print( file + " 的文件大小: %s" % stinfo.st_size + "Byte")
    # 字典当中分别储存文件路径，文件大小，最后访问时间，文件类型，是否依旧存在
    att = {'path':filePath,'size':stinfo.st_size,'ctime':stinfo.st_mtime,'type':os.path.splitext(file)[1],'exist':True}
    # 将字典和对应的文件名存进新的字典
    files[file] = att

nSpace = wSpace + "\\" + cSpace[1]
if not Path(nSpace).exists():
    os.makedirs(nSpace)

if is_admin():
    # 判断若果有系统权限就开始执行创建软件连接文件的操作
    for f in files:
        file = files.get(f)
        cPath = nSpace + "\\" + f
        if not os.path.exists(cPath):
            os.symlink(file.get('path'), cPath)
    for d in cDirs:
        myDir = cDirs.get(d)
        myPyth = nSpace + "\\" +d
        if not os.path.exists(myPyth):
            os.symlink(myDir.get('path'), myPyth)
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


