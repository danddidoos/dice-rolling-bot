import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in successfully as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! :ping_pong:")

@bot.command()
async def roll(ctx):
    result = random.randint(1, 6)
    await ctx.send(f"You rolled a {result}!")

bot.run(TOKEN)