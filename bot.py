import discord
import time
from key import token

client = discord.Client()
bot_channel = "road-to-10k"


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    # print(message.content)

    if message.content.startswith("-count "):
        if str(message.channel) == bot_channel:
            parameters = message.content.split()

            if len(parameters) >= 2:
                try:
                    for i in range(int(parameters[1]), int(parameters[2]) + 1):
                        await message.channel.send(i)
                        time.sleep(1)
                    await message.channel.send("finished counting")

                except ValueError:
                    await message.channel.send("invalid parameters dummy")
        else:
            await message.channel.send(f"command only usable in #{bot_channel}")

    if message.content == "-help":
        await message.channel.send("Type: '-count (from) (to)'")

    if message.content == "-die":
        await message.channel.send("goodbye")
        await client.close()

client.run(token)
