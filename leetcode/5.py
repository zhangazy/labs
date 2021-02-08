n = int(input())
pro = 1
sum = 0
while n > 0:
    a = int(n %10)
    n//=10
    sum+=a
    pro*=a 
result = pro - sum
print(result)