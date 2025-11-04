import os,datetime 

nickname = "angel"

print(f"\nhi {nickname}! welcome to your care journal. let's take a moment to reflect on your day and jot down some thoughts.\n")
print("there's no rush lovely, just let your thoughts flow naturally and be kind to yourself.\n")
print("let's just take a moment and *breathe deeply* together...\n")

entry = input("whenerver you're ready lovely, what's on your heart today?\n\n")

#save entry
os.makedirs("journals", exist_ok=True) #create a folder if it doesn't exist
filename = f"journals/{nickname} journal_entries.txt"

with open(filename, "a") as file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{timestamp} - {nickname}: {entry}\n")

print(f"\nthank you so much for sharing with me {nickname}, i'm so proud of you for taking this time for yourself!\n")
print("no matter what lovely, you're processing your emotions. you're growing, you're nurturing yourself, you're giving yourself your absolute best!\n")
print("i'm so so proud of you, soft and truly, my angel <3\n")

message = "see you next time lovely <3"
for char in message:
    print(char, end='', flush=True)
    import time
    time.sleep(0.3)
print("\n")
print("────────────────────────────────────────\n")
