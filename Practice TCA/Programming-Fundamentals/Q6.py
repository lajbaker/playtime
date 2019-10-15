#First function - zombie speed
def is_slow_zombie(speed):
    if speed < 5:
        speed = True
    else:
        speed = False
    return speed
#Second function - take action
def take_action(mutation, speed):
    if is_slow_zombie(speed) == True:
        print("This " + mutation + " zombie is a slow zombie. You can run around it!")
    else:
        print("This " + mutation + " zombie is a fast zombie. You better hide!")
#Third function - run function
def run():
    print("Enter the mutation type:")
    mutation = input()
    print("Enter the speed:")
    speed = int(input())
    print("What do you wish to do (identify or action)?")
    choice = input()
    if choice == "identify":
        print("A slow zombie: " + str(is_slow_zombie(speed)))
    elif choice == "action":
        take_action(mutation, speed)
    else:
        print("Unknown Zombie!")

run()

     