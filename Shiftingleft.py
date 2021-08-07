array=list(map(int,input().split()))
shift=int(input())
l=[]
if shift>size:
    shift=shift-size
for i in array[shift:]:
    l.append(i)
for i in array[:shift]:
    l.append(i)
print(l)
