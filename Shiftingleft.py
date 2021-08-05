array=list(map(int,input().split()))
shift=int(input())
l=[]
for i in array[shift:]:
    l.append(i)
for i in array[:shift]:
    l.append(i)
print(l)