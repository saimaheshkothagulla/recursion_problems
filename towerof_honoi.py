def honoi(n,source,temp,des):
    if n==1:
        print("move {}disk from {} to {}".format(n,source,des))
        return
    honoi(n-1,source,des,temp)
    print("move {} dick from {} to {}".format(n,source,des))
    honoi(n-1,temp,source,des)
honoi(3,"A","B","C")