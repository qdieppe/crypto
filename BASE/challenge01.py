#!/bin/python3
def get_base_index(char, base : str) :
    i = 0

    while i < len(base) :
        if base[i] == char :
            return (i);
        i = i + 1
    return (0);

def get_base_char(index : int, base : str) :
    if index < len(base) :
        return (base[index])
    return ("0");

def convert_to_base(nb : int, base : str) :
    baselen = len(base)
    ret = ""

    if (nb <= 0) :
        return (ret);
    extract = nb % baselen
    print(extract)
    return (str(convert_to_base(int(nb / baselen), base)) + str(get_base_char(extract, base)))

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
    return convert_to_base(nb, base2)

def convert_to_base64(num : str, base : str) :
    return convert_base(num, base, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

def convert_to_hex(num : str, base : str) :
    return convert_base(num, base, "0123456789ABCDEF")

def convert_to_dec(num : str, base : str) :
    return convert_base(num, base, "0123456789")

def convert_to_bin(num : str, base : str) :
    return convert_base(num, base, "01")
²
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

if __name__ == '__main__' :
    print(convert_base("F150A", "0123456789ABCDEF", "0123456789ABCDEF"))
    print(convert_hex_to_base64("F150A"))
