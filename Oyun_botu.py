import discord
from discord.ext import commands
import oyun

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, size tercihlerinize dayalı bir oyun bulabilirim.')

@bot.command()
async def oyunlar(ctx):
    kategoriler = ", ".join(oyun.oyunlar.keys())
    await ctx.send(f"Lütfen bir kategori seçin: {kategoriler}")

@bot.command()
async def kategori(ctx, kategori):
    if kategori in oyun.oyunlar:
        oyun_listesi = "\n".join([f"{tur}: {', '.join(oyunlar)}" for tur, oyunlar in oyun.oyunlar[kategori].items()])
        await ctx.send(f"İşte {kategori} oyunları:\n{oyun_listesi}")
    else:
        await ctx.send("Belirtilen kategori bulunamadı.")


bot.run("")
