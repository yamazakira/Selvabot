import discord 
import responses
from discord.ext import commands
import json
from keep_alive import keep_alive

# Enviar mensagem
async def enviar_msg(msg, user_msg):
  try:
    response = responses.handle_response(user_msg)
    await msg.channel.send(response)

  except Exception as e:
    print(e)


def rodar_bot():
  with open('config.json', 'r') as f:
    data = json.load(f)
    TOKEN = data['TOKEN']

  intents = discord.Intents.default()
  intents.message_content = True
  bot = commands.Bot("&", intents=intents)

  @bot.event
  async def on_ready():
      print(f'{bot.user} está rodando!')
    
  # Comando com envio de imagem
  @bot.command(pass_context=True)
  async def duduperna(ctx):
      await ctx.send('Dudu pernas divinas!', file=discord.File('media/duduperna.png'))
  
  # Comando com envio de imagem
  @bot.command(pass_context=True)
  async def negros(ctx):
      await ctx.send(file=discord.File('media/duduperna.png'))
    
  keep_alive()
  bot.run(TOKEN)