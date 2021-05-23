# 설문조사 인원수 입력
N = int(input())
C = 0
cute_c = 0
notcute_c = 0

# 인원수대로 1, 0으로 답하기
for i in range(N) :
    if int(input()) == 1 :
        cute_c += 1
    else :
        notcute_c += 1

# 1이 더 많으면 "Junhee is cute!" 출력, 0이 더 많으면 "Junhee is not cute!" 출력
if cute_c > notcute_c :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
    


