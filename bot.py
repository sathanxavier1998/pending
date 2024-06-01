import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQBlBywASL2ssWIlZFwnrLe0lO0vnr6Y4txVf3xXf7FkWESdhzoBT_Tdengyr39tMWB6bAnjKGrez9qYQGOLWB-zCgA1dq2EF1J1FZhVKM-tMQVvpCpWjIE9Fh2k1SayY0FYSUPfodLWqUleqrFV8OZbEd8bil3u4kejXNppL0ADbwpreAotsg8Ywi28u8vJ2gP3QplUsOr7yk5il1Wc_lj4MuOZcDhT_e8O11oG_y--ig3krGQIzjFO0G2jKySlMpfaW6uaKZJjTwxKvXlyS-A9GHsHS17RDDi_MnbhOZtXvcNMwyxcVSf5dwzNfcjgCQ6--BQs6csu5vkKdtKIkIVK6TXOIgAAAAGZvkloAA")        
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq to accept within seconds 💀
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await msg.delete()


logging.info("Bot Started....")
User.run()







