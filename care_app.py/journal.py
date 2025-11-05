import os,datetime 
import utils
import affirmation
from utils import append_journal_entry, blossom_drift

import time
def typeprint(text, speed=0.07):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(speed)
        print()

def run (nickname ="angel"):
    typeprint(f"\nhi {nickname}! welcome to your care journal. let's take a moment to reflect on your day and jot down some thoughts.\n")
    typeprint("there's no rush lovely, just let your thoughts flow naturally and be kind to yourself.\n")
    typeprint("let's just take a moment and *breathe deeply* together...\n")

    entry = input("whenerver you're ready lovely, what's on your heart today?\n\n")

    entry_line = []
    typeprint("\nyou can continue writing your journal entry. when you're done, just press enter on an empty line to finish:\n")

    while True:
        try: 
              line = input()
        except KeyboardInterrupt:
             print("\ninterrupted. saving your journal entry...\n")
             return
        if line.strip() == "":
            break
        entry_line += line + "\n"

    entry = "\n".join(entry_line).strip()
    if entry:
        append_journal_entry(nickname, entry)
        print(f"\nthank you so much for sharing with me {nickname}, i'm so proud of you for taking this time for yourself!\n")
        print("no matter what lovely, you're processing your emotions. you're growing, you're nurturing yourself, you're giving yourself your absolute best!\n")
        print("i'm so so proud of you, soft and truly, my angel <3\n")
    else: #if no entry
        print("\nno worries lovely, journaling is a personal journey and it's okay to take your time. i'm here whenever you're ready <3\n") 
        print("-----------------------------\n")

    blossom_drift()

    #save entry
    os.makedirs("journals", exist_ok=True) #create a folder if it doesn't exist
    filename = f"journals/{nickname} journal_entries.txt"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"{timestamp}\n{entry}\n\n") 
    print("your journal entry has been saved successfully!\n")
    print("-----------------------------\n")
    
    #gentle reflection    
    typeprint(f"here's a little note for you {nickname}:\n")
    typeprint("remember, journaling is a powerful tool for self-discovery and healing. by taking the time to reflect on your thoughts and feelings, you're nurturing your inner self and fostering personal growth.\n")
    typeprint("be proud of yourself for showing up and being honest with your emotions. you're doing amazing lovely <3\n")
    print("-----------------------------\n")

    message = "see you next time lovely <3"
    for char in message:
        print(char, end='', flush=True)
        import time
        time.sleep(0.3)
    print("\n")
    print("────────────────────────────────────────\n")
# optional direct test
if __name__ == "__main__":
    run()