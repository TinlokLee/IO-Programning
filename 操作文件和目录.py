'''
    os 模块封装了操作系统的目录和文件操作，有的函数会在os.path模块中
'''

import os 
os.uname

os.path.abspath()
os.mkdir()
os.path.join()
os.rmdir()
os.path.splitext()

# 列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) 
                               and os.path.splitext(x)[1]=='.py']

# 列出当前目录下所有目录
ls -l
[x for x in os.listdir('.') if os.path.isdir(x)]



# 打印当前目录文件，大小、 最后修改时间、 文件名
from datetime import datetime
import os

pwd = os.path.abspath('.')
print('Size   last  Modified   Name')
print('-'*60)

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getatime(f).strftime('%Y-%m-%d %H:%M'))
    flag = '/' if os.path.isdir(f) else ''
    print('%10d   %s  %s%s' % (fsize, mtime, f, flag))