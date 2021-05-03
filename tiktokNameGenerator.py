from requests import get
from random import choice
from string import ascii_letters

def generator():
    counter = 0
    while(counter<500):
        generatedName = ""
        counter += 1
        for index in range(4):
            randomChar = choice(ascii_letters)
            generatedName += randomChar
        response = get(f"https://www.tiktok.com/@{generatedName}")
        if response.status_code == 200:
            print(f"[taken] {generatedName}")
        else:
            print(f"[Not taken] {generatedName}")
