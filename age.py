driving = input("請問你有沒有開過車?")
if driving != '有' and driving != '沒有':
    print("只能輸入   有/沒有")
    raise SystemExit            # raise:觸發...錯誤
                                # sustemexit:系統離開
age = int(input("請問你的年齡?"))

if driving == '有':
    if age >= 18:
        print("你通過測驗了")
    else:
        print("奇怪   你怎麼開過車?")
elif driving == "沒有":
    if age >= 18:
        print("那你可以考駕照了")
    else:
        print("那等你18就可以考了!!!")