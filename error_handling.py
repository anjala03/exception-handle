
try:
    a= int (input ("enter first number"))
    b= int (input ("enter second number"))
    sum=a+b
    print(f"the sum is {sum}")
except ValueError:
    print("you entered wrong entity, please enter numbers")
finally:
    print("exception well handled")


