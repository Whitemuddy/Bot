from discord.ext import commands
from music_cog import music_cog
from restart_cog import restart_cog

bot = commands.Bot(command_prefix='-')
bot.remove_command('help')
bot.add_cog(music_cog(bot))
bot.add_cog(restart_cog(bot))
bot.run("your token")



