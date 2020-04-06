import discord
from discord.ext import commands

TOKEN = 'your token'
bot = commands.Bot(command_prefix='iki-')  #создание префикса

@bot.command(pass_context=True)  #разрешена получение данных о сообщении
async def hi(ctx):  #создаём асинхронную функцию бота
    await ctx.send('И тебе привет, '+ctx.message.author.name)  #отправляем сообщение с именем автора
@bot.command(pass_context=True)
async def say(ctx, *, arg):
    await ctx.send(arg)
@bot.command(pass_context=True)
async def kick(ctx, id):
    await ctx.send('Я пнул этого лоха '+id)
@bot.command(pass_context=True)
async def inventory(ctx, id):
    #код инвентаря, sql, все дела
    await ctx.send()
@bot.command(pass_context=True)
async def inventory(ctx, id):
    #код боёвки. Возможно рандомное число и какой-нибудь коэф или что-то вроде того
    await ctx.send()


bot.run(TOKEN)