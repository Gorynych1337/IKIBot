import discord
from discord.ext import commands

default_prefix = 'iki-'
custom_prefixes = {}
TOKEN = 'your token'
logs_switch = False
logs_channel = ''
botName = 'Ангрон'
botIconUrl = 'https://avatars.yandex.net/get-music-content/192707/732e6f8f.a.5361061-1/m1000x1000?webp=false'
bot = commands.Bot(command_prefix=default_prefix)  # создание префикса
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
    if logs_switch == True:
        await log_message(ctx,
                          '@' + str(ctx.message.author) + ' поприветствовал меня в #' + str(ctx.channel))


@bot.command(pass_context=True)
async def help(ctx, *args):  # создание embed'a для листа команд
    if len(args) == 0:
        emb = discord.Embed(title='Лист команд', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='Обычные команды',
                      value="`hi`, `say`, `kick`")
        emb.add_field(name='Игровые команды',
                      value="`inventory`, `battle`")
        emb.add_field(name='Настройка бота',
                      value='`log_channel`, `log_switch`, `prefix`')
        await ctx.send(embed=emb)
    elif args[0] == ('hi'):
        emb = discord.Embed(title='Простые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='{}hi'.format(default_prefix), value='Простое приветсвие. Ничего особенного')
        await ctx.send(embed=emb)
    elif args[0] == 'say':
        emb = discord.Embed(title='Простые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='{}say'.format(default_prefix), value='Говорит то, что вы напишите')
        await ctx.send(embed=emb)
    elif args[0] == 'kick':
        emb = discord.Embed(title='Простые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='{}kick'.format(default_prefix), value='Пинает вызванного вами человека')
        await ctx.send(embed=emb)
    elif args[0] == 'inventory':
        emb = discord.Embed(title='Игровые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='{}inventory'.format(default_prefix),
                      value='Пока в разработке! Вызывает инвентарь ваших вещей')
        await ctx.send(embed=emb)
    elif args[0] == 'battle':
        emb = discord.Embed(title='Игровые команды', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='{}battle'.format(default_prefix),
                      value='Пока в разработке! Вы бросаете вызов человеку и далее сражаетесь или нет')
        await ctx.send(embed=emb)
    elif args[0] == 'log_channel':
        emb = discord.Embed(title='Настройка бота', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='{}log_channel'.format(default_prefix),
                      value='Выбор канала для создания логов')
        await ctx.send(embed=emb)
    elif args[0] == 'log_switch':
        emb = discord.Embed(title='Настройка бота', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='{}log_switch'.format(default_prefix),
                      value='Включение/выключение ведения логов. Необходимы значения true или false')
        await ctx.send(embed=emb)
    elif args[0] == 'prefix':
        emb = discord.Embed(title='Настройка бота', colour=discord.Colour.from_rgb(150, 206, 214))
        emb.set_author(name=botName,
                       icon_url=botIconUrl)
        emb.add_field(name='{}prefix'.format(default_prefix),
                      value='Пока в разработке! Изменение префикса')
        await ctx.send(embed=emb)
    else:
        await ctx.send('У меня нет такой команды :(')


@bot.command(pass_context=True)
async def say(ctx, *args):
    try:
        channel_id = args[0]
        mother_id = ctx.channel.id
        ctx.channel.id = int(channel_id[2:-1])
        message = ''
        for i in range(1, len(args)):
            message += args[i] + ' '
        await ctx.send(message)
        ctx.channel.id = mother_id
    except:
        message = ''
        for i in range(len(args)):
            message += args[i] + ' '
        await ctx.send(message)


@bot.command(pass_context=True)
async def kick(ctx, id):
    await ctx.send('Я пнул этого лоха ' + id)
    if logs_switch == True:
        await log_message(ctx,
                          '@' + str(ctx.message.author) + ' пинает людей в #' + str(
                              ctx.channel) + '. Мне это не нравится')


class forGuild(commands.Cog, ):
    @commands.guild_only()
    @commands.command()
    async def log_switch(self, ctx, arg):
        global logs_switch
        global logs_channel
        if arg == 'true':
            logs_switch = True
            logs_channel = ctx.channel.id
            await ctx.send('Логи включены на сервере')
        elif arg == 'false':
            logs_switch = False
            await ctx.send('Логи выключены на сервере')
        else:
            await ctx.send('Введено неправильное значение')

    @commands.guild_only()
    @commands.command()
    async def log_channel(self, ctx, channel_id):
        global logs_channel
        logs_channel = int(channel_id[2:-1])
        await ctx.send('Канал логов изменнён на ' + channel_id)

    @commands.guild_only()
    @commands.command()
    async def prefix(self, ctx, *, prefixes=""):
        global custom_prefixes
        global default_prefix
        custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefix
        bot = commands.Bot(command_prefix=determine_prefix)
        bot.run()
        await ctx.send("Prefixes set!")


bot.add_cog(forGuild(bot))


async def log_message(ctx, data):
    mother_id = ctx.channel.id
    ctx.channel.id = logs_channel
    await ctx.send(data)
    ctx.channel.id = mother_id


async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefix)
    else:
        return default_prefix


@bot.command(pass_context=True)
async def inventory(ctx, id):
    # код инвентаря, sql, все дела
    await ctx.send()


@bot.command(pass_context=True)
async def battle(ctx, id):
    # код боёвки. Возможно рандомное число и какой-нибудь коэф или что-то вроде того
    # через ивент проверять согласие или отакз человека от боя
    await ctx.send()
    if logs_switch == True:
        await log_message(ctx,  # battle-data
                          )


bot.run(TOKEN)
