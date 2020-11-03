import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '.', intents=intents)

@client.command(aliases=['latency', 'ms'])
async def ping(ctx):
    await ctx.send(f'Returned in {round(client.latency * 1000)}ms.')

@client.command(aliases=['avatar'])
async def update(ctx):
    with open('react.png', 'rb') as f:
        await client.user.edit(avatar=f.read())
        await ctx.send(f'Updated avatar.')

@client.event
async def on_ready():
    print("Logged in.")
    
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 756312146803163198 or message_id == 758132060467494922 or message_id == 772976347592392716:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'SETA':
            role = discord.utils.get(guild.roles, name='Set A')
        elif payload.emoji.name == 'SETB':
            role = discord.utils.get(guild.roles, name='Set B')
        elif payload.emoji.name == 'SETC':
            role = discord.utils.get(guild.roles, name='Set C')
        elif payload.emoji.name == 'SETD':
            role = discord.utils.get(guild.roles, name='Set D')
        elif payload.emoji.name == 'SETE':
            role = discord.utils.get(guild.roles, name='Set E')
        elif payload.emoji.name == 'SETF':
            role = discord.utils.get(guild.roles, name='Set F')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("Assigned")
            else:
                print("Member not found")
        else:
            print("Role not found")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 756312146803163198 or message_id == 758132060467494922 or message_id == 772976347592392716:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'SETA':
            role = discord.utils.get(guild.roles, name='Set A')
        elif payload.emoji.name == 'SETB':
            role = discord.utils.get(guild.roles, name='Set B')
        elif payload.emoji.name == 'SETC':
            role = discord.utils.get(guild.roles, name='Set C')
        elif payload.emoji.name == 'SETD':
            role = discord.utils.get(guild.roles, name='Set D')
        elif payload.emoji.name == 'SETE':
            role = discord.utils.get(guild.roles, name='Set E')
        elif payload.emoji.name == 'SETF':
            role = discord.utils.get(guild.roles, name='Set F')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("Removed")
            else:
                print("Member not found")
        else:
            print("Role not found")

client.run(os.environ['DISCORD_TOKEN'])