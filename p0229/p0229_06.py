# continue 예제
# 1 - 100 합계를 구하는데 3의 배수는 제외하고 더하기 3367
# 1 - 100까지 출력, 3의 배수는 제외하고 출력 
# [1 2 4 5 7 8 10 ... ]
# while or for 사용해서
for i in range(1,101):
    if i%3 == 0:
        continue
    print(i, end=' ')
print()
i = 1
while i<101:
    if i%3 == 0:
        i = i+1
        continue
    print(i, end=' ')
    i = i+1
    
# 3의 배수를 제외하고 더하기 

sum = 0 
for i in range(1,101):
    if i%3 == 0:
        continue
    sum += i 
    
print('\n1-100 3의 배수제외한 합: ',sum)

i = 1
sum1 = 0 
while i<101:
    if i%3 == 0:
        i = i+1
        continue
    sum1 += i
    i = i+1
print('1-100 3의 배수제외한 합: ',sum1)
