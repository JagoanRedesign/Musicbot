from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo: 
        fuk = await message.reply_text("» ᴍᴇɴɢᴜʙᴀʜ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ᴀꜱɪꜱᴛᴇɴ...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» {ASS_MENTION} ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴜʙᴀʜ."
            )
        except:     	                               
            return await fuk.edit_text("» ɢᴀɢᴀʟ ᴍᴇɴɢᴜʙᴀʜ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ᴀꜱɪꜱᴛᴇɴ.")
    else:
        await message.reply_text(
            "» ʀᴇᴘʟʏ ꜰᴏᴛᴏ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ᴀꜱɪꜱᴛᴇɴ."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "» ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢʜᴀᴘᴜꜱ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ᴀꜱɪꜱᴛᴇɴ."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("» ɢᴀɢᴀʟ ᴍᴇɴɢʜᴀᴘᴜꜱ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ᴀꜱɪꜱᴛᴇɴ.")


@app.on_message(filters.command(["assbio", "setbio"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ASS_MENTION} ʙɪᴏ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴜʙᴀʜ."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"» {ASS_MENTION} ʙɪᴏ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴜʙᴀʜ.")
    else:
        return await message.reply_text(
            "» ʀᴇᴘʟʏ ᴘᴇꜱᴀɴ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ʙᴇʙᴇʀᴀᴘᴀ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴊᴀᴅɪᴋᴀɴɴʏᴀ ꜱᴇʙᴀɢᴀɪ ʙɪᴏ ᴀꜱɪꜱᴛᴇɴ."
        ) 


@app.on_message(filters.command(["assname", "setname"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ASS_MENTION} ɴᴀᴍᴀ ʙᴇʀʜᴀꜱɪʟ ᴅɪʀᴜʙᴀʜ."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ASS_MENTION} ɴᴀᴍᴇ ɴᴀᴍᴀ ʙᴇʀʜᴀꜱɪʟ ᴅɪʀᴜʙᴀʜ.")
    else:
        return await message.reply_text(
            "» ʀᴇᴘʟʏ ᴘᴇꜱᴀɴ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ʙᴇʙᴇʀᴀᴘᴀ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴊᴀᴅɪᴋᴀɴɴʏᴀ ꜱᴇʙᴀɢᴀɪ ɴᴀᴍᴀ ᴀꜱɪꜱᴛᴇɴ."
        )




TARGET = -1001651683956
@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def welcome(client, message):
   text = f"Halo {message.new_chat_members[0].first_name}, dan selamat datang di {message.chat.title}!"
     await app2.reply_text(text, disable_web_page_preview=True)



