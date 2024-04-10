import discord
from discord.ext import commands
from bot_logic import *
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We logged in as {bot.user}')

@bot.command('translate')
async def translate(ctx, text, target_language):
    text = translate(text, target_language)
    await ctx.send(f"**Translation:** {text}")

def translate(text, target_language):
    translation = translator.translate(text, dest=target_language)
    return translation

