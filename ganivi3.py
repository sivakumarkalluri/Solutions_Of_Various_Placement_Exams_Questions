input1="abcdd"
l=[]
for i in input1:
    l.append(input1.count(i))
print(input1[l.index(max(l))])

