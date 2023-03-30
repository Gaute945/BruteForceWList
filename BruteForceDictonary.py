from keyboard import write, press_and_release
from time import sleep
import random

#writes one list only
with open("10-million-password-list-top-1000000.txt", "r", encoding="utf8") as file:
    lines = file.readlines()

for line in lines:
    delay = random.randrange(0,3)
    write(line)
    sleep(delay)
    press_and_release("enter")