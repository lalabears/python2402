students = []
cnt = 0
while True: # 입력>출력>검색>삭제>수정
    print('-'*35)
    print('\t'+'[학생성적프로그램]')
    print('1. 학생성적입력') 
    #####이름, 국, 영, 수 점수를 입력은 받으면
    # [번호,이름,국,영,수,총합,평균,0]
    print('2. 학생성적수정') 
    # 국, 영, 수 점수를 수정해 볼 수 있음. 
    # (유의:국어를바꾸면, 합,평균)
    print('3. 학생성적삭제') # 도전!!
    print('4. 학생성적전체출력')  ####### 전체 출력 !!!!!!
    print('5. 학생검색출력') # 도전!!
    print('6. 등수처리')   # 얘빼고 다 할 수 는 있음.        
    print('0. 프로그램종료')  ####### 종료 !!!!
    print('-'*35)
    choice = input('원하는 번호를 입력하세요.>>')
    if not choice.isdigit():
        print('숫자만 입력이 가능합니다')
        continue
    choice = int(choice)
    if choice==1:
        print('학생성적입력입니다.')
        cnt += 1
        stu_name = input('학생이름을 입력하세요.>>')
        kor = int(input('국어점수를 입력하세요.>>'))
        eng = int(input('영어점수를 입력하세요.>>'))
        math = int(input('수학점수를 입력하세요.>>'))
        total = kor+eng+math
        avg = total/3
        rank = 0
        student = [cnt,stu_name,kor,eng,math,total,avg,rank]
        students.append(student)
		#print(student)
    # choice 4 에서 여러명을 입력했을때 여러명이 출력되게 해보세요
    elif choice == 4:
        print(' 입력된 학생 정보 입니다 >> ')
        print('-'*60)
        # for i in range(len(stSave)):
        #     print("{}번 \t이름: {} \t국어: {} \t영어: {} \t합계: {} \t평균 : {} \t등수 : {}".format(stSave[i][0],stSave[i][1],stSave[i][2],stSave[i][3],stSave[i][4],stSave[i][5],stSave[i][6] ))
        print("번호 \t이름 \t국어 \t영어 \t합계 \t평균 \t등수")
        print('-'*60)
        for stu in students:
            for i in stu:
                print(i, end = '\t')
            print()
            print()
        print('-'*60)
