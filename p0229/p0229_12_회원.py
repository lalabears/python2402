
member = []
cnt = 0 
# 이름을 입력을받아서 [[1, 홍길동] [2,유관순] [3, 이순신]]
while True:
    print('-'*25)
    print('1.입력')
    print('2.전체출력')
    print('3.검색출력')
    print('0.종료')
    ch = input('원하는 번호를 선택하세요 >> ')
    print('-'*25)
    ch = int(ch)
    if ch == 1:
        print('입력')
        name = input('이름을 입력해주세요 ')
        cnt = cnt+1
        m = [cnt, name]
        member.append(m)
    elif ch == 2 : # [[1, '홍길동'], [2, '유관순'], [3, '이순신']]
        # print('출력')
        print('번호\t이름')
        print('-'*20)
        for i in range(len(member)):
            print('{}\t{}'.format(member[i][0], member[i][1]))

        
    elif ch == 0 :
        print('종료')
        break
    else:
        print('다시입력')
        