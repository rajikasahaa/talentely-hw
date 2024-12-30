#year is a leap year if it is divisible by 4 and 100 if it isnt divisible by 100 its not a centuary year but can still be a leap year
while True:
    
    try:
        year=int(input("ENTER YEAR: "))
        
    except:
        print("INVALID DATA TYPE")
    else:
        if year%400==0 and year%100==0:
            print(year," is a leap year (and a centuary year).")
        elif year%4==0 and year%100!=0:
            print(year," is a leap year (and not a centuary year).")
        else: 
            print(year," is not a leap year.")
    
    
    ch=int(input("ENTER 0 TO STOP: "))
    if ch==0:
        break