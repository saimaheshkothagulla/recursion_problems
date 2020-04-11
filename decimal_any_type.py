#binary
def binary(n):
    if(n==0):
        return;
    binary(n//2)
    print(n%2,end="")
binary(11)
print("\n")
#octal
def octa(n):
    if(n==0):
        return;
    octa(n//8)
    print(n%8,end="")
octa(11)
print("\n")
#hexa decimal
def hexa(n):
    if(n==0):
        return;
    hexa(n//16)
    if n%16>=10:
        print(chr(n%16-10+ord("A")),end="")
    else:
        print(n%16,end="")
hexa(18)
