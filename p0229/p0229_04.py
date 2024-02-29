# while문과 if문을 사용
# 숫자 두개를 입력받고,(input) 
# 연산자를 입력받아서 (+-*/) (input)
# 계산결과 출력 ( if )
# 무한히 계산하는 계산기를 만드는데 (while)
# 첫번째 숫자에 0을 입력하면 프로그램이 종료가 되는 코드를 만드세요
# break 
# while 조건식: # 조건식이 참일때 실행문 수행 , 
#                   즉 조건식이 거짓일때 while종료
#   실행문
while True: # 무조건 참이기 때문에 while 안에 있는것 계속 반복
    n1 = int(input('첫번째 숫자를입력(종료 0 ) >> '))
    if n1 == 0 :
        print('종료되었습니다')
        break
    n2 = int(input('두번째 숫자 입력 >> '))
    cal = input('연산을 입력(+-*/) >> ')
    if cal == '+':
        print('{}+{}={}'.format(n1,n2,n1+n2))
    elif cal == '-':
        print('{}-{}={}'.format(n1,n2,n1-n2))
    elif cal == '*':
        print('{}*{}={}'.format(n1,n2,n1*n2))
    elif cal == '/':
        print('{}/{}={}'.format(n1,n2,n1/n2))
    else:
        print('연산을 잘못입력하셨습니다. 다시입력해주세요>> ')

    