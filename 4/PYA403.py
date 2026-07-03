a=[]

while True:
    num=int(input())
    if num==9999:
        break
    else:
        a.append(num)

print(min(a))
