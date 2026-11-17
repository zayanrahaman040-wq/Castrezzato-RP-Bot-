import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Online come {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} comandi")
    except Exception as e:
        print(e)

async def main():
    async with bot:
        await bot.load_extension("owner")
        await bot.load_extension("security")
        await bot.start(os.getenv("DISCORD_TOKEN"))

import asyncio
asyncio.run(main())
