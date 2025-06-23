import discord
from discord.ext import commands
from settings.config import DISCORD_TOKEN

# aqui Configuramos los permisos que necesita el bot
intents = discord.Intents.default()
intents.members = True  

# aqui se Crea el bot con el prefijo "!" y los intents configurados
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Este evento se ejecuta cuando el bot esta listo y conectado
    print(f'Bot conectado como {bot.user}')

async def main():
    async with bot:
        await bot.load_extension('cogs.welcome_cog')  # Carga el cog de bienvenida
        await bot.start(DISCORD_TOKEN)  # Inicia sesion con el token

import asyncio
asyncio.run(main()) 
