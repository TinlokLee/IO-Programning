'''
    文件读写IO操作
    f.open(path, 'r')
    f.read() 一次读取全部文件
    f.close() 报错IOError，该方法不会调用
    常与try...finally合用实现

    2 with open()方法
      文件过大，内存爆
      反复调用read(size)方法
      readline()
      readlines()

    3 file-like Object
      StringIO 是内存中创建的file-like Object，常用于临时缓冲
      BytesIO  内存中读取二进制文件
      两个模块读写文件具有一致接口

    
'''

try:
    f = open('/path/file', 'r')
    print(f.read())
    print(f.write())
finally:
    if f:
        f.close()

for line in f.readlines():
    print(line.strip())



from io import BytesIo
f = BytesIo(b'\xe4\xb8')
f.read()

f = BytesIo()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
