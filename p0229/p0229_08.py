# 1-100 까지 더하는데, 
# 총 합이 100이 넘었을때 총합과, 그 수를 출력하세요
# 1 + 2+ ....           105,     14

# ex) 1 - 10 까지 더하는데 총합이 4가넘는순가의 수를 출력 
# 1+2+3 총합: 6 수 3:

# for while 둘중 하나 사용해서 
sum = 0
for i in range(1,101):  
    sum += i
    if sum > 100 :
        break

print('수 : ', i)       
print('총합 : ', sum)  

# while 
total = 0 
i = 1
while i <= 100:
    total += i 
    if total >100:
        break
    i += 1 
    
print(i)
print(total)    
        
 