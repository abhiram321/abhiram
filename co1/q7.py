
a=[1,3,5,7,9,11,34]
b=[5,13,45,7,20,65,1]
s=int(0) 
c=int(0)

if len(a)==len(b):
  print("Lists are of same length") 
else:
  print("Lists have different length")

for i in range(0,len(a) and len(b)): 
  s=s+a[i]
  c=c+b[i]
if(s==c):
  print("equal sum")
else:
  print("not same sum")

print("Elements that matched are:") 
l=[]
for i in range(0,len(a)):
  for j in range(0,len(b)):
    if a[i]==b[j]:
        l.append(a[i] and b[j]) 
    else:
      continue
print(l)
