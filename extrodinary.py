def countsustrings(S):
    n1=["a","b"]
    n2=["c","d","e"]
    n3=["f","g","h"]
    n4=["i","j","k"]
    n5=["l","m","n"]
    n6=["o","p","q"]
    n7=["r","s","t"]
    n8=["u","v","w"]
    n9=["x","y","z"]
    div=0
    for l in S:
        if l in n1:
            div+=1
            continue
        elif l in n2:
            div+=2
            continue
        elif l in n3:
            div+=3
            continue
        elif l in n4:
            div+=4
            continue
        elif l in n5:
            div+=5
            continue
        elif l in n6:
            div+=6
            continue
        elif l in n7:
            div+=7
            continue
        elif l in n8:
            div+=8
            continue
        elif l in n9:
            div+=9
            continue
        else:
            print("Invalid String")
    if len(l)%div==0:
        count+=1