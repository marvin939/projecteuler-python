def check(n):
    m=0
    for i in range(1,21,1):
        if n%i==0:
            m+=1      
    if m==20:
        return True
    else:
        return False


for i in range(2500,100000000000,1):
    if check(i):
        print(i)



