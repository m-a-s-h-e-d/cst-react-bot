import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.command(aliases=['ping', 'latency', 'ms'])
async def ping(ctx):
    await ctx.send(f'Returned in {round(client.latency * 1000)}ms')

@client.command(aliases=['update', 'changeavatar'])
async def update():
    with open('react.png', 'rb') as f:
        await client.user.edit(avatar=f.read())

@client.event
async def on_ready():
    print("Logged in.")
    
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 756312146803163198:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

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
    if message_id == 756312146803163198:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

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
