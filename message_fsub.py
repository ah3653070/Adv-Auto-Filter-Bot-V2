update_channel = UPDATE_CHANNEL
#    if update_channel:
#        try:
#           user = await motech.get_chat_member(update_channel, msg.chat.id)
#           if user.status == "kicked out":
#              await msg.reply_text("😔 Sorry Dude, You are 🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜")
#              return
#       except UserNotParticipant:
#            #await msg.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
#            await msg.reply_text(
#                text="<b>📢 JOIN MY UPDATE CHANNEL 📢</b>",
#                reply_markup=InlineKeyboardMarkup([
#                   [ InlineKeyboardButton(text="⚠️ 𝙹𝚘𝚒𝚗 𝚖𝚢 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ⚠️ ", url=f"t.me/{UPDATE_CHANNEL}")]
#              ])
#            )
#           return
#       except Exception:
#            await msg.reply_text(f"💢Add This Channel @{UPDATE_CHANNEL}")
#            return"""
