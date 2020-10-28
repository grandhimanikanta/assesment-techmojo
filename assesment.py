Assesment
==============
Question 1
================

d={}
f=open("data.txt","r")
for s in f:
    # print(s)
    l=s.split()
    # print(l)
    for i in l:
        if i.startswith("#"):
            if i in d:
                d[i]=d[i]+1
                # print(d)
            else:
                d[i]=1
                # print(d)
    sorted_d = sorted(d.items(), key=lambda x: x[1])
f.close()
print(d)
count=0
for key,values in d.items():
    if count !=10:
        print(key,values)
        count=count+1
    else:
        break
