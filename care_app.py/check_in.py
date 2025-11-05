#check_in.py
import utils
import affirmation
from utils import blossom_drift

import time
def typeprint(text, speed=0.07):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(speed)
        print()

def run (nickname ="angel"):
    print(f"\hi {nickname}! i'm glad you're here. let's check in for just a moment:)\n")
    print("no pressure lovely, just be honest with yourself and take your time!\n")

    mood = input("how are you feeling right now lovely, just one word is okay:")
    energy = input("\nhow is your energy level for today (on a scale of 1-10):")
    body = input("\nhow is your body feeling today (on a scale of 1-10):")
    gratitude = input("in one word, what are you grateful for today:")

    typeprint(f"\nthank you for sharing with me {nickname}, i'm beyond proud of you and don't forget to be kind to yourself!\n")
    typeprint("remember, every feeling is valid and it's okay to have ups and downs. you're doing amazing!\n")


    if int(energy)<= 4 or int(body)<= 4:
        print("it seems like you're having a rough day {nickname}. that's completely okay. remember to take breaks, breathe deeply, and be gentle with yourself. you're doing the best you can, and that's more than enough.be kind to yourself love <3\n")
    elif int(energy)>= 7 and int(body)>= 7:
        print("a soft day today {nickname}! that's wonderful to hear. make sure to savor these moments of high energy and well-being. consider engaging in activities that bring you joy and fulfillment. keep shining your beautiful light!\n")
    else:
        print("there's a little spark in you today {nickname}. that's great! try to focus on activities that can help boost your energy and improve your mood. remember, it's okay to have ups and downs. you're doing amazing!\n")
    print("-----------------------------\n")

    #gentle reflection    
    typeprint(f"here's a little note for you {nickname}:\n")
    print("-----------------------------\n")

    typeprint("remember, no matter what, i am here for you and proud of you always <3\n")
    typeprint("take care lovely, and don't forget to treat yourself with kindness and compassion!\n")   
    typeprint("i'm proud of you for checking in at all, that's a big step towards self-care and well-being!\n")
    typeprint(f"here's an affirmation for you today {nickname}: \n")
    typeprint("you got this lovely <3\n") 

    message = "see you next time lovely <3"
    for char in message:
        print(char, end='', flush=True)
        import time
        time.sleep(0.3)
    print("\n")
    print("────────────────────────────────────────\n")

    blossom_drift()

    #optional test run when executed directly
if __name__ == "__main__":  
        run("angel")