import numpy as np

def load_csv_file(file_path):
    data=np.genfromtxt(file_path,delimiter=',',dtype=None,names=True,encoding='cp949')
    return data

#np.genfromtxt 함수는 넘파이 함수 중 하나로
# 파일에서 데이터를 읽어 넘파이 배열로 변환하는 데 사용한다.

#delimiter 매개변수는 데이터를 구분하는 구분자를 나타냄, csv파일은 쉼표로 구분','
#dtype=None은 데이터의 유형을 넘파이가 알아서 유추하도록 하는 설정
#names=True 파일 데이터에 데이터 헤더(열 이름)이 포함되어 있는지 유무
#encoding='cp949'는 문서의 인코딩 방식이 cp949로 되어있다는 설정, 보통 한글은 utf-8
#데이터 문서는 cp949 인코딩 방식을 사용

file_path='2022.csv'
loaded_data=load_csv_file(file_path)
print(loaded_data)                  # 벡터화된 상태

row_input=input("조회 행 번호 입력: ")
try:
    row_number=int(row_input)
    if row_number<len(loaded_data):
        print(loaded_data[row_number])
    else:
        print("행 번호 범위 에러")
except:
    print("exc에러 - 유효 숫자 입력")
