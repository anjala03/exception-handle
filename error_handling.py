def my_func(): 
     a= int (input ("enter first number"))
     b= int (input ("enter second number"))
     sum=a+b
     print(f"the sum is {sum}")
     return sum


try:
    x= my_func()    
   
except ValueError:
    print("you entered wrong entity, please enter numbers")
    x=my_func()

finally:
    print("exception well handled")


