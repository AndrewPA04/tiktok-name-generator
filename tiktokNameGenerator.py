import requests
import asyncio
import random
import string

async def generator():
        counter = 0
        while(counter<500):
            generatedName = ""
            counter += 1
            for index in range(4):
                randomChar = random.choice(string.ascii_letters)
                generatedName += randomChar
            response = requests.get(f"https://www.tiktok.com/@{generatedName}")
            if response.status_code == 200:
                print(f"[taken] {generatedName}")
            else:
                print(f"[Not taken] {generatedName}")

asyncio.run(generator())
