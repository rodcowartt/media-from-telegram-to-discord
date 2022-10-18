from telethon import TelegramClient, sync, events
import discord
import os, glob
import nest_asyncio
nest_asyncio.apply()

api_id = 11111111 #https://my.telegram.org/apps
api_hash = 'hash'
name='Your Name'
client1 = TelegramClient(name,api_id, api_hash)


@client1.on(events.NewMessage(from_users={'username1','username2'}))#creates an event that catches new messages from telegramm (for choosed usernames)
async def handler(event):
    if event:
        filename='./media/'+str(event.message.file.name)
        await client1.download_media(event.message, filename)
        print(' Name: ' + str(event.message.file.name))#None.jpg if file is image and full name if video, but if message is forwarded then None.jpg or None.mp4
        f_name=str(event.message.file.name)#full name of the downloaded file
        intents = discord.Intents.default()
        intents.message_content = True

        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(client))
            channel = client.get_channel(1031981900425867354)#channel id from discord
            file_name_true = 'None'
            if (f_name == file_name_true):#sends file into channel
                await channel.send(file=discord.File('./media/' + file_name_true + '.jpg'))
                await channel.send(file=discord.File('./media/' + file_name_true + '.mp4'))
            else:
                await channel.send(file=discord.File('./media/' + f_name))
            await client.close()
            # Loop Through the folder projects all files and deleting them one by one
            for file in glob.glob("./media/*"):#delete old files from folder
                os.remove(file)

        client.run('Your`s discord bot TOKEN')
client1.start()
client1.run_until_disconnected()





