import time
import sys
from pathlib import Path
import datetime

#typing text helper function
def type_out(text, speed=0.05):
    """Simulates typing out text in the terminal."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # Move to next line after typing

#finding/creating data directory and files
DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

MOOD_LOG_FILE = DATA_DIR / "mood_log.txt"
JOURNAL_FILE = DATA_DIR / "journal_entries.txt"

#blossom drifting animation
def blossom_drift(cycles=15, speed=0.22):
    """Simulates a drifting blossom animation in the terminal."""
    width = 40
    height = 10
    blossom = "🌸"
    positions = [(i, j) for i in range(height) for j in range(width)]
    
    for _ in range(cycles):
        x, y = positions[int(time.time() * 1000) % len(positions)]
        sys.stdout.write("\033[2J\033[H")  # Clear screen & reset cursor
        for i in range(height):
            for j in range(width):
                if (i, j) == (x, y):
                    sys.stdout.write(blossom)
                else:
                    sys.stdout.write(" ")
            sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")  # Move down after animation finishes

    def save_mood(mood):
        # code to save mood, now mood is passed in correctly ✨
        with open("mood_log.txt", "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - Mood: {mood}\n")
    def save_journal(entry):
        # code to save journal entry, now entry is passed in correctly ✨
        with open("journal_entries.txt", "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - Entry: {entry}\n") 
    
    return save_mood, save_journal

#journal menu
def cozy_menu(save_mood, save_journal):
    while True:
        type_out("\nCozy Care Menu:", 0.03)
        print("1. Log Mood")
        print("2. Write Journal Entry")
        print("3. View mood log")
        print("4. View journal entries")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")  

        if choice == "1":
            mood = input("How are you feeling today? ")
            save_mood(mood)
            type_out("Mood logged. Take a deep breath and relax.", 0.03)
            blossom_drift()
        elif choice == "2":
            entry = input("Let's write your journal entry: ")
            save_journal(entry)
            type_out("Journal entry saved. Reflect on your thoughts.", 0.03)
            blossom_drift() 
        elif choice == "3":
            if MOOD_LOG_FILE.exists():
                type_out("\nYour progress so far lovely:", 0.03)
                with open(MOOD_LOG_FILE, "r") as f:
                    for line in f:
                        type_out(line.strip(), 0.02)
            else:
                type_out("Your progress haven't started yet, let's take our first step!", 0.03)
        elif choice == "4": 
            if JOURNAL_FILE.exists():
                type_out("\nYour journal entries so far lovely:", 0.03)
                with open(JOURNAL_FILE, "r") as f:
                    for line in f:
                        type_out(line.strip(), 0.02)
            else:
                type_out("Your journal is empty, let's start writing!", 0.03)
        elif choice == "5":
            type_out("Great job showing up for yourself today bestie! 🌸 See you later", 0.03)
            blossom_drift()
            break
        else:
            type_out("Uhm bestie that's not an option but c'mon, we got this together :)", 0.03)

def append_mood_entry(line: str):
    """Appends a mood entry to the mood log file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(MOOD_LOG_FILE, "a") as f:
        f.write(f"{timestamp} - Mood: {line}\n")


def append_journal_entry(line: str):
    """Appends a journal entry to the journal file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(JOURNAL_FILE, "a") as f:
        f.write(f"{timestamp} - Entry: {line}\n")

# entry point 💗 main character moment
if __name__ == "__main__":
    blossom_drift()
    save_mood = append_mood_entry
    save_journal = append_journal_entry 
    cozy_menu(save_mood, save_journal)

