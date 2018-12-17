'''
    序列化： picking
    把变量从内存中变成可储存或传输的过程

    反序列化：unpicking
    把变量内容从序列化的对象，重新读到内存中

'''

import pickle

d = dict(name='Lee', age=18, score=100)
print(pickle.dumps(d))
print(pickle.loads(d))

import json
json.dumps(d)
json.loads(d)

# json 进阶
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)


import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=lambda obj: obj.__dict__))