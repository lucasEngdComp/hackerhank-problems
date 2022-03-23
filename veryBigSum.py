def aVeryBigSum(ar):
    sum=0
    for i in range(len(ar)):
        if ar[i] < 0:
            sum+=abs(ar[i])
        else:
            sum+=ar[i]
    return sum

j =aVeryBigSum([1,1,-10000000000000000000000000000000000000])

print(j)