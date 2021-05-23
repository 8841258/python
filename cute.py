# 설문조사 인원수 입력
N = int(input())
C = 0
array = []

# 인원수대로 1, 0으로 답하기
while C < N :
    A = int(input())
    array.append(A)
    S = sum(array)
    C += 1

# 1이 더 많으면 "Junhee is cute!" 출력, 0이 더 많으면 "Junhee is not cute!" 출력
if S > N - S :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
    


