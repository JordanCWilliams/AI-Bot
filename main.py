import discord
import os
from neuralintents import GenericAssistant

TOKEN = 'OTcxMjQ5MTYyMTI3NTYwNzQ0.YnHwRQ.vgkGf2fbbBZcTqyV-HE_DsO-GuU'

chatbot = GenericAssistant('intent.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

TOKEN = os.getenv('TOKEN')


@client.event
async def on_message(message):
    if message.aithor == client.user:
        return

    if message.content.startswith("$aibot"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)


client.run(TOKEN)