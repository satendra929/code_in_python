def pairs(n) :
    if n==1 :
        l=['()']
        return l
    else :
        re=pairs(n-1)
        ans=[]
        for i in re :
            ans.append('('+i+')')
            ans.append('()'+i)
        return ans
        

print pairs(3)
