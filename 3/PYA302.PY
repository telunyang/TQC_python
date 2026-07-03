a=int(input())
b=int(input())
result=0
for i in range(a, b+1):
    if i%2==0:
        result=result+1
print(result)