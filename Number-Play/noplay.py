print("Give me a number, and I will confirm if it is a prime number.")
while True:
    try:
        testno = int(input())
        break
    except ValueError:
        print("Please enter a valid number.")    
if testno > 1:
    for i in range(2,testno):
        if (testno % i) == 0:
            print(testno, "is not a prime number.")
            print(i, "times", testno//i,"is",testno)
            break
    else:
        print(testno, "is a prime number.")
else:
    print(testno, "is not a prime number.")
        
        
