import discord
from discord.ext import commands

PREFIX = 'iki-'

TOKEN = 'your token'
bot = commands.Bot(command_prefix=PREFIX)  # создание префикса
bot.remove_command(name='help')  # удаление предустановленной команды help


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)  # разрешена получение данных о сообщении
async def hi(ctx):  # создаём асинхронную функцию бота
    await ctx.send('И тебе привет, ' + ctx.message.author.name)  # отправляем сообщение с именем автора


@bot.command(pass_context=True)
async def help(ctx, *args):  # создание embed'a для листа команд
    if len(args) == 0:
        emb = discord.Embed(title='Лист команд', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name='Ангор',
                       icon_url='https://avatars.yandex.net/get-music-content/192707/732e6f8f.a.5361061-1/m1000x1000?webp=false')
        emb.add_field(name='Обычные команды',
                      value="`hi` `say` `kick`")
        emb.add_field(name='Игровые команды',
                      value="`inventory` `battle`")
        await ctx.send(embed=emb)
    elif args[0] == ('hi'):
        emb = discord.Embed(title='Простые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name='Ангор',
                       icon_url='https://avatars.yandex.net/get-music-content/192707/732e6f8f.a.5361061-1/m1000x1000?webp=false')
        emb.add_field(name='{}hi'.format(PREFIX), value='Простое приветсвие. Ничего особенного')
        await ctx.send(embed=emb)
    elif args[0] == 'say':
        emb = discord.Embed(title='Простые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name='Ангор',
                       icon_url='https://avatars.yandex.net/get-music-content/192707/732e6f8f.a.5361061-1/m1000x1000?webp=false')
        emb.add_field(name='{}say'.format(PREFIX), value='Говорит то, что вы напишите')
        await ctx.send(embed=emb)
    elif args[0] == 'kick':
        emb = discord.Embed(title='Простые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name='Ангор',
                       icon_url='https://avatars.yandex.net/get-music-content/192707/732e6f8f.a.5361061-1/m1000x1000?webp=false')
        emb.add_field(name='{}kick'.format(PREFIX), value='Пинает вызванного вами человека')
        await ctx.send(embed=emb)
    elif args[0] == 'inventory':
        emb = discord.Embed(title='Игровые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name='Ангор',
                       icon_url='https://avatars.yandex.net/get-music-content/192707/732e6f8f.a.5361061-1/m1000x1000?webp=false')
        emb.add_field(name='{}inventory'.format(PREFIX), value='Пока в разработке! Вызывает инвентарь ваших вещей')
        await ctx.send(embed=emb)
    elif args[0] == 'battle':
        emb = discord.Embed(title='Игровые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name='Ангор',
                       icon_url='https://avatars.yandex.net/get-music-content/192707/732e6f8f.a.5361061-1/m1000x1000?webp=false')
        emb.add_field(name='{}battle'.format(PREFIX),
                      value='Пока в разработке! Вы бросаете вызов человеку и далее сражаетесь или нет')
        await ctx.send(embed=emb)
    else:
        await ctx.send('У меня нет такой команды :(')


@bot.command(pass_context=True)
# async def say(ctx, channel_id, *, arg):
#     ctx.channel.id = int(channel_id[2:-1])
#     await ctx.send(arg)
async def say(ctx, *args):
    try:
        channel_id = args[0]
        mother_id = ctx.channel.id
        ctx.channel.id = int(channel_id[2:-1])
        message = ''
        for i in range(1, len(args)):
            message += args[i]+' '
        await ctx.send(message)
        ctx.channel.id = mother_id
    except:
        message = ''
        for i in range(len(args)):
            message += args[i]+' '
        await ctx.send(message)


@bot.command(pass_context=True)
async def kick(ctx, id):
    await ctx.send('Я пнул этого лоха ' + id)


@bot.command(pass_context=True)
async def inventory(ctx, id):
    # код инвентаря, sql, все дела
    await ctx.send()


@bot.command(pass_context=True)
async def battle(ctx, id):
    # код боёвки. Возможно рандомное число и какой-нибудь коэф или что-то вроде того
    # через ивент проверять согласие или отакз человека от боя
    await ctx.send()


bot.run(TOKEN)
