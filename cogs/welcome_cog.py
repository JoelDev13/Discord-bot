import discord
from discord.ext import commands
from settings.config import WELCOME_CHANNEL_ID, RULES_CHANNEL_ID

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        # aqui obtengp el canal donde se enviara el mensaje de bienvenida
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            # Creo un embed con mensaje de bienvenida personalizado
            embed = discord.Embed(
                title="¡Bienvenido al servidor!",
                description=(
                    f"Hola {member.mention}, esperamos que disfrutes tu estadía\n\n"
                    f"Por favor, lee las reglas en <#{RULES_CHANNEL_ID}>"  # aqui menciona el canal de reglas para que sea clickeable
                ),
                color=discord.Color.blue()  # Color azul para el embed
            )
            embed.set_image(url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3JvaGp3ZDI4dDViMDNpbDUxNWd1NDNvdXFwYnAzdzQxa2NsMTJwaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/11KzOet1ElBDz2/giphy.gif")
            try:
                await channel.send(embed=embed)  # Envia el embed al canal de bienvenida
            except Exception as e:
                print(f"No pude enviar el mensaje en el canal: {e}") 

async def setup(bot):
    await bot.add_cog(WelcomeCog(bot)) 