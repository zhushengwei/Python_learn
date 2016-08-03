#!/user/bin/python
#coding:utf-8
import random

dict = {
    1:"剪刀",
    2:"石头",
    3:"布"
}

print "1 is 剪刀"
print '2 is 石头'
print "3 is 布"

people_input = raw_input('pleace input: 1 or 2 or 3\n')
computer_input = random.randint(1,3)
print computer_input

