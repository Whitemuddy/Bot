import discord
from discord.ext import commands
import sys
import os

class restart_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='restart', aliases=['res'])
    async def restart(self, ctx):
        embed = discord.Embed(color=discord.Color.blurple())
        embed.add_field(name='Restarting...',
                        value='This can take some time!')
        await ctx.send(embed=embed)
        os.startfile('C:/Users/Whitemuddy/Desktop/bot/Bot_kobi/run.bat')
        sys.exit()
