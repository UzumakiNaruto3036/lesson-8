n=int(input("enter a number greater than 0:"))
if n<=0:
    print("please enter a number greater than 0")
else:
    print("i will print the numbers from your number to 1:" )
    for i in range(n,0,-1):
        print(i)
        