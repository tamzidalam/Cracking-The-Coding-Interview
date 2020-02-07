

def searchKey(a,key,low,high):

    if low > high:

        return False

    else:

        mid=(low+high)//2

        if key==a[mid]:

            return mid

        elif key < a[mid]:

            high=mid-1

            return searchKey(a,key,low,high)

        else:

            low=mid+1

            return searchKey(a,key,low,high)



def mergeElements(a,l,r):

    k=0
    i=0
    j=0




    while i< len(l) and j<len(r):

        if l[i]<=r[j]:

            a[k]=l[i]
            i=i+1

        else:


            a[k] = r[j]
            j = j + 1

        k=k+1



    while i<len(l):

        a[k] = l[i]
        i = i + 1
        k = k + 1



    while j < len(r):

        a[k] = r[j]
        j = j + 1
        k = k + 1


def mergeSort(a):

    i=len(a)

    if i==1:
        return

    else:
        mid=len(a)//2

        l=a[:mid]
        r=a[mid:]

        mergeSort(l)
        mergeSort(r)
        mergeElements(a,l,r)





if __name__=="__main__" :


    a=[34,500,93,65,680]




    mergeSort(a)

    k=int(input("Enter the number you want to find:\n"))


    s=searchKey(a,k,0,len(a)-1)


    print(s)