import matplotlib.pyplot as plt 
import datetime

date = []
moods = []
energies = []

with open("care_journal_log.txt", "r") as log: 
    for line in log:
        parts = line.strip().split(", ")
        entry_date = parts[0]
        mood = int(parts[2].split(": ")[1])
        energy = int(parts[3].split(": ")[1])
        
        date.append(entry_date)
        moods.append(mood)
        energies.append(energy)

plt.figure()

plt.plot(date, moods, label="Mood", marker='o')
plt.plot(date, energies, label="Energy", marker='o')        

plt.xlabel("your day")
plt.ylabel("wellness levels (1-10)")
plt.title("🌈 your mood and wellness bloom chart 🌈")

plt.legend()
plt.show()  
