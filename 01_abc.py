# 如果a+b+c=1000，且 a^2+b^2=c^2  ,求出a,b,c 可能得组合

import time
start_time = time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if c**2 == b**2+a**2 and c == 1000-a-b:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))


# 第一次修改
# a,b 确定  c已知
for a in range(1001):
    for b in range(1001):
        c = 1000-a-b
        if c**2 == a**2 + b**2:
            print("a,b,c:%d,%d,%d"%(a,b,c))
end_time = time.time()
print("time:%d"%(end_time-start_time))
print("finished")

# 存储学生信息
# name
# age
# hoetown
# 列表，字典，元祖
[
    ("zhangsan",24,"beijing")
    ("zhangsan",24,"beijing")
    ("zhangsan",24,"beijing")
]

# ADT
# class Stus(object):
#     def adds(self):
#     def pop(self):
#     def sort(self):
#     def modify(self):
#
# for stu in stus:
#     if stu(0)=="zhangsan":
#
# [
#     {
#         "name":"zhangsan",
#         "age":23
#         "hometown":"beijing"
#     },
# ]

{
    "zhangsan":{
        "age":24,
        "hometown":"beijing"
    },
}

# dict 检索信息key-value  比 列表快哦