a=float(input("Enter the First Number :"))
b=float(input("Enter the Second Number :"))


print("Select the Operators \nPress + for Addition \nPress - for Subtraction \n Press / for Division \nPress * for Multiplication  ")
i=input("Enter operator=")
if (i=="+"):
    print("Result:",a+b)
elif(i=="-"):
    print("Result:",a-b)
elif(i=="/"):
    if b==0:
        print("Error Divion by Zero")
    else:
        print("Result:",a/b)
elif(i=="*"):
    print("Result:",a*b)
else:
    print("Choose from the given Operators ")
