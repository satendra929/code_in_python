
s="racecarenterelephantmalayalam"

for i in range (len(s)-1) :
    for j in range (len(s)-1,i,-1) :
        temp2=j
        temp=i
        check=True
        while temp <= temp2 : 
            if s[temp] == s[temp2] :
              temp+=1
              temp2-=1
            else :
                check=False
                break
        if check == True :
            print i , j
            print s[i:j+1]
