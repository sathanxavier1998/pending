import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "AgG76v0AubV92ASTHWgEJl6yaXgLnfQzrLS-FN1c3FyS0CGhB7Po5V7ILiv3Mb784B8P5Jlo9bp6Fc0C-1m-7gZeg9ygblAHLl7NHL0KaWqmqf9PFvpPJAClWNrY0GySRGrAivCd5JpAHYq5e0CfSAvDZ3wKkgIpWCDAoRdqhxkIStSc5RiTrLqKlSO6V4WX1IU1_TZkulcRR_LLelpxXzxE7crqAqr7ZRl5sx1qLcBWxQwP4_Y4ivQN4pFzm2bcrMtlRY0FzM-2XVCGRNVj-FnHUOEoaRmCWJICP3JbJb6BeSnbJGt38qYsaez5xbjjbCKM0rUknmqQCQYKmTAqT71HhiVfsAAAAAA8lrkwAA")        
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







