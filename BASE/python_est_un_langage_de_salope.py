import os

print("PYTHON:\n")
nb = 1231734562630205456
div = 16

code = nb / div
mod = nb % div
print(nb,'/',div,'=',int(code))
print(nb,'%',div,'=',mod)

code2 = nb // div
print(nb,'//',div,'=',int(code2))
