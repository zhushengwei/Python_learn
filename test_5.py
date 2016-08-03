# coding:utf-8
import re
import urllib

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

nothing = "12345"
# 匹配以数字结尾的字符串以继续搜索
search = re.compile(" (\d*)$")  
# 匹配最终的网页类型字符串以跳出循环
search_html = re.compile("\.html$")  # 

for i in xrange(400): 
    print "%s: " % nothing,

    line = urllib.urlopen( "%s%s" % (url,nothing) ).read()
    print line

    # 如果找到最终的网页链接则终止查询
    if search_html.findall (line):
        break

    match = search.findall (line)
    if match:
        # 下一个nothing值
        nothing = match [0]
    else:
        # 上一个nothing除以二
        nothing = str(int(nothing) / 2)