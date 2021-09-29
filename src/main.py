import os
from discord.ext import commands
from dotenv import load_dotenv


token = os.getenv('BOT_TOKEN')
print(token)
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 'paulmes#7230'  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    print(bot)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!name'):
        await message.channel.send("Hello " + message.name + "!")

    if message.content.startswith('!count'):
        await message.channel.send("Hello " + message.name + "!")

    if message.content.startswith('!admin'):
        await message.channel.send("Hello " + message.name + "!")

    if message.content.startswith('!mute'):
        await message.channel.send("Hello " + message.name + "!")

    if message.content.startswith('!ban'):
        await message.channel.send("Hello " + message.name + "!")

    if message.content.startswith('!xkcd'):
        await message.channel.send("Hello " + message.name + "!")

    if message.content.startswith('!poll'):
        await message.channel.send("Hello " + message.name + "!")
    
    if message.content.startswith('!tictactoe'):
        await message.channel.send("Hello " + message.name + "!")


@bot.command()
async def pong(ctx):
    await ctx.send('pong')
bot.run(token)  # Starts the bot