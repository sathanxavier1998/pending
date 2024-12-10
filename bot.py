import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQGe8-oAlytmtBc24ff724Zk59iNxGsUKBa95ze6PF9R95fEVZGO3Zw1klK3fQE-_HhLtqeW2nLfMP23bTN-L1_wc_GIrO7P0ETau3U-HdrZbrewE1ainx1rCcZqTg5r-Fp_Hl8zNTeX6LH8WNnuJVMMdBxSUAfio2SGGnn-mgVM7m_cavdArhLlFjy3x8-YPKWvG-gbX1yXvGdbnXdUtqBwwt65sLBI4Mw9rss3cyoXAaRjJPHSK21kHOTgYc9kYGv9mn8kx8FzEaNgIWSDdAwL4LG8sU46EyGqOz3xcJ7qg45yWfSYBBWSg6mC-UL60-0GGdrdA7-p0iuQpoLHSP1ksl4_jgAAAAGnInKIAA")        
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







