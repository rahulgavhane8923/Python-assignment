file=open('abc.txt','a')
s=input("enter string to append")
file.write(s)
file.close()
file=open('abc.txt')
print(file.read())
file.close()
