while Teue:
    a = int(input("Enter a b number less than 25:"))
    if a < 25:
        for i in range(a,26):
            print("Inside the loop, my variable is",i)
        break
    else:
        print("Error")