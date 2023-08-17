bracket_string="}{{}{}"
b=bracket_string.split()
l=[]
count = 0
for c in b:
    if c=="}" and len(l)==0:
        count+=1
    if c=="{":
        l.append(1)
    if c=="}":
        l.pop()
    if c=="{" and count!=0:
        print("no")
        exit()
if count==0 and len(l)==0:
    print("ok")
else:
    print("no")