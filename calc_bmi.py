# 키와 몸무게를 입력받아 bmi 계산
height = float(input("신장(cm)을 입력하세요. >> "))
weight = float(input("체중(kg)을 입력하세요. >> "))
bmi = weight / (height / 100) ** 2

if bmi >= 30 :
    status = "\"고도비만\""
elif bmi >= 25 :
    status = "\"비만\""
elif bmi >= 23 :
    status = "\"과체중\""
elif bmi >= 18.5 :
    status = "\"정상\""
else :
    status = "\"저체중\""

print("당신의 bmi는 {:.2f}, 현재 상태는 {} 입니다.".format(bmi, status))



