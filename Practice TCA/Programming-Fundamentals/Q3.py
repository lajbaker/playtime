print("How many days remain until the next full moon?")
repetitions = int(input())
index = repetitions
print("We must count the days...")
print()
for count in range(repetitions,0,-1):
    print("The full moon will be upon us in " + str(index) + " days.")
    index = index-1
print()
print("It's a full moon. The beast has been unleashed!")
print("May it have mercy on our souls.")