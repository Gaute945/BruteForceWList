import fileinput as fi
from keyboard import write, press_and_release
from time import sleep
import random

#use multiple txt files
with fi.input(files=["zero-10.txt", "english.txt", "10-million-password-list-top-1000000.txt"]) as f:
    for line in f:
        delay = random.randrange(0,3)
        write(line)
        sleep(delay)
        press_and_release("enter")