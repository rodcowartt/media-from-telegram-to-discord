from telethon import TelegramClient, sync, events
import discord
import os, glob
import nest_asyncio
import pathlib

nest_asyncio.apply()

api_id = 11111111 #https://my.telegram.org/apps
api_hash = 'hash'
name='Your Name'
TgClient = TelegramClient(name,api_id, api_hash)

for file in glob.glob("./media/*"): #on start of the script this will delete old files from folder
    os.remove(file)
    print("Deleted " + str(file))


@TgClient.on(events.NewMessage(from_users={'username1','username2'}))#creates an event that catches new messages from telegram (for choosed usernames)
async def handler(event):
    if event:
        FileName=str(event.message.file.name) #full name of the downloaded file
        FilePath='./media/'+FileName #path to the downloaded file
        await TgClient.download_media(event.message, FilePath) #downloading file
        print(' Name: ' + FileName) #None.jpg if file is image and full name if video, but if message is forwarded then None.jpg or None.mp4
        FindАdvertising = event.message.message.find("http") #searching "http" in message with attached file
        if FindАdvertising!=-1:
            print("It`s an Advertisement, not gonna post it")
        else:
            print("There is no Advertisement")

            currentDirectory = pathlib.Path('./media/') 
            DsClient = discord.Client(intents=intents)

            @DsClient.event
            async def on_ready(): #event starts when discord bot is logged in
                print('We have logged in as {0.user}'.format(DsClient))
                channel = DsClient.get_channel(1031981900425867354) #channel id from discord
                for currentFile in currentDirectory.iterdir(): #for each file in media folder 
                    FilePath = currentFile
                    if (os.path.getsize(FilePath) < 8000000):  #sends file into channel or deletes it if it`s too large
                        await channel.send(file=discord.File(FilePath))# sends file into channel
                    else:
                        print("File is too LARGE")
                        os.remove(FilePath) #deleting file
                await DsClient.close() #disconnetcing bot
                DsClient.clear()
                # Loop Through the folder projects all files and deleting them one by one
                for file in glob.glob("./media/*"):#delete old files from folder
                    os.remove(file)
                    print("Deleted " + str(file))

            await DsClient.start('Your`s discord bot TOKEN')

TgClient.start()
TgClient.run_until_disconnected()
