def plus(pnum) :
    presult = sum(pnum)
    return presult

if __name__ == "__main__" :
    
    expression = input().split('-')
    
    pnum = [] 
    num = [] 
 
    for exp in expression :
        if '+' in exp :
            pnum = list(map(int, exp.split('+')))  
            presult = plus(pnum)
            num.append(presult)
        else :
            num.append(int(exp))
    
    result = num[0]
    for i in range(1, len(num)) :
        result -= num[i]  
        
    print(result)     
   
