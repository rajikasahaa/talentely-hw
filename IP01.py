#kelvin, celcius, farenheit
while True:

    print("     TEMPERATURE CONVERTOR      \n")

    print("1. Kelvin to Celcius \n2. Kelvin to Farenheit")
    print("3. Celcius to Kelvin \n4. Celcius to Farenheit")
    print("5. Farenheit to Celcius \n6. Farenheit to Kelvin")

    n= int(input("\nEnter the number corresponding to your choice: "))
    if n==1:

        #Kelvin to Celcius (1)
        inp_temp = float(input("\n3ENTER THE TEMPERATURE THAT YOU WANT TO CONVERT: "))
        conv_1= inp_temp - 273.15
        print("\nThe temperature in Kelvin converted to Celcius is: ",conv_1)
    elif n==2:

        #Kelvin to Farenheit (2)
        inp_temp = float(input("\n3ENTER THE TEMPERATURE THAT YOU WANT TO CONVERT: "))
        conv_2= (inp_temp - 273.15) * 18 +32
        print("\nThe temperature in Kelvin converted to Farenheit is: ",conv_2)
    elif n==3:

        #Celcius to Kelvin (3)
        inp_temp = float(input("\n3ENTER THE TEMPERATURE THAT YOU WANT TO CONVERT: "))
        conv_3= (inp_temp + 273.15)
        print("\nThe temperature in Celcius converted to Kelvin is: ",conv_3)
    elif n==4:

        #Celcius to Farenheit (4)
        inp_temp = float(input("\n3ENTER THE TEMPERATURE THAT YOU WANT TO CONVERT: "))
        conv_4= ((9/5)* inp_temp)+32
        print("\nThe temperature in Celcius converted to Farenheit is: ",conv_4)
    elif n==5:

        #Farenheit to Celcius (5)
        inp_temp = float(input("\n3ENTER THE TEMPERATURE THAT YOU WANT TO CONVERT: "))
        conv_5= (5/9)*(inp_temp - 32)
        print("\nThe temperature in Farenheit converted to Celcius is: ",conv_5)
    elif n==6:

        #Farenheit to Kelvin (6)
        inp_temp = float(input("\n3ENTER THE TEMPERATURE THAT YOU WANT TO CONVERT: "))
        conv_6= (5/9)*(inp_temp + 459.67)
        print("\nThe temperature in Farenheit converted to Kelvin is: ",conv_6)
    else:
        print("INVALID INPUT, ENTER AN APPROPRIATE NUMBER \n\n")