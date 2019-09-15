# 队列相比列表优点:大小可控,超过最大值自动移除;
# index[0]位置添加删除的时间复杂度为o(1), 而列表为o(n)
from collections import deque

lst = deque(maxlen=3)
# append appendleft pop popleft
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)  # deque([1, 2, 3], maxlen=3)
lst.append(4)
print(lst)  # deque([2, 3, 4], maxlen=3)
lst.appendleft(5)
print(lst)  # deque([5, 2, 3], maxlen=3)
lst.popleft()
print(lst)  # deque([2, 3], maxlen=3)
lst.pop()
print(lst)  # deque([2], maxlen=3)


# heapq 模块有两个函数:nlargest() 和 nsmallest() 求最大/最小的N个元素
# 当N的个数相对较小的时候,headpq是最好的选择
# 当N=1时候, 使用min和max即可
# 当N接近集合大小的时候,先排序后切片效率更高:sorted(items)[:N]
import heapq
lst_one = [-1, 9, 6, 32, 98, 11, 7]
print(heapq.nlargest(3, lst_one))  # [98, 32, 11]
print(heapq.nsmallest(3, lst_one))  # [-1, 6, 7]
# 可以接受key
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
print(heapq.nlargest(3, portfolio, key=lambda x: x['price']))
# [{'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'ACME', 'shares': 75, 'price': 115.65},
# {'name': 'IBM', 'shares': 100, 'price': 91.1}]
lst_two = [1,2]
heapq.heappush(lst_two, 3)
print(lst_two)  # [1, 2, 3]
heapq.heappop(lst_two)
print(lst_two)  # [2, 3]
heapq.heappushpop(lst_two, 5)
print(lst_two)  # [3, 5]
heapq.heapify(lst_two)
print(lst_two)  # [3, 5]
heapq.heapreplace(lst_two, 6)
print(lst_two)  # [5, 6]

# 对比字典的优点, 创建字段时候可以初始化每个key刚开始对应的值
from collections import defaultdict
lst_dic = defaultdict(list)
set_dic = defaultdict(set)
# 也可以使用普通字典设置默认值, 但有点麻烦
d = {} # A regular dictionary
d.setdefault('a', [])

#  控制字典排序
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['c'] = 2
d['b'] = 3
print(d)
# 缺点:内部维护着一个根据键插入顺序排序的双向链表,每次添加新元素后会添加到链表尾部,消耗内存

# 字典的运算 求最大价格
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
print(max(zip(prices.values(), prices.keys())))  # (612.78, 'AAPL')

# 查找字典相同值
a = {'x' : 1, 'y' : 2, 'z' : 3}
b = {'w' : 10, 'x' : 11, 'y' : 2}
print(a.keys() & b.keys())  # {'y', 'x'}
print(a.keys() - b.keys())  # {'z'}
print(a.items() & b.items())  # {('y', 2)}

# 删除序列相同元素并保持顺序
# 如果元素可hash
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
# 如果有字典,可增加参数
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if not key else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))  # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: d['x'])))  # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

