
# 新建一个列表
#
from timeit import Timer
def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():
    li = []
    for i in range(10000):
        # li += [i]
        li = li+ [i]
        # += 已经有优化，相对于来说第二种方式耗时长，不推荐

def t3():
    li=[i for i in range(10000)]

def t4():
    li = list(range(10000))

def t5():
    li =[]
    for i in range(10000):
        li.extend([i])

timer1 = Timer("t1()","from __main__ import t1")
print("append:",timer1.timeit(1000))

timer2 = Timer("t2()","from __main__ import t2")
print("+=:",timer2.timeit(1000))

timer3 = Timer("t3()","from __main__ import t3")
print("[i for i in range]:",timer3.timeit(1000))

timer4 = Timer("t4()","from __main__ import t4")
print("list(range):",timer4.timeit(1000))

timer5 = Timer("t5()","from __main__ import t5")
print("extend:",timer5.timeit(1000))

def t6():
    li = []
    for i in range(10000):
        li.append(i)

def t7():
    li = []
    for i in range(10000):
        li.insert(0,i)

timer6 = Timer("t6()","from __main__ import t6")
print("append:",timer6.timeit(1000))

timer7 = Timer("t7()","from __main__ import t7")
print("insert:",timer7.timeit(1000))


# append: 0.6234207669999999
# +=: 0.836778138
# [i for i in range]: 0.33286703500000003
# list(range): 0.22879982900000018
# extend: 0.9871886480000001
# append: 0.6333307930000003
# insert: 19.32698758

x = list(range(2000000))
pop_zero = Timer("x.pop(0)","from __main__ import x")
print("pop_zero",pop_zero.timeit(number= 1000),"second")

x = list(range(2000000))
pop_end = Timer("x.pop(0)","from __main__ import x")
print("pop_end",pop_end.timeit(number=1000),"seconds")

# pop_zero 2.243728581 second
# pop_end 2.45254509 seconds