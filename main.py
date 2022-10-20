from telethon import TelegramClient, sync, events
import discord
import os, glob
import nest_asyncio
nest_asyncio.apply()

api_id = 11111111 #https://my.telegram.org/apps
api_hash = 'hash'
name='Your Name'
TgClient = TelegramClient(name,api_id, api_hash)


@TgClient.on(events.NewMessage(FromUsers={'username1','username2'}))#creates an event that catches new messages from telegram (for choosed usernames)
async def handler(event):
    if event:
        FileName=str(event.message.file.name) #full name of the downloaded file
        FilePath='./media/'+FileName #path to the downloaded file
        await TgClient.download_media(event.message, FilePath) #downloading file
        print(' Name: ' + FileName) #None.jpg if file is image and full name if video, but if message is forwarded then None.jpg or None.mp4
        
        if (os.path.getsize(FilePath) < 8000000):#Size of file verification (discord allows upload files 8 mb or least)
            intents = discord.Intents.default()
            intents.message_content = True

            DsClient = discord.Client(intents=intents)

            @DsClient.event
            async def on_ready():
                print('We have logged in as {0.user}'.format(DsClient))
                channel = DsClient.get_channel(1031981900425867354) #channel id from discord
                FileNameDefault = 'None'
                if (FileName == FileNameDefault):#sends file into channel
                    await channel.send(file=discord.File('./media/' + FileNameDefault + '.jpg'))
                    await channel.send(file=discord.File('./media/' + FileNameDefault + '.mp4'))
                else:
                    await channel.send(file=discord.File('./media/' + FileName))
                await DsClient.close()
                # Loop Through the folder projects all files and deleting them one by one
                for file in glob.glob("./media/*"):#delete old files from folder
                    os.remove(file)

            DsClient.run('Your`s discord bot TOKEN')
        else:
            print("File is too LARGE")
            for file in glob.glob("./media/*"): #deleting the big file, that bot can`t upload
                os.remove(file)
                print("Deleted " + str(file))

TgClient.start()
TgClient.run_until_disconnected()
