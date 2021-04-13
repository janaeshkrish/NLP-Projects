a =[1,3,6,2,9]
b =[4,2,5,7,9,1,11,3]

c=[]
for i in a:
	for j in b:
		if i==j:
			c.append(i)
print(c)


s= "my name is janaesh"
l =0 
x=s.strip()
for i in range(len(x)):
	if x[i] == " ":
		l =0
	else:
		l+=1
print(l)