#coding:utf-8
import string

s = ''.join([line.rstrip() for line in open('mess.txt')])
# 读取文本内容

occ = {}
# 定义一个字典，里面存储每个字符以及对应出现的频率

for c in s:
    occ[c] = occ.get(c, 0) + 1
# 同样的字符，字典的值加1
# 计算出平均情况（所有字符数量／字符数量）

avgOC = len(s) // len(occ)
# 循环输出稀有性低于平均的字符


print ''.join([c for c in s if occ[c] < avgOC])

# 那么就有人比较聪明的抓住“rare”这个单词，也就是字符数量是稀有的，那么假设就是字符出现的次数就是1

d = {}

for ch in s:
    d[ch] = d.get(ch,0) + 1

print ''.join([ch for ch in s if d[ch] == 1])