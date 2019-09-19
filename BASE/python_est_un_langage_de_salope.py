import os

print("PYTHON:\n")
nb = 1231734562630205456
div = 16

code = nb / div
mod = nb % div
print(nb,'/',div,'=',int(code))
print(nb,'%',div,'=',mod)
print("\n")
print("BC :\n");
os.system("echo \"1231734562630205456 / 16\" > div")
os.system("cat div && bc < div")
os.system("echo \"1231734562630205456 % 16\" > modulo")
os.system("cat modulo && bc < modulo")


