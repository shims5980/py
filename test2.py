import numpy as np
testarr=np.array([1,2,3,4],int)
print('-----testarr-----')
print(testarr)
print(type(testarr))
print(type(testarr[1]))

testarr1=np.array(['1','2',3,4],np.int64)
print('\n-----testarr1-----')
print(testarr1)
print(type(testarr1))
print(type(testarr1[1]))
print(testarr1.dtype)
print(testarr1.shape)       # 1차원벡터으로 열 결과 출력 (2차원=매트릭스)

# 3개의 차원에 2행,4열이 3덩어리 -> (텐서)
testarr2=np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                   [[9, 10, 11, 12], [13, 14, 15, 16]],
                   [[17, 18, 19, 20], [21, 22, 23, 24]]])
print('\n-----testarr2-----')
print(testarr2)
print(testarr2.ndim)        # ndim property로 testarr2지원
print(testarr2.size)        # 총량

#reshape함수로 배열의 형태 변환
test_reshape=np.array(([1,2,3,4],[5,6,7,8]), int)
print('\n-----test_reshape-----')
print(test_reshape)
print(test_reshape.shape)
print(test_reshape.size)

print('\n-----test_reshape2-----')
test_reshape2=test_reshape.reshape(8,)      # 사이즈만 같으면 자유롭게 변환 가능
print(test_reshape2)
print(test_reshape2.size)

print('\n-----test_reshape.flatten()-----')
print(test_reshape.flatten())

testindex=np.array(([1,2,3], [4,5,6]),int)
print('\n-----testindex-----')
print(testindex)
print(testindex[0])
print(testindex[1])
print(testindex[1][2])

print('\n-----testindex[0,0]=100-----')
testindex[0,0]=100
print(testindex)


testsl=np.array(([1,2,3,4],[5,6,7,8],[9,10,11,12]),int)
print('\n-----testslice-----')
print(testsl)
print(testsl.shape)
print(testsl.size)

print(testsl[:,:])           # 행 전체, 열 전체 slice
print(testsl[:,:3].shape)    # 3행까지 slice

print('\n-----arange test-----')
spl=np.arange(40)       # 0~39
print(spl)

print('\n-----np.ones마스크 test-----')
print(np.ones(shape=(10,),dtype=np.int32))      # 10개 원소 벡터
print(np.ones(shape=(5,2),dtype=np.int32))      # 5x2 매트릭스

print('\n-----np.zeros마스크 test-----')
print(np.zeros(shape=(10,),dtype=np.int32))      # 10개 원소 벡터
print(np.zeros(shape=(5,2),dtype=np.int32))      # 5x2 매트릭스

print('\n-----np.empty마스크 test-----')
print(np.empty(shape=(10,),dtype=np.int32))      # zero와 똑같이 0으로 채워지지만 empty는 데이터 할당X
print(np.empty(shape=(5,2),dtype=np.int32))      # 칸은 생성, 내용은 비어있음

print('\n-----np.identity test-----')
print(np.identity(n=5, dtype=np.int32))         # 5x5 생성, 대각선으로 1 채움

print('\n-----np.eye test-----')
print(np.eye(N=3, M=5, dtype=np.int64))            # dtype 지정 안할 시 '.'이 찍혀나옴(실수, 부동소수점)

print('\n-----')
print(np.eye(3,5,k=3))                  # 3(k)번째 인덱스부터 사선으로 1출력

print('\n-----np.diag test-----')
print(np.diag(        np.eye(3,5,k=3, dtype=np.int32)       ))          # 매개변수 1개
print(np.diag(        np.eye(3,5,k=3, dtype=np.int32), k=3       ))     # 매개변수 2개

print('\n-----np.random test-----')
print(np.random.uniform(0, 1, 10).reshape(2,5))      # 최소0, 최대1, 10개, 균등분포

print('\n-----np.random 균등분포 test-----')
sum=0
arr=np.random.uniform(0, 1, 1000)
for i in range(1000):
    element=arr[i]
    sum+=element
print('균등분포: ', sum/1000)         # 균등분포에서 샘플링 개수가 높아질수록 평균은 절반에 수렴

print('\n-----np.random 정규분포 test-----')
arr_normal=np.random.normal(0, 10, 1000)
#print(arr_normal)

sum=0
for i in range(arr_normal.size):
    ele=arr_normal[i]
    sum+=ele
print(sum/1000)

print('\n-----numpy 집계함수(sum()) test-----')
arr_1=np.arange(1, 11)
print(arr_1)
print(arr_1.sum())                      # 1차원 벡터


arr_2=np.arange(1,13).reshape(3,4)
print(arr_2)
# 2차원 매트릭스로 행방향, 열방향 집계 순서 정하기
print(arr_2.sum(axis=0))            # 행방향
print(arr_2.sum(axis=1))            # 열방향

print('\n-----vstack, hstack test-----')
a=np.array([1,2,3])
b=np.array([4,5,6])
print('vstack\n',np.vstack((a,b)))         # 행 추가 방식
print('\nhstack\n',np.hstack((a,b)))         # 열 추가 방식 -> 하나의 벡터

print('\n-----concatenate test-----')
a=np.array([[1,2,3]])
print(a)
b=np.array([[4,5,6]])
print(b)

print('axis=0\n',np.concatenate((a,b), axis = 0))
print('\naxis=0 & reshape(1,6)\n',np.concatenate((a,b), axis = 0).reshape(1,6))
print('\naxis=1\n',np.concatenate((a,b), axis = 1))

print()
a=np.array([[1,2],[3,4]])
print(a)
b=np.array([[5,6]])
print(b)
print('b배열은',b.ndim,'차원')         # 몇 차원인지
print(np.concatenate((a,b.T),axis=1))   # T=Transpose -> 배열의 형태를 가로에서 세로로 변환 -> 새로운 행에 붙는 것이 아닌 새로운 열에 붙음


print()
oper_arr=np.array([1,2,3])
print(oper_arr)
print('\n같은 자리 덧셈',oper_arr + oper_arr)
print('\n같은 자리 곱셈',oper_arr * oper_arr)
print('\n같은 자리 나눗셈',oper_arr / oper_arr)


print()
broad_arr=np.array([[1,2,3], [4,5,6]])
print(broad_arr)
x=10
print('\n모든자리 10 덧셈\n',broad_arr + x)         # 스칼라 = 단일값
print('\n모든자리 10 뺄셈\n',broad_arr - x)         # 매트릭스 스칼라 결과
print('\n모든자리 10 곱셈\n',broad_arr * x)
print('\n모든자리 10 나눗셈\n',broad_arr / x)

print()
broad_matrix=np.arange(1,13).reshape(4,3)
print('\nbroad_matrix\n',broad_matrix)
broad_vector=np.arange(10, 40, 10)
print('\nbroad_vector\n',broad_vector)
print('\nbroad_matrix + broad_vector\n', broad_matrix + broad_vector)

print()
comp=np.arange(10)
print(comp)
print(comp>6)              # 모든 요소에 >6 조건 브로드캐스팅
print(np.all(comp>=0))      # All(==and):모든 요소 충족 시, Any(==or):한 요소라도 충족 시

print()
where_arr=np.arange(10)
print(where_arr)
print(np.where(where_arr>6,1,0))        # where>6은 조건식, 1은 참(true)일 때 리턴 값, 0은 거짓(false)일 때 리턴 값
print(np.where(where_arr>0,0,255))

print('\n-----nans test-----')
def nans(shape, dtype=np.float64):
    a=np.empty(shape, dtype)           # 칸만 생성
    a.fill(np.nan)                     # 칸을 nan으로 채움
    return a
print(nans([3,4]))

print()
nan_arr=np.array([1,2,3,np.nan,5])
print(np.isnan(nan_arr))            # is 로 시작하면 값은 true, false
print(np.isnan(nans([3,4])))

print()
arg_arr=np.array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18]])
print(arg_arr)
print(np.argmax(arg_arr, axis=0))










