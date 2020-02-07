
def mergeList(a,b):

    size=len(a)+len(b)

    i=0
    j=0
    k=0

    temp=[None]*size

    while i<len(a) and j<len(b):


        if(a[i]<=b[j]):

            temp[k]=a[i]

            i=i+1

        else:
            temp[k]=b[j]
            j=j+1


        k=k+1



    while i<len(a):


        print(i)

        temp[k] = a[i]

        i = i + 1

        k=k+1


    while (j < len(b)):
        temp[k] = b[j]
        j = j + 1
        k = k + 1



    return temp







if __name__=="__main__" :

    a=[None]*8

    a=[1,3,5,7]

    b=[2,4,6,8]

    a=mergeList(a,b)


    print(a)