def pow(n,b):
    if n==0:
        return 1
    return b*pow(n-1,b)
print(pow(5,2))