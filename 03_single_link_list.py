
class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

     #node = Node(100)  存数据100

class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=Node):
        self.__head = node
    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur 游标，用来移动遍历节点
        cur = self.__head
        # count 记录数量
        count = 0
        while cur!= None :
            count +=1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个列表"""
        # cur 游标，用来移动遍历节点
        cur = self.__head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next
        print(" ")

    def add(self,item):
        """链表头部添加元素 头插法"""
        node =Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        """链表尾部添加元素 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur =self.__head
            while cur.next != None:
                cur =cur.next
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素
        :param  pos 从0开始"""
        node = Node(item)
        if pos <=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count<(pos-1):
                count+=1
                pre = pre.next
                pre.next = node

    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头结点
                #头结点情况：
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

# 实例对象

# li=List()

# node = Node(100)
# single_obj = SingleLinkList()
# single_obj.travel()

if __name__=="__main__":
    ll = SingleLinkList()
    print(ll.is_empty())

    print(ll.length())
    ll.append(1)

    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()


nengrangyuyan shuode  jiubie bibi 