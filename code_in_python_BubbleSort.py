#Bubble Sort
import timeit
import random

li=[1,5,2,7,3,2,6,4]
l=[]
for i in range(100) :
    l.append(random.randint(1,100))

#print (l)
temp=0

def bubble (l) :
    st=timeit.default_timer()
    for i in range (len(l)-1) :
        for j in range (i+1,len(l)) :
            if l[i] > l[j] :
                l[i] , l[j] = l[j] , l[i]
    ans=timeit.default_timer()-st
    print ("Sorted using bubble sort")
    print ("Time elapsed : "+(str)(ans))
    print ("Sorted List is : ")
    print (l)

def insertion(li) :
    start=timeit.default_timer()
    for i in range (1,len(li)) :
        val=li[i]
        j=i
        while j > 0 and li [j-1] > val   :
            li[j]=li[j-1]
            j-=1
        li[j]=val
    return li
            

print (insertion (li))


