statement="hi hello how are you"
# statement=statement.split()
# output=" ".join(statement[::-1])
# print(output)
l=[""]
output=""
for i in statement:
    if i==" ":
        l.append('')
    else:
        l[-1]+=i
for i in range(1,len(l)+1):
    output+=l[-i]

    if i!=len(l):
        output+=" "
print(output)