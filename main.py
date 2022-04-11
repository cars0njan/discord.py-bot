prefix = '='

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help') #optional

####################





####################

TOKEN = #your bot token#
client.run(TOKEN)
