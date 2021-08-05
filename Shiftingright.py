array=[1,2,3,4,5,6]
shift=1
l=[]
for i in range(shift,0,-1):
    l.append(array[-i])
for i in array[:len(array)-shift]:
    l.append(i)
print(l)

