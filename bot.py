import logging
import re

import discord
from decouple import config

from cows import random_cow

logging.basicConfig(level=logging.INFO)

TOKEN = config("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

def is_supervocalic(text):
    vowels = {v: False for v in ("a", "e", "i", "o", "u")}
    for char in text:
        if char in vowels:
            if vowels[char]:
                return False
            else:
                vowels[char] = True

    return all(vowels.values())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg_content = message.content.lower()
    print("*")
    print(msg_content)

    if "bug" in msg_content:
        await message.add_reaction("🐛")

    if is_supervocalic(msg_content):
        await message.add_reaction(client.get_emoji(557365346265202688))

    if "secret" in msg_content:
        pass
        # await message.channel.send(file=discord.File("./LOZ_Secret.wav"))

    if re.search(r"\bmemes?\b", msg_content):
        pass
        # await message.channel.send(f"```{random_cow()}```")

@client.event
async def on_ready():
    print(f"Connected as {client.user}")

client.run(TOKEN)
