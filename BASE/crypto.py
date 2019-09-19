#!/bin/python3
def get_base_index(char, base : str) :
    i = 0

    while i < len(base) :
        if base[i] == char :
            return (i);
        i = i + 1
    return (0);

def get_base_char(index : int, base : str) :
    if (index < len(base)):
        return (base[index])
    return ("")

def convert_to_base(nb : int, base : str) :
    baselen = len(base)
    ret = ""

    if (nb == 0) :
        return (ret);
    extract = nb % baselen
    presave = nb
    nb = nb - (extract)
    save = nb
    nb = int(nb) // int(baselen)
    char = str(get_base_char(extract, base))
    return (str(convert_to_base(int(nb), base)) + char)

def convert_to_number(num : str, base : str) :
    baselen = len(base)
    i = 0
    ret = 0

    while i < len(num) :
        ret += get_base_index(num[i], base)
        if i < len(num) - 1 :
            ret *= baselen
        i = i + 1
    return (ret);

def convert_base(num : str, base : str, base2 : str) :
    nb = convert_to_number(num, base)
    return (convert_to_base(nb, base2));

def convert_to_base64(num : str, base : str) :
    return convert_base(num, base, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

def convert_to_hex(num : str, base : str) :
    return convert_base(num, base, "0123456789ABCDEF")

def convert_to_dec(num : str, base : str) :
    return convert_base(num, base, "0123456789")

def convert_to_bin(num : str, base : str) :
    return convert_base(num, base, "01")

def convert_hex_to_base64(num : str) :
    return convert_to_base64(num, "0123456789ABCDEF")

def convert_dec_to_base64(num : str) :
    return convert_to_base64(num, "0123456789")

def convert_bin_to_base64(num : str) :
    return convert_to_base64(num, "01")

def convert_base64_to_hex(num : str) :
    return convert_to_hex(num, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

def convert_dec_to_hex(num : str) :
    return convert_to_hex(num, "0123456789")

def convert_bin_to_hex(num : str) :
    return convert_to_hex(num, "01")

def convert_base64_to_dec(num : str) :
    return convert_to_dec(num, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

def convert_hex_to_dec(num : str) :
    return convert_to_dec(num, "0123456789ABCDEF")

def convert_bin_to_dec(num : str) :
    return convert_to_dec(num, "01")

def convert_base64_to_bin(num : str) :
    return convert_to_bin(num, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

def convert_hex_to_bin(num : str) :
    return convert_to_bin(num, "0123456789ABCDEF")

def convert_dec_to_bin(num : str) :
    return convert_to_bin(num, "0123456789")

def extend_bin_number(num_bin : str, size : int) :
    ret = []
    size_str = len(num_bin)
    i = 0
    k = 0

    while (size_str + i < size) :
        ret.append('0')
        i = i + 1

    while (k < size_str):
        ret.append(num_bin[k])
        k = k + 1

    return (''.join(ret))

def bin_xor(num_bin : str, num_bin2 : str) :
    if (len(num_bin) > len(num_bin2)):
        size = len(num_bin)
    else:
        size = len(num_bin2)

    nb = extend_bin_number(num_bin, size)
    nb2 = extend_bin_number(num_bin2, size)
    ret = []
    count = 0

    while (count < size) :
        ret.append(single_bit_xor(nb[count], nb2[count]))
        count = count + 1;
    return (''.join(ret))

def hex_xor(num0 : str, num1 : str) :
    nb = convert_to_number(num0, "0123456789ABCDEF")
    nb2 = convert_to_number(num1, "0123456789ABCDEF")
    xor = nb ^ nb2
    return convert_to_base(xor, "0123456789ABCDEF")

def single_bit_xor(bit0, bit1) :
    first = int(bit0)
    second = int(bit1)
    return str((first ^ second))

def getBytes(message):
    length = len(message) / 2
    ret = []
    i = 0

    while i < length :
        ret.append(message[i*2 : i*2 + 2])
        i+=1

    return (ret)

def xorBytes(onexor, bytesArray) :
    ret = []
    e = 0
    for e in bytesArray :
        ret.append(hex_xor(e, onexor))
    return (ret);

def getOccurenceChar(char, bytesArray) :
    c = 0
    for i in bytesArray :
        if char == i :
            c = c + 1
    return (c);

def isEnglish(bytesArray) :
    E = getOccurenceChar("45", bytesArray)
    T = getOccurenceChar("54", bytesArray)
    A = getOccurenceChar("41", bytesArray)
    O = getOccurenceChar("4F", bytesArray)
    I = getOccurenceChar("49", bytesArray)
    N = getOccurenceChar("4E", bytesArray)

    S = getOccurenceChar("53", bytesArray)
    H = getOccurenceChar("48", bytesArray)
    R = getOccurenceChar("52", bytesArray)
    D = getOccurenceChar("44", bytesArray)
    L = getOccurenceChar("4C", bytesArray)
    U = getOccurenceChar("55", bytesArray)

    B = getOccurenceChar("42", bytesArray)
    V = getOccurenceChar("56", bytesArray)
    K = getOccurenceChar("4B", bytesArray)
    J = getOccurenceChar("4A", bytesArray)
    X = getOccurenceChar("58", bytesArray)
    Q = getOccurenceChar("51", bytesArray)
    Z = getOccurenceChar("5A", bytesArray)
    return (E + T + A + O - J - X - Q - Z) #+ O + I + N + S + H + R + D + L + U - B - V - K - J - X - Q - Z)

def getxor(onexor, message) :
    ret = [];
    array = getBytes(message)
    ret = xorBytes(onexor, message)
    return (ret)

def getIndex(array) :
    old = 0
    i = 0
    index = 0
    indexs = []
    for e in array :
        if old < e :
            old = e
            indexs.append(i)
            index = i
        i = i + 1
    return (indexs[int(len(indexs) / 2)])

def bruteforcecaesarkey(message):
    i = 0

    keys = []
    while i < 256 :
        xor = getxor(convert_to_base(i, "0123456789ABCDEF"), message)
        keys.append(isEnglish(xor))
        i = i + 1;
    print(getIndex(keys))

if __name__ == '__main__' :
    print(hex_xor("5374616C6C6D616E","426C61636B486174"))
    bruteforcecaesarkey("0430272762112D243635233027786204302727262D2F62232C2662012D2D32273023362B2D2C")
