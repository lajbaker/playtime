#Under function
def underBanner(message):
    print("Halloween")
    print("-"*len(message))
    print(message)
#Over function
def overBanner(message):
    print(message)
    print("-"*len(message))
    print("Halloween!")
#Both function    
def bothBanner(message):
    print(message)
    print("-"*len(message))
    print("Halloween!")
    print("-"*len(message))
    print(message)
#Grid function
def gridBanner(message):
    if len(message) <= 5:
        for count in range(0,len(message),1):
            index = 1
            for count in range(0,len(message),1):
                if index < len(message):
                    print("Halloween | ", end="")
                    index += 1
                else:
                    print("Halloween", end ="")
            print("")
    else:
        for count in range(0,5,1):
            index = 1
            for count in range(0,5,1):
                if index < 5:
                    print("Halloween | ", end="")
                    index += 1
                else:
                    print("Halloween", end="")            
            print("")


print("Welcome to banner assist. Please enter your message below:")
message = input() 
print()
print("Please select from the following options:")
print("1) Under - display the word \"Halloween\" with a line under it and then the message under the line. ")
print("2) Over - display the message with a line under it followed by the word \"Halloween\".")
print("3) Both - display the message above and below the word \"Halloween\".")
print("4) Grid - display the word \"Halloween\" in a grid that is n x n in size.")
print()
print("Please make your choice (1 to 4):")
while True:
    try:
        choice = int(input())
        break
    except ValueError:
        print("Please enter a number between 1 and 4:")
print()

if choice == 1:
    underBanner(message)
elif choice == 2:
    overBanner(message)
elif choice == 3:
    bothBanner(message)
elif choice == 4:
    gridBanner(message)
else:
    print("invalid entry")
