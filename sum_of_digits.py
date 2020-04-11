def sum1(n):
    if n//10==0:
        return n
    return sum1(n//10)+n%10
print(sum1(1912))
