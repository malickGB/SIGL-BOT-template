import os
from discord.ext import commands
from dotenv import load_dotenv


token = os.getenv('BOT_TOKEN')
print(token)
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 'malick#5960'  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$name'):
        await message.channel.send('Hello '+ message.author + '!')


@bot.command()
async def pong(ctx):
    await ctx.send('pong')
token= "ODkyODIxODA0ODY1OTc4NDI4.YVSfGg.PjaWzksYxURpqjmxeceM9U6u1zQ"
bot.run(token)  # Starts the bot