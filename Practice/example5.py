a = []
n = int(input())
for i in range(1,n+1):
    b = int(input())
    a.append(b)
a.sort()
print("largest element is :",a[n-1])
