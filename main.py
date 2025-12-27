import discord
from discord.ext import commands
import google.generativeai as genai
import os

# O Render vai ler estes valores das "Environment Variables" de forma segura
TOKEN_DISCORD = os.getenv("MTQ1NDI4MTQxMjg4NTc0NTY5NQ.GNoUmA.y2plJ4jwZUSB7BOpqLbObyDsGdl0MndGJ-4oWM")
CHAVE_IA = os.getenv("AIzaSyCui5cOqukzpXv37CJrMmYcsnLboNKNzAk")

# Configuração da IA (Gemini 1.5 Flash - Gratuito e rápido)
genai.configure(api_key=CHAVE_IA)
model = genai.GenerativeModel('gemini-1.5-flash')

# Configurações de permissões do Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Mensagem que aparece nos Logs do Render quando o bot liga
    print(f'🕶️ Lester na nuvem! Delegado Torcato no comando.')

@bot.command()
async def lester(ctx, *, pergunta):
    # O prompt que dá a personalidade do Lester ao bot
    prompt = f"Tu és o Lester do GTA V. És sarcástico, inteligente e ajudas a turma 10 CNT da Escola Rocha Peixoto. Responde a isto: {pergunta}"
    try:
        response = model.generate_content(prompt)
        await ctx.send(f"🤖 **Lester AI:** {response.text}")
    except Exception as e:
        await ctx.send(f"❌ Erro no sistema: {e}")

@bot.command()
async def delegado(ctx):
    await ctx.send("👮‍♂️ **O Boss desta operação é o Torcato Maravalhas da 10 CNT. Respeitem o homem!**")

# Liga o bot usando o Token que configuraste no Render
bot.run(TOKEN_DISCORD)
