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

@bot.slash_command(name="ping", description="Shows the bot's latency")
async def ping(ctx):
    latency_in_ms = bot.latency * 1000
    await ctx.respond(f"My ping is currently: {latency_in_ms:.0f}ms")

@bot.slash_command(name="fastfetch", description="intel NUC specs from fastfetch")
async def fastfetch(ctx):
    import subprocess
    result = subprocess.run(['fastfetch', '--logo', 'none', '--cpu-temp'], stdout=subprocess.PIPE)
    relevant_info = result.stdout.decode('utf-8')
    converter = Ansi2HTMLConverter(inline=True)
    html_output = converter.convert(relevant_info)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_output, 'html.parser')
    plain_text = soup.get_text('\n', strip=True)
    await ctx.respond('```' + plain_text + '```')

bot.run(os.getenv('TOKEN'))
