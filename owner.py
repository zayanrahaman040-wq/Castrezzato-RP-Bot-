import os
import discord
from discord.ext import commands
from discord import app_commands

MAGIC_WORD = os.getenv("MAGIC_WORD", "drago-rosso-77")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

class PannelloOwner(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Kick", style=discord.ButtonStyle.danger, emoji="👢")
    async def kick_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Usa /kick @utente", ephemeral=True)

    @discord.ui.button(label="Security", style=discord.ButtonStyle.success, emoji="🛡️")
    async def security_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Security ON: chi crea canali senza permesso viene kickato.", ephemeral=True)

    @discord.ui.button(label="Ban", style=discord.ButtonStyle.danger, emoji="🔨")
    async def ban_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Usa /ban @utente", ephemeral=True)

    @discord.ui.button(label="Warn", style=discord.ButtonStyle.primary, emoji="⚠️")
    async def warn_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Usa /warn @utente", ephemeral=True)

    @discord.ui.button(label="Annunci", style=discord.ButtonStyle.primary, emoji="📢")
    async def annunci_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Usa /annuncio testo", ephemeral=True)

    @discord.ui.button(label="Giochi", style=discord.ButtonStyle.primary, emoji="🎮")
    async def giochi_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Giochi: /8ball /moneta /dado", ephemeral=True)

    @discord.ui.button(label="Aiuto", style=discord.ButtonStyle.secondary, emoji="❓")
    async def aiuto_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Prova /help per tutti i comandi", ephemeral=True)

    @discord.ui.button(label="Backup Security", style=discord.ButtonStyle.success, emoji="💾")
    async def backup_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Backup Security attivo.", ephemeral=True)

    @discord.ui.button(label="Log", style=discord.ButtonStyle.secondary, emoji="📜")
    async def log_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Log: controllo ultimi eventi.", ephemeral=True)

    @discord.ui.button(label="Bot", style=discord.ButtonStyle.secondary, emoji="🤖")
    async def bot_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Bot online, ping {round(interaction.client.latency*1000)}ms", ephemeral=True)

class MagicaModal(discord.ui.Modal, title="Pannello Proprietario"):
    parola = discord.ui.TextInput(label="Parola magica", placeholder="Scrivi la parola magica...", style=discord.TextStyle.short)
    async def on_submit(self, interaction: discord.Interaction):
        if self.parola.value != MAGIC_WORD and interaction.user.id != OWNER_ID:
            await interaction.response.send_message("Solo owner o staff autorizzato puo entrare.", ephemeral=True)
            return
        embed = discord.Embed(title="Pannello Proprietario", description="Benvenuto boss 👹", color=0xFF0000)
        await interaction.response.send_message(embed=embed, view=PannelloOwner(), ephemeral=True)

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="proprietario", description="Apri pannello owner")
    async def proprietario(self, interaction: discord.Interaction):
        await interaction.response.send_modal(MagicaModal())

async def setup(bot):
    await bot.add_cog(Owner(bot))
