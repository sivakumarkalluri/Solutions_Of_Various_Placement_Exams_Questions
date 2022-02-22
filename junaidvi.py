input1="apqresdfe"
input2="pqarsehje"
vowels="AEIOUaeiou"
count1=0
count2=0
for i in  input1:
    if i in vowels:
        count1+=1
for i in input2:
    if i in vowels:
        count2+=1
print(max(count1,count2))


