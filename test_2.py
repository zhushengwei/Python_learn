import string

text = open('mess.txt').read()


def my_solution(text):
    s = ""
    for each in text:
        if ord(each) >= ord('a') and ord(each) <= ord("z"):
            s += each 
    print s

if __name__ == '__main__':
    my_solution(text)
