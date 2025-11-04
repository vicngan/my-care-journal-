#starting a matcha mood tracker 
print("hi lovelies, how are you today?")

sleep = int(input("On a scale of 1-10, how well did you sleep last night? "))
energy = int(input("On a scale of 1-10, how is your energy level? "))
stress = int(input("On a scale of 1-10, how stressed do you feel? "))
mood = int(input("On a scale of 1-10, how is your overall   mood? "))       

average = (sleep + energy + (10 - stress) + mood) / 4

print(f"Your matcha mood score for today is: {average:.2f}/10")

if average >= 8:
    print("you're doing well lovely, keep glowing!!")
elif average >= 5:
    print("you're doing okay, take some time for yourself today.")
else:
    print("it's okay to have tough days, grab a matcha and remember to be kind to yourself.") 

#end of matcha mood tracker 
