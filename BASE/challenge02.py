import sys
from crypto import *

def clear_lines(lines) :
    ret = []
    var = 0
    for i in lines :
        if i[len(i) - 1] == '\n' :
           var = i[0:len(i) - 1]
        ret.append(var)
    return (ret)

if __name__ == '__main__' :
    f = open(sys.argv[1])
    lines = f.readlines()
    lines = clear_lines(lines)
    print(hex_xor(lines[0], lines[1]))
