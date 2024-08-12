import discord
from discord.ext import commands
import os
from hqmumudiliv2 import decrypt as dec
from hqmumudiliv2 import encrypt as enc

Bot = commands.Bot(command_prefix = ".")

@Bot.event
async def on_ready():
    print("Bot is working.")

@Bot.event
async def on_command_error():
    print("an unknown exception happened but skipped.")

@Bot.command()
async def encrypt(ctx, *, text):
    if len(text) > 199:
        await ctx.send("maximum character limit is 200.")
        print(f"{ctx.message.author} used encrypt but stucked at character limit.")
        return
    try:
        result = enc(text)
    except KeyError as e:
        await ctx.send(f"an error occured while encrypting: key {e} is not in the encypting keyboard. You cant encrypt this symbol.")
        print(f"{ctx.message.author} used encrypt but stucked at invalid keyboard value exception.")
        return
    print(f"{ctx.message.author} encrypted: {text}. Result: {result}")
    await ctx.send(f"```\n{result}\n```")

@Bot.command()
async def decrypt(ctx, *, text):
    if len(text) > 999:
        await ctx.send("maximum character limit is 1000.")
        print(f"{ctx.message.author} used decrypt but stucked at character limit.")
        return
    try:
        result = dec(text)
    except KeyError:
        await ctx.send("This is an invalid encrypted value. This value doesnt match properly with the decrypting technique.")
        print(f"{ctx.message.author} used decrypt but stucked at invalid encrypted value exception.")
        return
    print(f"{ctx.message.author} decrypted: {text}. Result: {result}")
    await ctx.send(f"```\n{result}\n```")
Bot.run("Toke")