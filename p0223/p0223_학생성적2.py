stu1 = [1,'홍길동',100,100,100,300, 100.0, 1]
stu2 = [2,'유관순',90,90,90,270,90.0,2]
print('-'*35)
print('[학생성적프로그램]')
print('-'*35)
print('1. 학생성적입력') # 
print('4. 학생성적전체출력') #
print('0. 프로그램 종료 ')
print('-'*35)
choice = int(input('원하는 번호를 입력하세요 >> '))
if choice == 1 :
    print('학생성적입력')
    stu_name = input("이름을 입력하세요 >> ")
    kor = int(input('국어점수를 입력하세요 >> '))
    eng = int(input('영어점수를 입력하세요 >> '))
    math = int(input('수학점수를 입력하세요 >> '))
    stu3 = [3, stu_name,kor,eng,math,(kor+eng+math),(kor+eng+math)/3, 3]
    print(stu3)
elif choice == 4 :
    print('학생성적출력')
    print('[학생 성적 출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],
    stu1[5],stu1[6],stu1[7])) # 홍길동
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    stu2[0], stu2[1], stu2[2],stu2[3],stu2[4],
    stu2[5], stu2[6], stu2[7]
    )) # 유관순
elif choice == 0:
    print('프로그램을 종료합니다')
else:
    print('다시입력해주세요 ')



# 1번을 입력하면 [학생성적입력을 선택하셨습니다] 출력
# 만약 1번인 경우
#  이름, 국,영,수 
#  stu3 =[번호, 이름, 국,영,수, 총,평, 등]
# 4번을 입력하면
# [학생 성적 출력]
# 번호    이름    국어    영어    수학    총점    평균    등수
# 1       홍길동  100     100     100     300     100.0   1
# 2       유관순  90      90      90      270     90.0    2
