import os, sys
from pathlib import Path

# 打开文件
workingSpace = "F:\\PythonTest"
# 调用函数返回文件夹内的文件名列表
dirs = os.listdir( workingSpace )
files = {}
# 输出所有文件和文件夹
for file in dirs:
    print (file)
    filePath = workingSpace + "\\" + file
    path = Path(filePath)
    # 如果是文件夹的话就跳过
    if path.is_dir():
        continue
    # 否则打开该文件
    fd = os.open(filePath, os.O_RDWR | os.O_CREAT)
    # 提取文件的 stat 信息
    stinfo = os.fstat(fd)
    # 使用 os.stat 来接收文件的访问时间和大小
    print( file + " 的修改时间: %s" % stinfo.st_mtime)
    print( file + " 的文件大小: %s" % stinfo.st_size + "Byte")
    # 元组当中分别储存文件路径，文件大小，最后访问时间，文件类型，是否依旧存在
    attribute = (filePath,stinfo.st_size,stinfo.st_mtime,os.path.splitext(file)[1],True)
    files[file] = attribute

for f in files:
    print(files.get(f))