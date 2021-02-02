pi_list = list()
n=1
pi1 = int(n+2)
pi2 = 4
 
for i in range(10):
    
    pi3 = (pi1 / pi2)
    
    pi_list.append(pi3)
    
    pi2 += 2
 
    pi=sum(pi_list[0::2])-sum(pi_list[1::2])
