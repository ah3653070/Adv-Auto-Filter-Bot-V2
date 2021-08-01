from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from config import Config 
from button import START_BUTTON, START_MSG
# Config 
UPDATE_CHANNEL = Config.UPDATE_CHANNEL
BOT_USER_NAME = Config.BOT_USER_NAME
SUB_TRY = Config.SUB_TRY
SUB_JOIN = Config.SUB_JOIN
SUB_TEXT = Config.SUB_TEXT
SUB_UPDATE = Config.SUB_UPDATE

# start and Update channel added
@Client.on_message(filters.private & filters.command("/start"))
async def start(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{SUB_JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{SUB_TRY}", url=f"https://t.me/{BOT_USER_NAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"{SUB_UPDATE} @{UPDATE_CHANNEL}")
            return  
    reply_markup =  START_BUTTON
    await update.reply_text(
        text=START_MSG.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )