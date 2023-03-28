# f = open ("data.txt","w")
# f.write("primeira line\n")
# f.write("segunda line\n")
# f.close()

# #escrita final
# f = open ("data.txt",'a')
# f.write("terceira line\n")
# f.close()

# #leitura\
# f = open ("data.txt","r")
# print(f.read())
# f.close()


# lista  = ["segunda","terca","quarta","quinta","sexta","sabado","domingo"]


# f = open("data.txt","r+")

# f.writelines(lista)

# lista = f.readlines()
# print(lista)
# f.close()

import pickle as pk

v1="hello word"
v2=["hello","word"]

f = open("data.dat","wb")
pk.dump(v1,f)
pk.dump(v2,f)
f.close()

#leitura do arquivo bin

f = open("data.dat","rb")
v1 = pk.load(f)
v2 = pk.load(f)
print(v1)
print(v2)
f.close()()

