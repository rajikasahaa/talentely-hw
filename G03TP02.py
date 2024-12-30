#basic calculator

print("BASIC CALCULATOR : This calculator can perform four basic operations! \n")
print("Select an operation to perform:")
print("1. ADDITION \n2. SUBTRACTION \n3. MULTIPLICATION \n4. DIVISION \n")
op=int(input("ENTER THE CORRESPONDING NUMBER : "))

if op==1:
    #code for addition
    num1=float(input("ENTER THE FIRST NUMBER- "))
    num2=float(input("ENTER THE SECOND NUMBER- "))
    sum=num1+num2
    print("ANSWER: ",sum)
elif op==2:
    #code for subtraction
    num1=float(input("ENTER THE FIRST NUMBER- "))
    num2=float(input("ENTER THE SECOND NUMBER- "))
    diff=num1-num2
    print("ANSWER: ",diff)
elif op==3:
    #code for multiplication
    num1=float(input("ENTER THE FIRST NUMBER- "))
    num2=float(input("ENTER THE SECOND NUMBER- "))
    product=num1*num2
    print("ANSWER: ",product)
elif op==4:
    #code for division
    num1=float(input("ENTER THE FIRST NUMBER- "))
    num2=float(input("ENTER THE SECOND NUMBER- "))
    if num2==0:
        print("numbers cannot be divided by zero")
    else:
        div=num1/num2
        print("ANSWER: ",div)
else:
    print("INVALID ENTRY, ENTER A VALID NUMBER")