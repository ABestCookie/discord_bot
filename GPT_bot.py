import discord
from discord.ext import commands
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True  # 必須要開這個

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}!")

@bot.command()
async def ask(ctx, *, question):
    await ctx.send("🤔 Thinking...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
    
        answer = response["choices"][0]["message"]["content"]
    except Exception as e:
        answer=e
    await ctx.send(answer)

bot.run(DISCORD_TOKEN)
