Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ar = ['TOI','Hindu','ET','BM','HT']
ar2 = [0]*5
ar2[0] = 26
ar2[1] = 20.5
ar2[2]= 34
ar2[3] = 10.5
ar2[4] = 18
ar3 = [0]*2
    
m = int(input("Enter the number of costs to be checked"))
for i in range(0,m):
    result = []
    cost = int(input("Enter the cost"))
    for k in range(0,5-1):
        for l in range(k+1,5):
            if(ar2[k]+ar2[l]<=cost):
                result.append([ar[k],ar[l]])
    print(result)
