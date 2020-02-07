

def mergeList(a,b):


    i=0

    j=0

    k=0

    while j<len(b) and i<len(a):

        # print(i)

        if(a[i]<b[j]):

            i=i+1

        else:

            k=len(a)

            print(k)

            while(k>i):

                # print(k)
                a.insert(k,a[k-1])
                k=k-1




            a[i]=b[j]

            # print(i)

            j=j+1
            i=0


    return a







if __name__=="__main__" :

    a=[None]*6

    a=[1,3,9]

    b=[2,4,6]

    a=mergeList(a,b)


    # print(a)