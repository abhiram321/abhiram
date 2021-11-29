str1 = input("Enter a string : ")
wlist = str1.split()
count= []
for i in wlist:
    count.append(wlist.count(i))
print("count of the occurrence:" + str(list(zip(wlist, count))))
