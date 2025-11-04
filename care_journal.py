import datetime

print("welcome to your care journal!")
name = input("your name, lovely:\n> ")

today = datetime.date.today()
print(f"\nhi {name}, today is {today}. let's reflect on your day.\n")
print("────────────────────────────────────")           

mood = input("how are you feeling today (1-10)?\n> ")
energy = input("how is your energy level (1-10)?\n> ")
gratitude = input("what is one thing you are grateful for today?\n> ")
self_care = input("what is one self-care activity you did today?\n> ")
water = input("how many glasses of water did you drink today?\n> ")

with open("care_journal_log.txt", "a") as log: 
    log.write(f"{today}, name: {name}, mood: {mood}, energy: {energy}, gratitude: {gratitude}, self-care: {self_care}, water: {water}\n")

print("your entry is save with love <3 ")
print(f"\nthank you for journaling today, {name}. remember to take care of yourself!\n")
