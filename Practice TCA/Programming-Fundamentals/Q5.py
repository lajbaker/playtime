dead_ends = 0
mummies = 0
print("Escaping the tomb...")
for x in range(4):
    print("What lies before me?")
    choice = input()
    if choice == "a dead end":
        dead_ends =+ 1
        print("Time to turn back.")
    elif choice == "a mummy":
        mummies += 1
        print("Better find another way.")
    else:
        "Let's move around it."
print("Encountered "+ str(dead_ends) +" dead ends and " + str(mummies) + " mummies.")
