
num = [[10,20],[30,40],[50,60]]

for i in range(len(num)): # i = 0, 1, ..
    for j in range(len(num[i])): # j = 0, 1 ..
        print(num[i][j]) # num[0][0] num[0][1]

i = 0
while i < len(num):
    j = 0 
    while j < len(num[i]):
        print(num[i][j])
        j = j+1
    i += 1
    
students = [[1,'홍길동',100],[2,'이순신',90], 
            [3,'유관순',85],[4, '김유신', 70],
            [5, '김구',95]]


searName = input('검색하고싶은 학생의 이름을 입력해주세요 >> ')
for i,m in enumerate(students): # m = [1,홍길동]  , [2, 유관순] ... 
    if searName in m:
        print('{}\t{}'.format(students[i][0], students[i][1]))

i = 0
while i<len(students):
  # print(students[i])
  if searName in students[i]:
    print('{}\t{}'.format(students[i][0], students[i][1]))
  i = i + 1
  
  
        