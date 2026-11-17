import os
import discord
from discord.ext import commands

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_create, limit=1):
            if entry.user.id == OWNER_ID or entry.user.bot:
                return
            try:
                await channel.delete(reason="Creato senza permesso")
                await channel.guild.kick(entry.user, reason="Ha creato canale senza permesso")
                print(f"Kickato {entry.user} per canale non autorizzato")
            except Exception as e:
                print(e)

async def setup(bot):
    await bot.add_cog(Security(bot))
