# [PCCE 기출문제] 1번 / 문자 출력
message = "Let's go!"

print("3\n2\n1")
print(message)

# [PCCE 기출문제] 2번 / 각도 합치기
angle1 = int(input())
angle2 = int(input())

sum_angle = angle1 + angle2
print(sum_angle%360)

# [PCCE 기출문제] 3번 / 수 나누기
number = int(input())

answer = 0

for i in range((len(str(number)) + 1) // 2):
    answer += number % 100
    number //= 100

print(answer)

# [PCCE 기출문제] 4번 / 병과분류
code = input()
last_four_words = code[-4:]

if last_four_words == "_eye":
    print("Ophthalmologyc")
elif last_four_words =="head":
    print("Neurosurgery")
elif last_four_words =="infl":
    print("Orthopedics")
elif last_four_words =="skin":
    print("Dermatology")
else:
    print("direct recommendation")
