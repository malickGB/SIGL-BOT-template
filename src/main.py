import os
from discord.ext import commands
import discord
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 'paulmes#7230'  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def admin(message, member: discord.Member):
    roles = [o.name for o in message.guild.roles]
    if 'admin' in roles:
        role = discord.utils.get(message.author.guild.roles, name="admin")
    else:
        await message.guild.create_role(name='admin', colour=discord.Colour(0xff0000), permissions=discord.Permissions(8))
        role = discord.utils.get(message.author.guild.roles, name="admin")

    await member.add_roles(role)

@bot.command()
async def name(message):
    await message.channel.send("Hello " + message.author.name + "!")




@bot.command()
async def pong(ctx):
    await ctx.send('pong')

token = ""
bot.run(token)  # Starts the bot