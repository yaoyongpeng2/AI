#----------------10.1. Operating System Interface-------------------
import os
cwd=os.getcwd()
print(cwd)
os.chdir("../")
print(os.getcwd())
os.system('mkdir test-os')
os.rename('test-os','test-os2')
print(os.listdir())
os.rmdir('test-os2')
#print(dir(os))
#print(help(os))

import shutil
os.chdir(cwd+'/../')
#os.mkdir('./build/executables')#仅单层目录
os.makedirs('./build/executables',exist_ok=True)#可多层，已存在，可覆盖
shutil.copy('workfile','./build/executables/workfile.txt')
#防止下一行报错：目标路径“installdir\executables”已存在
#os.removedirs('installdir')#能删除非空子目录
shutil.rmtree('installdir')#能删除目录树，无论子目录是否非空
print(shutil.move('./build/executables','installdir'))#见以下注释
# 总结：关键逻辑表
# =========================================================================================
# 目标状态                    | shutil.move 行为                     | 解决方法
# -----------------------------------------------------------------------------------------
# 目标不存在且父目录存在       | 重命名源为 installdir                | 直接调用 shutil.move
# 目标不存在且父目录不存在     | 报错 FileNotFoundError               | 先创建父目录 os.makedirs
# 目标存在且是目录             | 移动源到目标目录内                   | 直接调用 shutil.move
# 目标存在且是文件             | 报错 NotADirectoryError              | 删除文件或修改目标路径
# 目标存在且需覆盖             | 报错 shutil.Error                    | 先删除旧目录 shutil.rmtree
# =========================================================================================

#-----------------------------------10.2. File Wildcards----------------------
os.chdir(cwd)
import glob
print(glob.glob('*.py'))
#-----------------------------10.3. Command Line Arguments--------------------
import sys
print(sys.argv)

import argparse
parse=argparse.ArgumentParser(description='Show top lines from each file')
#.vscode/launch.json，增加了"args": ["Class.py ", "${file}", "-l", "5"]
parse.add_argument('filenames',nargs='+')#filenames位置参数（无前缀-），'+'=至少一个
parse.add_argument('-l','--lines',type=int,default=10)#-l/--lines可选参数（前缀-），行数（默认 10，须为整数）
args=parse.parse_args() #按照add_argument()给的参数结构，
                        #解析命令行参数（=sys.argv=lanch.json文件的args项的值）
print(args)

