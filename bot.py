import discord
import os
import random
from discord.ext import commands
from discord.ext import tasks
from ansi2html import Ansi2HTMLConverter
import dotenv
from dotenv import load_dotenv
import subprocess

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
intents = discord.Intents.all()
bot = commands.Bot()

@bot.slash_command(name="roll", description="Roll the dice")
async def roll(ctx):
    rolled_number = random.randint(1, 100)
    await ctx.respond(f'You rolled: 🎲{rolled_number}')

@bot.slash_command(name="temp", description="Pi temperature")
async def temp(ctx):
    import subprocess
    result = subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE)
    await ctx.respond(f"Current Raspberry Pi temperature: {result.stdout.decode('utf-8')}")

@bot.slash_command(name="ping", description="Shows the bot's latency")
async def ping(ctx):
    latency_in_ms = bot.latency * 1000
    await ctx.respond(f"My ping is currently: {latency_in_ms:.0f}ms")

@bot.slash_command(name="neofetch", description="Pi specs from neofetch")
async def neofetch(ctx):
    import subprocess
    result = subprocess.run(['neofetch', '--stdout'], stdout=subprocess.PIPE)
    relevant_info = result.stdout.decode('utf-8')
    converter = Ansi2HTMLConverter(inline=True)
    html_output = converter.convert(relevant_info)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_output, 'html.parser')
    plain_text = soup.get_text('\n', strip=True)
    await ctx.respond('```\n' + plain_text + '```')

bot.run(os.getenv('TOKEN'))