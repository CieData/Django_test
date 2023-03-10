# ----------------------------------------------------------
# 데이터 프레임 요소 다루기
# ----------------------------------------------------------
# 패키지, 모듈 로딩 -----------------------------------------
import pandas as pd

# DF 생성 --------------------------------------------------
data=[[10,20,30],['f','m','m'],[11,22,33],[44,55,66],['A','B','C']]
df1=pd.DataFrame(data)
df1_T=df1.T
df1_T

# DF 요소/원소 다루기 ---------------------------------------
# 열 기준으로 요소
# 0번 컬럼 가져오기
one=df1[0]

print(one,type(one))

# 여러개 컬럼 요소 가져오기
df1[[0,2]]

# 범위 지정 후 요소 가져오기
# 범위 지정 컬럼 추출 불가(행만 가능)
df1[0:1]

# DF 요소/원소 다루기 컬럼---------------------------------------
# 데이터프레임의 컬럼 속성 변경하기 ==> 변수명.속성명=새로운값
df1.columns=['one','two','three']
df1.columns

# 'one'컬럼 가져오기
df1['one']
df1.one

# DF 요소/원소 다루기 행---------------------------------------
# 변수명.iloc[인덱스] - 반드시 정수형 인덱스만 가능
# 변수명.loc[인덱스] - 문자열 인덱스 가능
# 0번 행 데이터 가져오기
zeroRow=df1.iloc[0]
print(zeroRow, type(zeroRow))
# 2개 행 데이터 가져오기
df1.iloc[[0,1]]
df1.iloc[1:4]
df1[1:4]

# 행 인덱스 속성 변경
df1.index=['A','B','C','D','E']
df1.iloc[0] # 행 인덱스 바꿔도 수치값이 남아 있음
df1.loc['A']
#df1.loc[0]  #loc 은 이름 바뀐 인덱스로 사용


# 요소/원소 추출하기 ----------------------------------------------
print('-----------------------------')
df1
# 사용법 : 변수명.iloc[행인덱스, 열인덱스], 변수명.iloc[행인덱스][열인덱스]
# 사용법 : 변수명.loc[행인덱스, 열인덱스], 변수명.loc[행인덱스][열인덱스]
# 요소값이 22,33인 데이터 추출
v33=df1.loc['C','three']
v22=df1.loc['C','two']
v22,v33

# 데이터 44, 66 추출
v46=df1.loc['D',['one','three']]
print(v46,type(v46))

# 데이터 20,30,22,33 추출
v2323=df1.loc[['A','C'],['two','three']]
print(v2323,type(v2323))