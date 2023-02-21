if True:
    print("True 執行")
else:
    print("False執行")
    
x=int(input("請輸入數字："))
if x>200:
    print("大於200")
elif x >100:
    print("大於100且小於等於200")
else:
    print("小於100")

#四則運算
n1=int(input("請輸入數字一："))
n2=int(input("請輸入數字二："))
op=input("請輸入四則運算 + 、 - 、 * 、 / ：")
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("不支援的運算格式")