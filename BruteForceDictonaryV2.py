from keyboard import write, press_and_release
from time import sleep
import random

#combines two txt files
with open("./english.txt", "r", encoding="utf8") as line:
    lines = line.readlines()

with open("./zero-10.txt", "r", encoding="utf8") as date:
    dates = date.readlines()

#repeats for the ammount of lines in english.txt
for line in lines:
    delay = random.randrange(0, 3)
    #removes non text from output
    combined_text = f"{line.strip()}{random.choice(dates).strip()}"
    fix_combined_text = combined_text.strip("\n,'")
    sleep(delay)
    write(fix_combined_text)
    press_and_release("enter")