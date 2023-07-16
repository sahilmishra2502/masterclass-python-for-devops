num1 = int(input("enter a numner 1"))
num2 =int(input("enter a numner 2"))
choice =(input("enter the operation + - / *"))
if choice=="+":
    sum= num1+num2
elif choice=="-":
    diff= num1-num2
elif choice=="*":
    multiply = num1*num2
elif choice=="/":
    divide= num1/num2
else:
    print("invalid choice")
print(sum)
print (diff)
print(multiply)
print(divide)