def print1(n):
    if n==0:
        return
    print(n,end=" ")
    print1(n-1)
print1(10)
print("\n")
def print2(n):
    if n==0:
        return
    print2(n-1)
    print(n, end=" ")
print2(10)