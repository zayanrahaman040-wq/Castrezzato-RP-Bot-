import sys, types
# Finto audioop per Python 3.13 - cosi discord non crasha
_audioop = types.ModuleType('audioop')
def _return_bytes(fragment, *a, **k):
    return bytes(fragment) if isinstance(fragment, (bytes, bytearray)) else fragment
def _return_zero(*a, **k):
    return 0
def _ratecv(fragment, width, nchannels, inrate, outrate, state, weightA=1, weightB=0):
    return bytes(fragment), state
for _name in ['mul','tomono','tostereo','add','bias','reverse','lin2lin','lin2ulaw','ulaw2lin','lin2alaw','alaw2lin','lin2adpcm','adpcm2lin','getsample']:
    setattr(_audioop, _name, _return_bytes)
for _name in ['minmax','avg','rms','avgpp','maxpp','cross','findfactor','findfit','findmax']:
    setattr(_audioop, _name, _return_zero)
_audioop.ratecv = _ratecv
sys.modules['audioop'] = _audioop

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
