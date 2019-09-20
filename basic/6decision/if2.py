score = int(input("당신의 점수를 입력해주세요: "))
if score >= 90:
    print(score)
    print("A grade")
if score == 100:
    print("You are perfect.")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("F grade")
