def selectionsort(array):
    i=0
    while i<len(array):
        j=i
        k=i+1
        while k<len(array):
            if array[k]<array[j]:
                j=k
            k=k+1
        array[i],array[j]=array[j],array[i]
        i=i+1
array1=[3,6,8,7,3,3,2]
selectionsort(array1)
print(array1)
