while True:
    #Taking input from the user
    email=input("ENTER YOUR EMAIL ID: ")

    try:
        index= email.index("@")
        #Separating username and domain
        username= email[:index]
        domain= email[index+1:]

        print(f"\nYOUR USERNAME IS {username} AND YOUR DOMAIN IS {domain}")
    #Handling Error    
    except ValueError:
        print("Invalid email id, kindly enter a valid id.")
