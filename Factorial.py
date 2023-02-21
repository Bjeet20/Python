#fact of n
n=int(input("Enter a number:"))
a=1
f=1
for x in range(1,n+1):
    f=f*a
    a+=1
print(f)

